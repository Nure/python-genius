def estimate_deployment_costs(instance_count, hourly_rate_per_instance, budget_cap):
    monthly_cost = instance_count * hourly_rate_per_instance * 24 * 30

    if monthly_cost > budget_cap:
        excess_amount = monthly_cost - budget_cap
        return f"REJECTED: Budget Exceeded by ${excess_amount:.2f}"

    return f"APPROVED: Deployment within budget. Monthly Cost: ${monthly_cost:.2f}"


instance_count = 5
hourly_rate_per_instance = 0.45
budget_cap = 1500

print(estimate_deployment_costs(instance_count,
      hourly_rate_per_instance, budget_cap))

instance_count = 12
hourly_rate_per_instance = 0.85
budget_cap = 10000.00

print(estimate_deployment_costs(instance_count,
      hourly_rate_per_instance, budget_cap))
