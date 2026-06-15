# Lab 3: The Deployment Budget Optimizer
### Learning Objectives
- Functions with Parameters and Return values

- Arithmetic operations

- Comparative conditions (`>` ,`<=`)

### Scenario
Your financial team wants to make sure cloud spending doesn't go overboard. You need to build a function that dynamically figures out the total monthly operational cost of setting up server groups and raises flags if things get too expensive.

### Task Instructions

1. Create a function called `estimate_deployment_cost` that accepts three inputs: `instance_count`, `hourly_rate_per_instance`, and `budget_cap`.

2. Compute the total cost for a standard 30-day billing month (Assume $30 \text{ days} \times 24 \text{ hours} = 720 \text{ hours}$ of uptime total).

3. Check the calculated cost against the `budget_cap`:

- If the cost exceeds the cap, return an alert string: `"REJECTED: Budget Exceeded by $X!"`

- If it is within budget limits, return: `"APPROVED: Total Estimated Cost is $X."`

4. Inject the final dollar numbers inside your returned values cleanly.


# --- STARTER CODE ---

```bash

def estimate_deployment_cost(instance_count, hourly_rate, budget_cap):
    # TODO: Calculate total monthly cost (instances * hourly_rate * 720)
    # TODO: Implement if/else conditional check against budget_cap
    # TODO: Return the appropriate message string
    pass

# Test Cases to verify your execution:
print(estimate_deployment_cost(instance_count=5, hourly_rate=0.45, budget_cap=1500.00))
print(estimate_deployment_cost(instance_count=12, hourly_rate=0.85, budget_cap=5000.00))

```