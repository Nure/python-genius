# Lab 4 Solution Logic: The Profile Text Normalization Pipeline

## Goal
Clean a list of messy survey strings into a normalized list ready for production.

## Step-by-step Logic

1. **Iterate** — loop over each `record` in `raw_survey_inputs`.

2. **Chain string methods** — for every record:
   - `.strip()` removes leading/trailing whitespace (the erratic outer spaces).
   - `.lower()` forces consistent lowercase casing.
   - Chaining (`record.strip().lower()`) applies both in one expression because each
     method returns a new string.

3. **Build a new list** — `sanitized_records.append(cleaned)` stores each result.
   The original `raw_survey_inputs` is left untouched (strings are immutable, and we
   never reassign into it), so we can print a before/after comparison.

4. **Verify** — print both lists to visually confirm the transformation.

## Note
`.strip()` only trims the *outer* whitespace; spaces inside an item (e.g.
`"alice smith"`) and characters like commas/underscores are preserved on purpose,
since those are part of the actual content.
