# Change these values to verify different execution paths!
is_active = True
cpu_percent = 93.2
is_production = True

# 1. Build the compound logical matching condition statement based on the rules:
# Rule A: The server status is not active (not is_active)
# Rule B: CPU is high AND it is a production environment (cpu_percent > 90.0 and is_production)
should_alert = (not is_active) or (cpu_percent > 90.0 and is_production)

# 2. Conditional flow to broadcast the final verdict statement cleanly
if should_alert:
    print("[ALERT] Urgent dispatch! System needs manual intervention.")
else:
    print("[OK] System operating within safe margin bounds.")
