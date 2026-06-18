# Lab 5: System Alert Flag Evaluator

# Change these values to verify different execution paths!
is_active = True
cpu_percent = 94.5
is_production = True

# Build the compound logical matching condition statement.
# Alert if the server is down, OR if CPU is critically high in production.
should_alert = (not is_active) or (cpu_percent > 90.0 and is_production)

if should_alert:
    print("[ALERT] Urgent dispatch! System needs manual intervention.")
else:
    print("[OK] System operating within safe margin bounds.")
