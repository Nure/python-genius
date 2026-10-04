# 1. String (str)
# A string is a sequence of characters wrapped in matching single (') or double (") quotes. It is used to store text data.

# General Example: Storing a person's name or street address.

# DevOps Example: Storing a cloud region, an IP address, or a Git branch name.

# General
student_name = "Alice Smith"
home_address = "123 Cloud Lane, Texas"

# DevOps
aws_region = "us-east-1"
target_ip = "192.168.1.50"
git_branch = 'main'


# 2. Integer (int)
# An integer is a positive or negative whole number without any decimal points.

# General Example: Counting a person's age or the number of children they have.

# DevOps Example: Counting active server instances, container replicas, or network ports.

# General
user_age = 34
number_of_kids = 2

# DevOps
active_containers = 5
ssh_port = 22
max_retry_attempts = 3



# 3. Float (float)
# A float (floating-point number) represents real numbers that contain a decimal point.

# General Example: Storing financial amounts or physical measurements like height and weight.

# DevOps Example: Measuring performance metrics like CPU utilization, execution timers, or system latency.

# General
hourly_wage = 45.50
body_height_meters = 1.75

# DevOps
cpu_utilization_percent = 78.4
api_response_latency_seconds = 0.015
disk_free_space_gb = 120.0




# 4. List (list)
# A list is an ordered, changeable (mutable) collection of items wrapped in square brackets []. Lists can hold duplicate values and can even store a mix of different data types.

# General Example: A shopping list or a collection containing the names of a person's children.

# DevOps Example: A collection of server IP addresses, microservice names, or environment stages.

# General
children_names = ["Liam", "Maya", "Oliver"]
mixed_survey_data = ["Alice", 34, True]

# DevOps
web_cluster_ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
deployment_pipeline_stages = ["Build", "Test", "Deploy"]



# 5. Dictionary (dict)
# A dictionary is a collection of key-value pairs wrapped in curly braces {}. Instead of accessing items by an index number (like a list), you look up data using a specific label called a "key". Keys must be unique.

# General Example: A complete survey profile where every personal trait has a specific label.

# DevOps Example: A configuration file map representing environment settings or container specifications.

# General
human_survey_profile = {
    "name": "Alice Smith",
    "age": 34,
    "has_wife": False,
    "kids": ["Liam", "Maya"]
}

# DevOps
container_config = {
    "image": "nginx:latest",
    "exposed_port": 80,
    "environment": "production",
    "is_healthy": True
}

# How to access a dictionary value:
print(human_survey_profile["name"])  # Output: Alice Smith
print(container_config["exposed_port"])  # Output: 80