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