# Harshlings

Small exercises to get you used to reading and writing [Harsh](https://gitlab.com/bahiminin.benoit.dah.opensource/harsh-lang) — Rust without the braces. Each exercise is a short program with one thing wrong; the compiler tells you what, on the line of the `.hrs` file you are editing; you fix it, save, and the runner moves to the next. If you know Rustlings, this is that, in Harsh — with a set of exercises Rustlings cannot have, for the mistakes a new Harsh writer actually makes.

## Setup

```
cargo install harsh-lang           # hrs and its tools, once
git clone https://gitlab.com/bahiminin.benoit.dah.opensource/harshlings
cd harshlings
hrs run                            # builds the runner (written in Harsh) and starts watching
```

`hrs run` opens the first exercise that is not done, shows why it fails, and reruns every time you save a file under `exercises/`. When an exercise passes, delete its `// I AM NOT DONE` line and the runner moves on.

```
hrs run -- list                    # every exercise, done or not
hrs run -- run variables01          # one exercise, once
hrs run -- hint variables01         # when you are stuck
```

## The exercises

The topics are numbered in the order of *The Harsh Programming Language*, so the folder listing is the path through them:

```
01_variables   02_functions   03_control    04_layout      05_ownership
06_structs     07_enums       08_modules    09_collections 10_errors
11_generics    12_traits      13_lifetimes  14_tests       15_closures
16_iterators   17_pipes       18_patterns   19_smart_pointers
20_threads     21_macros
```

Harsh's own rules sit where the Book teaches the construct: the general layout ones at `04_layout` (a line at a column no block uses, a comma after a `match` arm, `()` where `$` belongs, a spaced `[` inside an application, the arrow against an application, a written `;`, `do:` as a value, a bare parameter before `->`), the `\` literal in a tuple with the structs, the chain with the iterators, a pipe given one value too many with the pipes, and `extern "C":` with the macros.

Each exercise has a hint, and each has a solution under `solutions/` — look only when the hint was not enough.

## For contributors

An exercise is `exercises/<topic>/<name>.hrs` (marked `// I AM NOT DONE`, with the task in a comment at the top), `exercises/<topic>/<name>.hint`, and `solutions/<topic>/<name>.hrs`. `python3 verify.py` checks all three for every exercise: the exercise must fail as it stands, the solution must pass, and the hint must exist. CI runs it on every push.

The runner is `src/main.hrs`, a Harsh program; `hrs fmt` lays it out.

## Licence

MPL-2.0, like Harsh.
