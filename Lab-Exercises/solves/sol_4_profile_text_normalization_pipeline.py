raw_survey_inputs = ["  ALICE SMITH ", " dhaka, BANGLADESH  ",
                     "  mLOpS_ENGineer  ", "  LIAM,MAYA "]
normalized_outputs = []

for text in raw_survey_inputs:
    normalized_text = text.strip().lower().replace(",", " ").replace("_", " ")
    normalized_outputs.append(normalized_text)

print(f"Raw Input: {raw_survey_inputs}")
print(f"Sanitized Production Input: {normalized_outputs}")
