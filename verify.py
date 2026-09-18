#!/usr/bin/env python3
"""Harshlings' own check: every exercise fails as it stands, every solution
passes. Run in CI and before every commit. Uses `hrs` and `rustc` on PATH."""
import glob, os, subprocess, sys, tempfile

def run(path):
    """('ok'|'transpile'|'compile'|'run', message) for one .hrs program."""
    d = tempfile.mkdtemp()
    rs = os.path.join(d, "main.rs")
    r = subprocess.run(["hrs", path, "-o", rs], capture_output=True, text=True)
    if r.returncode != 0:
        return "transpile", r.stderr
    r = subprocess.run(["rustc", "--edition", "2021", "-A", "warnings", rs, "-o", os.path.join(d, "main")],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return "compile", r.stderr
    r = subprocess.run([os.path.join(d, "main")], capture_output=True, text=True, timeout=10)
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
