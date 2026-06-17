raw_survey_inputs = ["  ALICE SMITH ", " dhaka, BANGLADESH  ", "  mLOpS_ENGineer  ", "  LIAM,MAYA "]
sanitized_records = []

# Loop through each messy string in the raw inputs list
for record in raw_survey_inputs:
    # Remove leading/trailing whitespaces and convert characters to lowercase
    clean_record = record.strip().lower()
    
    # Append the newly formatted string into our production list
    sanitized_records.append(clean_record)

# Output both lists to the terminal to visually verify the transformation pipeline
print(f"Raw Input: {raw_survey_inputs}")
print(f"Sanitized Production Input: {sanitized_records}")
