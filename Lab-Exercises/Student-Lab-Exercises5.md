# Lab 5: System Alert Flag Evaluator

### Learning Objectives

- Complex boolean evaluations (`and`, `not`, `or`)

- Logical comparisons and flag validation

- Control execution states

### Scenario

You are developing an automated error monitoring daemon. It continuously looks at a series of active machine flags to evaluate whether an urgent maintenance engineer needs to be page-alerted out of bed.

### Task Instructions
1. Look at the three telemetry boolean flags provided in the scenario block below.

2. Create an overriding rule condition to trigger an alert (`should_alert = True`) if any of the following logical evaluations are met:

- The server status is not active (`is_active` is False).
- The CPU utilization is critically high (`cpu_percent > 90.0`) and it is a critical environment (`is_production` is True).

3. Use conditional flows to broadcast the final verdict statement cleanly.


# --- STARTER CODE ---
```bash
# Change these values to verify different execution paths!
is_active = True
cpu_percent = 94.5
is_production = True

# TODO: Build your compound logical matching condition statement
# should_alert = ???

if should_alert:
    print("[ALERT] Urgent dispatch! System needs manual intervention.")
else:
    print("[OK] System operating within safe margin bounds.")
```


