# pyhon Fundamental Labs Solutions Guide

This comprehensive solution guide provides the complete engineering breakdown, structural code, and operational verification logs for the Python Fundamental Assignment Labs (Lab 1 to Lab 5). All code solutions have been fully developed, validated locally, and committed to the remote repository.

---

# Python Fundamental Labs Solutions Guide

This comprehensive solution guide provides the complete engineering breakdown, structural code, and operational verification logs for the Python Fundamental Assignment Labs (Lab 1 to Lab 5). All code solutions have been fully developed, validated locally, and committed to the remote repository.

---

## Technical Specifications
- **Developer & Architect:** Md Shehab Kazi
- **Deployment Platform:** Linux Environment
- **Authentication Protocol:** Secure Shell (SSH Encryption Key via `git@github.com:shehabkazi-blip/python-genius.git`)
- **Execution Target:** Python 3.x Environment

## AI Attribution & Acknowledgments
- **Development Methodology:** This repository represents a hybrid development approach. The core logic gates, algorithmic conditions, and system workflows were mapped out based on the lab requirements, with structural optimization, precise float formatting (`:.2f`), and comprehensive markdown documentation pipelines generated with the strategic assistance of **Google Gemini AI**.
- **Purpose:** Leveraging AI-assisted engineering practices to ensure industry-standard code styling, clean execution logs, and professional-grade DevOps documentation.

---

## Lab 1: Automated Infrastructure Welcome Banner

### Objective
Initialize core environment variables (strings, integers) to build a dynamic, paramterized operational welcome greeting banner for cloud management terminals.

### Implementation Code
```python
# System environment variables initialization
developer_name = "Md Shehab Kazi"
system_role = "Solution Architect"
active_labs_count = 5

# Broadcast welcoming telemetry status using dynamic string interpolation
print(f"=========================================")
print(f"   WELCOME TO DEVOPS AUTOMATION ENGINE   ")
print(f"=========================================")
print(f"Operator Name : {developer_name}")
print(f"Designation   : {system_role}")
print(f"Active Tasks  : {active_labs_count} Core Pipeline Labs")
print(f"System Status : INITIALIZED & READY")
print(f"=========================================")
Verification Logs
Plaintext
=========================================
   WELCOME TO DEVOPS AUTOMATION ENGINE   
=========================================
Operator Name : Md Shehab Kazi
Designation   : Solution Architect
Active Tasks  : 5 Core Pipeline Labs
System Status : INITIALIZED & READY
=========================================
Lab 2: The Multi-Cluster IP Audit Tool
Objective
Parse nested dictionary maps representing data infrastructure configurations, compute dynamic resource nodes utilization percentage metrics, and formulate baseline structural diagnostics.

Implementation Code
Python
cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": ["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18", "10.0.1.19"]
}

def calculate_capacity(config):
    # Manual loop variable accumulator to dynamically parse current configuration elements
    active_count = 0
    for node in config["active_nodes"]:
        active_count += 1
    
    # Extract structural constraints and compute utilization
    max_slots = config["total_max_slots"]
    utilization = (active_count / max_slots) * 100
    
    # Broadcast formatted summary data
    print(f"=========================================")
    print(f"      MULTI-CLUSTER IP AUDIT REPORT      ")
    print(f"=========================================")
    print(f"Cluster Name     : {config['cluster_name']}")
    print(f"Active Endpoints : {active_count} Nodes")
    print(f"Max Capacity     : {max_slots} Slots")
    print(f"Current Load     : {utilization:.2f}%")
    print(f"=========================================")

# Execute telemetry check
calculate_capacity(cluster_config)
Verification Logs
Plaintext
=========================================
      MULTI-CLUSTER IP AUDIT REPORT      
=========================================
Cluster Name     : dhaka-prod-east
Active Endpoints : 5 Nodes
Max Capacity     : 8 Slots
Current Load     : 62.50%
=========================================
Lab 3: The Deployment Budget Optimizer
Objective
Enforce strict spending controls on server group scaling rules by designing a dynamic evaluation routine verifying hourly instance costs against a monthly billing budget threshold.

Implementation Code
Python
def estimate_deployment_cost(instance_count, hourly_rate, budget_cap):
    # Calculate baseline uptime standard hours (30 Days * 24 Hours)
    total_hours = 720
    
    # Compute gross configuration operational expenses
    total_cost = instance_count * hourly_rate * total_hours
    
    # Execute validation gate using clean float formatting bounds
    if total_cost > budget_cap:
        over_budget = total_cost - budget_cap
        return f"REJECTED: Budget Exceeded by ${over_budget:.2f}!"
    else:
        return f"APPROVED: Total Estimated Cost is ${total_cost:.2f}."

# --- Test Cases adjusted to validate both structural logic code path branches ---
# Test Case 1: Within Safe Boundaries (Triggers APPROVED Status)
print(estimate_deployment_cost(instance_count=5, hourly_rate=0.30, budget_cap=1500.00))

# Test Case 2: Breach Condition Active (Triggers REJECTED Status)
print(estimate_deployment_cost(instance_count=12, hourly_rate=0.85, budget_cap=5000.00))
Verification Logs
Plaintext
APPROVED: Total Estimated Cost is $1080.00.
REJECTED: Budget Exceeded by $2344.00!
Lab 4: The Profile Text Normalization Pipeline
Objective
Ingest raw unstructured array payloads from human-submitted entries and clean up erroneous padding artifacts and casing discrepancies to maintain database indexing integrity.

Implementation Code
Python
raw_survey_inputs = ["  ALICE SMITH ", " dhaka, BANGLADESH  ", "  mLOpS_ENGineer  ", "  LIAM,MAYA "]
sanitized_records = []

# Map raw records through cleanup loops to transform data properties
for record in raw_survey_inputs:
    # Execute method chaining to strip padding spaces and unify lowercase letters
    clean_record = record.strip().lower()
    
    # Commit sanitized string element to downstream system arrays
    sanitized_records.append(clean_record)

# Stream evaluation outputs to verifying terminal log
print(f"Raw Input: {raw_survey_inputs}")
print(f"Sanitized Production Input: {sanitized_records}")
Verification Logs
Plaintext
Raw Input: ['  ALICE SMITH ', ' dhaka, BANGLADESH  ', '  mLOpS_ENGineer  ', '  LIAM,MAYA ']
Sanitized Production Input: ['alice smith', 'dhaka, bangladesh', 'mlops_engineer', 'liam,maya']
Lab 5: System Alert Flag Evaluator
Objective
Orchestrate a real-time logical monitoring gateway running boolean diagnostic checks to verify host systems and trigger emergency on-call responder schedules upon threshold breaches.

Implementation Code
Python
# Modifiable parameters simulating standard cloud infrastructure telemetry signals
is_active = True
cpu_percent = 94.5
is_production = True

# Compound logic block processing specific threat evaluations using explicit operator priorities
should_alert = (not is_active) or (cpu_percent > 90.0 and is_production)

# Direct execution paths flow based on diagnostic matching verdict
if should_alert:
    print("[ALERT] Urgent dispatch! System needs manual intervention.")
else:
    print("[OK] System operating within safe margin bounds.")
Verification Logs
Plaintext
[ALERT] Urgent dispatch! System needs manual intervention.

---

### 🚀 Git Commands for Deployment:
Ekhon apnar lokali `README.md` file-e eita seave korar por, push korar jonno terminal-e por por ei tin-ti command run korun:

```bash
git add README.md
git commit -m "docs: finalize entire lab matrix from 1 to 5 in structured guide"
git push origin dev

