#!/usr/bin/env python3
"""Harshlings' own check: every exercise fails as it stands, every solution
passes. Run in CI and before every commit. Uses `hrs` and `rustc` on PATH."""
import glob, os, shutil, subprocess, sys, tempfile

import re
# An exercise that uses the matrix literals needs Harsh's standard library, the
# `hrs_std` crate, so it is built as a small Harsh project by `hrs` itself --
# `hrs_std` ships inside `hrs`, in Harsh's standard distribution -- one shared
# project, so nalgebra is compiled once.
CARGO = os.path.join(tempfile.gettempdir(), "harshlings-cargo")

def needs_std(path):
    return re.search(r"\b[mv]~|hrs_std", open(path).read()) is not None

def run_cargo(path):
    os.makedirs(os.path.join(CARGO, "src"), exist_ok=True)
    open(os.path.join(CARGO, "Cargo.toml"), "w").write(
        '[package]\nname = "exercise"\nversion = "0.1.0"\nedition = "2021"\n\n'
        '[[bin]]\nname = "exercise"\npath = "target/hrs/main.rs"\n\n[dependencies]\nhrs_std = "0.1"\n')
    shutil.copy(path, os.path.join(CARGO, "src", "main.hrs"))
    r = subprocess.run(["hrs", "build", "--quiet"], cwd=CARGO, capture_output=True, text=True)
    if r.returncode != 0:
        return ("compile" if "error[E" in r.stdout + r.stderr else "transpile"), r.stdout + r.stderr
    try:
        r = subprocess.run([os.path.join(CARGO, "target", "debug", "exercise")], capture_output=True, text=True, timeout=10)
    except subprocess.TimeoutExpired:
        return "hang", "did not finish in 10 seconds"
    if r.returncode != 0:
        return "run", r.stderr
    return "ok", r.stdout

def run(path):
    """('ok'|'transpile'|'compile'|'run', message) for one .hrs program."""
    if needs_std(path):
        return run_cargo(path)
    # Each program is built in a folder of its own, removed afterwards: left
    # behind, they came to 13 MB apiece and filled a disk over a few runs
    # (found 2026-09-24).
    d = tempfile.mkdtemp()
    try:
        return run_in(path, d)
    finally:
        shutil.rmtree(d, ignore_errors=True)

def run_in(path, d):
    rs = os.path.join(d, "main.rs")
    r = subprocess.run(["hrs", path, "-o", rs], capture_output=True, text=True)
    if r.returncode != 0:
        return "transpile", r.stderr
    r = subprocess.run(["rustc", "--edition", "2021", "-A", "warnings", rs, "-o", os.path.join(d, "main")],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return "compile", r.stderr
    try:
        r = subprocess.run([os.path.join(d, "main")], capture_output=True, text=True, timeout=10)
    except subprocess.TimeoutExpired:
        return "hang", "did not finish in 10 seconds"
    if r.returncode != 0:
        return "run", r.stderr
    return "ok", r.stdout

bad = 0
exercises = sorted(glob.glob("exercises/*/*.hrs"))  # numbered topics, zero-padded names: text order is the reading order
# `hrs fmt` must never be run over exercises/: several are broken by their
# layout, and the formatter would quietly repair them (it repaired layout1
# on 2026-09-11). Format src/ and solutions/ only.
for ex in exercises:
    name = os.path.basename(ex)[:-4]
    sol = ex.replace("exercises/", "solutions/", 1)
    hint = ex[:-4] + ".hint"
    src = open(ex).read()
    if "// I AM NOT DONE" not in src:
        print(f"FAIL {name}: no `// I AM NOT DONE` marker"); bad += 1
    if not os.path.exists(hint):
        print(f"FAIL {name}: no hint"); bad += 1
    stage, _ = run(ex)
    if stage == "hang":
        print(f"FAIL {name}: the exercise hangs instead of failing"); bad += 1; continue
    if stage == "ok":
        print(f"FAIL {name}: the exercise passes as it stands"); bad += 1
    if not os.path.exists(sol):
        print(f"FAIL {name}: no solution"); bad += 1; continue
    if "I AM NOT DONE" in open(sol).read():
        print(f"FAIL {name}: the solution still carries the marker"); bad += 1
    sstage, msg = run(sol)
    if sstage != "ok":
        print(f"FAIL {name}: the solution fails at {sstage}:\n{msg}"); bad += 1
    else:
        print(f"ok   {name}: fails at {stage}, solution passes")
print(f"{len(exercises)} exercise(s), {bad} problem(s)")
sys.exit(1 if bad else 0)
