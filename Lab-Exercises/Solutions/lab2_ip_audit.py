# Lab 2: The Multi-Cluster IP Audit Tool

cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": ["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18", "10.0.1.19"]
}

def calculate_capacity(config):
    # Count how many items are in the active_nodes list using a loop
    active_count = 0
    for _node in config["active_nodes"]:
        active_count += 1

    total_slots = config["total_max_slots"]

    # Run the mathematical formula to find utilization percentage
    utilization = (active_count / total_slots) * 100

    # Print the status statement
    print(f"--- Capacity Audit: {config['cluster_name']} ---")
    print(f"Active Nodes : {active_count}")
    print(f"Total Slots  : {total_slots}")
    print(f"Utilization  : {utilization:.1f}%")

# Execute the audit tool
calculate_capacity(cluster_config)
