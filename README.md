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
16_iterators   17_pipes       18_comprehensions 19_matrices
20_patterns    21_smart_pointers 22_threads  23_macros
```

Harsh's own rules sit where the Book teaches the construct: the general layout ones at `04_layout` (a line at a column no block uses, a comma after a `match` arm, `()` where `$` belongs, a spaced `[` inside an application, the arrow against an application, a written `;`, `do:` as a value, a bare parameter before `->`), the `\` literal in a tuple with the structs, the chain with the iterators, a pipe given one value too many with the pipes, and `extern "C":` with the macros.

**Macros.** Harsh's macros are organised as the Rust Book organises Rust's, by who wrote them, and `23_macros` covers what a single file can hold:

- **Harsh macros (~)**, your own, written in Harsh -- declarative (`macros02`, defining a `macro_rules~`) and procedural: custom derive, attribute-like and function-like.
- **Rust macros (!)**, your own, written in Rust inside a Harsh project -- declarative (`macros04`, calling a `macro_rules!`) and procedural, in the same three kinds.
- **Harsh DSLs (~)**, imported from Harsh libraries -- Harsh throughout; the prelude's `g~` and `m~` are in `18_comprehensions` and `19_matrices`.
- **Rust DSLs (!)**, imported from Rust libraries -- called by Harsh's rules (`macros01`), their own languages in braces with Harsh holes.

Procedural macros, Harsh's and Rust's, each need a crate of their own, which a single-file exercise cannot hold; the Book teaches them in chapter 23 (sections 23.5 and 23.6), with a macro crate and the crate that uses it. `macros03` is `extern` blocks, not a macro: the Book teaches them in the same chapter.

Each exercise has a hint, and each has a solution under `solutions/` — look only when the hint was not enough.

## For contributors

An exercise is `exercises/<topic>/<name>.hrs` (marked `// I AM NOT DONE`, with the task in a comment at the top), `exercises/<topic>/<name>.hint`, and `solutions/<topic>/<name>.hrs`. `python3 verify.py` checks all three for every exercise: the exercise must fail as it stands, the solution must pass, and the hint must exist. CI runs it on every push.

The runner is `src/main.hrs`, a Harsh program; `hrs fmt` lays it out.

## Licence

MPL-2.0, like Harsh.

## Exercises that use matrices

The matrix exercises (`19_matrices`) use Harsh's standard library, `hrs_std`, which ships inside `hrs` itself -- Harsh's standard distribution -- so there is nothing more to install. They are built as one small Harsh project; the first one compiles the linear algebra underneath (`nalgebra`, fetched once from crates.io), so it needs the network and takes a little longer, and the rest reuse it.
