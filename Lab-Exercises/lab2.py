
cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": ["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18", "10.0.1.19"]
}

def calculate_capacity(config):
    # 1. use for loop for active_nodes count
    active_count = 0
    for node in config["active_nodes"]:
        active_count += 1
    
    # 2.Total max slot extract and get utilization percentage
    max_slots = config["total_max_slots"]
    utilization = (active_count / max_slots) * 100
    
    # 3. summery report print by (use f-string )
    print(f"""
=========================================
      MULTI-CLUSTER IP AUDIT REPORT
=========================================
Cluster Name     : {config['cluster_name']}
Active Endpoints : {active_count} Nodes
Max Capacity     : {max_slots} Slots
Current Load     : {utilization:.2f}%
=========================================
Status           : {"CRITICAL - Near Capacity" if utilization > 80 else "HEALTHY - Safe Load"}
=========================================
""")

# Execute the audit tool
calculate_capacity(cluster_config)
