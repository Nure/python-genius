# Lab 2 Solution Logic: The Multi-Cluster IP Audit Tool

## Goal
Parse a nested cluster config, count the active nodes with a loop, and report
the cluster utilization percentage.

## Step-by-step Logic

1. **Access nested data** — `cluster_config` is a dictionary. We read values by
   key: `config["active_nodes"]` (a list) and `config["total_max_slots"]` (an int).

2. **Count with a loop** — the task explicitly asks for a `for` loop, so instead of
   `len()` we iterate over `active_nodes` and increment `active_count` once per
   element. The loop variable is named `_node` because we only care about the
   count, not the value.

3. **Utilization formula**
   ```
   Utilization % = (Active Nodes / Total Max Slots) * 100
   ```
   With 5 active nodes and 8 slots: `(5 / 8) * 100 = 62.5%`.

4. **Report** — an f-string prints a clean summary. `{utilization:.1f}` formats the
   percentage to one decimal place so the output stays tidy.

## Why this works
Dictionary key lookups give direct access to the structured config, and the manual
counter demonstrates loop-based aggregation that the lab is practicing.
