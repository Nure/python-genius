# Lab 1 Solution Logic: The Smart Survey Onboarding Engine

## Goal
Interview a user, capture their profile, and assign a clearance tier based on age
and developer status.

## Step-by-step Logic

1. **Capture inputs** — `input()` always returns a string.
   - `name` stays a string.
   - `age` is cast with `int()` so it can be compared numerically.
   - The developer answer is normalized with `.strip().lower()` and compared to
     `"yes"`, producing a clean boolean (`is_developer`).

2. **Tier decision (`if-elif-else`)** — order matters here:
   - Check `age < 18` **first**. If true, the user is a Guest regardless of
     developer status.
   - Only if they are 18+ do we look at `is_developer`:
     - Developer → `Tier 1: Admin Infrastructure Access`.
     - Not a developer → `Tier 2: Standard Executive Access`.
   - Because each branch is mutually exclusive, exactly one tier is assigned.

3. **Output** — an f-string builds a readable profile card. A nested
   `{'Yes' if is_developer else 'No'}` converts the boolean back to friendly text.

## Why this works
The age gate is evaluated before the developer check, which matches the rule that
under-18 users can never reach Tier 1, even if they are developers.
