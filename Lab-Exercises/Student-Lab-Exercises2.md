## Lab 2: The Multi-Cluster IP Audit Tool


### Learning Objectives
- Lists (`list`) and Dictionaries (`dict`)

- Sequential Loops (`for loop`)

- Arithmetic Operations (Counting & Percentages)


### Scenario
Your cloud infrastructure just generated a raw audit log of all active internal application routes. You need to parse this map to tally how many endpoints exist and evaluate system capacity variables.


### Task Instructions
1. Use the provided `cluster_config` nested dictionary structure.

2. Write a function named `calculate_capacity` that uses a loop to extract the item values from the `active_nodes` list.

3. Calculate the percentage of cluster utilization:

$$\text{Utilization \%} = \left( \frac{\text{Active Nodes}}{\text{Total Max Slots}} \right) \times 100$$

4. Print a clean summary report using string interpolation.


# --- STARTER CODE ---
```bash
cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": ["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18", "10.0.1.19"]
}

def calculate_capacity(config):
    # TODO: Calculate how many items are in the active_nodes list
    # TODO: Run the mathematical formula to find utilization percentage
    # TODO: Print the status statement
    pass

# Execute the audit tool
calculate_capacity(cluster_config)

```