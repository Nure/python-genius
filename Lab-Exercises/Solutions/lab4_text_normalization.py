# Lab 4: The Profile Text Normalization Pipeline

raw_survey_inputs = ["  ALICE SMITH ", " dhaka, BANGLADESH  ", "  mLOpS_ENGineer  ", "  LIAM,MAYA "]
sanitized_records = []

# Clean each string: strip surrounding whitespace, then force lowercase
for record in raw_survey_inputs:
    cleaned = record.strip().lower()
    sanitized_records.append(cleaned)

print(f"Raw Input: {raw_survey_inputs}")
print(f"Sanitized Production Input: {sanitized_records}")
