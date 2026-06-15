## Lab 1: The Smart Survey Onboarding Engine
### Learning Objectives
- `input()` capturing and Type Casting (`int`)

- Conditionals (`if-elif-else`) and Logic Operators (`and`, `or`)

- String Interpolation (`f-strings`)

### Scenario
You are building an entry portal for an automated processing system. The script must interview a human user, gather their basic profile info, and evaluate their clearance tier based on strict age rules.

### Task Instructions
1. Prompt the user for their `name`, `age`, and whether they are a `developer` (yes/no).

2. Cast the captured input data into its mathematically appropriate type.

3. Apply the following tier logic rules:

- If they are under 18, assign them to `"Tier 3: Guest"` access.

- If they are 18 or older and they are a developer, assign them to `"Tier 1: Admin Infrastructure Access"`.

- If they are 18 or older but not a developer, assign them to `"Tier 2: Standard Executive Access"`.

4. Output a personalized configuration summary string using an F-String.


# --- STARTER CODE ---

 ```bash 
 1. TODO: Capture inputs from user (Name, Age, Developer Status)


2. TODO: Evaluate conditional logic to determine the clearance tier


3. TODO: Print out the final profile card using an f-string
```