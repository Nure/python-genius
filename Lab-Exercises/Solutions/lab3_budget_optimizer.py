# Lab 3: The Deployment Budget Optimizer

def estimate_deployment_cost(instance_count, hourly_rate, budget_cap):
    # Calculate total monthly cost (30 days * 24 hours = 720 hours of uptime)
    HOURS_PER_MONTH = 720
    total_cost = instance_count * hourly_rate * HOURS_PER_MONTH

    # Compare against the budget cap and return the appropriate message
    if total_cost > budget_cap:
        overage = total_cost - budget_cap
        return f"REJECTED: Budget Exceeded by ${overage:.2f}!"
    else:
        return f"APPROVED: Total Estimated Cost is ${total_cost:.2f}."

# Test Cases to verify your execution:
print(estimate_deployment_cost(instance_count=5, hourly_rate=0.45, budget_cap=1500.00))
print(estimate_deployment_cost(instance_count=12, hourly_rate=0.85, budget_cap=5000.00))
