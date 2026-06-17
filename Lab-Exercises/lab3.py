
def estimate_deployment_cost(instance_count, hourly_rate, budget_cap):
    # 1. Calculate total uptime hours for a standard 30-day month (30 days * 24 hours)
    total_hours = 720
    
    # 2. Compute the total monthly operational cost
    total_cost = instance_count * hourly_rate * total_hours
    
    # 3. Perform conditional check against the financial budget cap
    if total_cost > budget_cap:
        over_budget = total_cost - budget_cap
        return f"REJECTED: Budget Exceeded by ${over_budget:.2f}!"
    else:
        return f"APPROVED: Total Estimated Cost is ${total_cost:.2f}."

# --- Test Cases designed to trigger one APPROVED and one REJECTED outcome ---

# Test Case 1: Total cost is $1,080.00, which sits comfortably within the $1,500.00 cap (APPROVED)
print(estimate_deployment_cost(instance_count=5, hourly_rate=0.30, budget_cap=1500.00))

# Test Case 2: Total cost is $7,344.00, which cleanly breaches the $5,000.00 limit (REJECTED)
print(estimate_deployment_cost(instance_count=12, hourly_rate=0.85, budget_cap=5000.00))
