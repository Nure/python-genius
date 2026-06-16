cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": ["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18", "10.0.1.19"]
}


def calculate_capacity(config):
    cluster_name = config["cluster_name"]
    total_max_slots = config["total_max_slots"]
    active_nodes = config["active_nodes"]

    active_nodes_count = 0
    for node in active_nodes:
        active_nodes_count += bool(node)

    utilization_percentage = (
        float(active_nodes_count) / total_max_slots) * 100.00

    print(f" ###### Audit Report for Cluster: {cluster_name} ###### ")
    print(f" Total active nodes found: {active_nodes_count}")
    print(f" Total max slots available: {total_max_slots}")
    print(f" Utilization Percentage: {utilization_percentage:.2f}%")
    print("###### End of Report ######")


calculate_capacity(cluster_config)
