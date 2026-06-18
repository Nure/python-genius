# Lab 3 Solution Logic: The Deployment Budget Optimizer

## Goal
Estimate the monthly cost of a server group and approve or reject it against a
budget cap.

## Step-by-step Logic

1. **Function signature** — `estimate_deployment_cost(instance_count, hourly_rate,
   budget_cap)` accepts the three required inputs and **returns** a string (rather
   than printing), so callers can reuse the result.

2. **Cost formula** — a standard billing month is fixed at
   `30 days * 24 hours = 720 hours`:
   ```
   total_cost = instance_count * hourly_rate * 720
   ```

3. **Budget check (`if/else`)**
   - If `total_cost > budget_cap`: compute the overage (`total_cost - budget_cap`)
     and return a `REJECTED` message.
   - Otherwise: return an `APPROVED` message with the total cost.

4. **Clean number injection** — `{value:.2f}` formats dollars to two decimal places.

## Worked test cases
- `5 * 0.45 * 720 = 1620.00` vs cap `1500.00` → exceeds by `120.00` → **REJECTED**.
- `12 * 0.85 * 720 = 7344.00` vs cap `5000.00` → exceeds by `2344.00` → **REJECTED**.

## Why this works
Pulling the 720-hour constant into a named variable keeps the formula readable, and
returning strings keeps the function pure and testable.
