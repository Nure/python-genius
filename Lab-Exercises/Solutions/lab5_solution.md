# Lab 5 Solution Logic: System Alert Flag Evaluator

## Goal
Combine three telemetry flags into one boolean that decides whether to page an
engineer.

## Step-by-step Logic

The alert rule is the **OR** of two independent failure conditions:

1. **Server down** — `not is_active`. If the server is not active, alert
   immediately, no matter the CPU.

2. **Overloaded production** — `cpu_percent > 90.0 and is_production`. High CPU is
   only urgent when it happens in a production environment. Both parts must be true
   (`and`).

Combined:
```python
should_alert = (not is_active) or (cpu_percent > 90.0 and is_production)
```

## Operator precedence
Python evaluates `not` first, then `and`, then `or`, so the parentheses are not
strictly required — but they make the two failure conditions explicit and readable.

## Trace of the sample values
`is_active=True`, `cpu_percent=94.5`, `is_production=True`:
- `not is_active` → `False`
- `94.5 > 90.0 and True` → `True`
- `False or True` → **`True`** → prints the `[ALERT]` line.

## Why this works
Grouping the CPU + production check together ensures a high CPU on a non-production
box won't wake anyone up, while a downed server always will.
