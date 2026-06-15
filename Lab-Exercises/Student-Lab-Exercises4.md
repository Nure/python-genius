# Lab 4: The Profile Text Normalization Pipeline

### Learning Objectives

- Strings and String Methods (`.strip()`, `.lower()`)

- Lists and Loops

- Appending dynamic modifications to lists

### Scenario
A user filled out a human survey, but their input text is completely disorganized. There are erratic spaces everywhere, and the casing style is messy. You need to clean this text array before passing it downstream into production environments.

### Task Instructions

1. Loop through the raw list of unformatted data inputs.

2. For every item, remove any unnecessary background whitespace characters on the sides and force all lettering into complete lowercase.

3. Store the cleaned results dynamically into a new list named `sanitized_records`.

4. Output both lists to the terminal to visually verify the conversion results.

# --- STARTER CODE ---

```bash
raw_survey_inputs = ["  ALICE SMITH ", " dhaka, BANGLADESH  ", "  mLOpS_ENGineer  ", "  LIAM,MAYA "]
sanitized_records = []

# TODO: Write a loop to clean each string element and save it to sanitized_records


print(f"Raw Input: {raw_survey_inputs}")
print(f"Sanitized Production Input: {sanitized_records}")
```