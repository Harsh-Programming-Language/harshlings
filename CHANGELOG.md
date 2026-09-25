# Changelog

## 0.1.6 — 2026-09-24

- **Macros, by who wrote them** (the user's architecture): Harsh macros (~), Rust macros (!), Rust DSLs (!), Harsh DSLs (~), each with its declarative and procedural kinds. Each `23_macros` exercise names its part; `macros03` is `extern` blocks, not a macro. The README maps the exercises onto it, and says why procedural macros are taught in the Book rather than here.
- **Fixed:** `verify.py` left a 13 MB folder behind for every program it checked; it now removes each one.
- **Fixed:** the README's topic list (it predated `18_comprehensions` and `19_matrices`, and named `21_macros`); `macros02`'s header said `macro_rules!` for a `macro_rules~`.

## 0.1.5 — 2026-09-23

- **`macros04`**: the broken form is now Rust's habit, `pair! (1, 2)`; the lesson is `pair! 1 2` (Harsh 0.1.24 retired `m! do:`).

## 0.1.4 — 2026-09-23

- **`vec!` is written as Harsh writes any call:** `vec! 1 2 3`, and `vec! { 0; n }` for a repeated value. The bracket spelling now means a vector holding one array and is refused (Harsh 0.1.23). Needs `harsh-lang` 0.1.23.
- **`macros04` teaches `pair! 1 2`**: the `m!\` spelling it taught is retired (Harsh 0.1.24).

## 0.1.3 — 2026-09-21

- **19 Matrices** grows by three, for Harsh 0.1.21: `matrices05` takes a part of a matrix (`slice`, and the view `&a[1.., 1..]`), `matrices06` tells the matrix product from `.*`, `matrices07` marks a function `<>` to apply it to each element. They need `harsh-lang` 0.1.21 and `hrs_std` 0.1.1.

## 0.1.2 — 2026-09-21

- `comprehensions06`: a condition attached to the wrong `for`, where the names it tests do not exist yet. The fix is to move it, not rewrite it.

## 0.1.1 — 2026-09-21

- Two new sections, for what Harsh adds to Rust: **18 Comprehensions** (five exercises: `g~`, conditions, several `for`s, `dict~`, laziness) and **19 Matrices** (four: the literal, the product, `solve`, and a least-squares fit). The old 18–21 are now 20–23.
- `macros02` in the matcher's form of `hrs` 0.1.30: a metavariable is written in its parentheses, `(($x:expr))` inside the arm's own.
- Exercises that use `m~`/`v~` are built by `hrs` as a small Harsh project: `hrs_std` ships inside `hrs` 0.1.30, so nothing is fetched and no variable is needed; rustc's errors and a panic's place land on the exercise's lines.
- `verify.py` reports an exercise that hangs instead of crashing on it.

