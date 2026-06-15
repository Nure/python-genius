class HumanSurvey:
    # The Constructor: sets up the attributes (variables) for every new instance
    def __init__(self, name, age, has_wife, kids):
        self.name = name          # Attribute
        self.age = age            # Attribute
        self.has_wife = has_wife  # Attribute
        self.kids = kids          # Attribute (List)

    # A method (function inside a class) representing human action/verb
    def introduce(self):
        return f"Hi, I'm {self.name} and I have {len(self.kids)} children."

# Creating INSTANCES (Objects) from the Class
nure_instance = HumanSurvey("Nure", 34, False, ["Abrar", "Arian"])
bob_instance = HumanSurvey("Bob", 40, True, ["Charlie"])

# Accessing Instance Data
print(nure_instance.introduce())
print(bob_instance.name)




# ---- Another-example
class EC2Server:
    def __init__(self, server_id, ip_address, instance_type, status="stopped"):
        self.server_id = server_id
        self.ip_address = ip_address
        self.instance_type = instance_type
        self.status = status

    def start_server(self):
        self.status = "running"
        return f"Server {self.server_id} at {self.ip_address} is now RUNNING."

    def stop_server(self):
        self.status = "stopped"
        return f"Server {self.server_id} has been SAFELY STOPPED."

# Creating Server Instances (Simulating Cloud Infrastructure)
web_server = EC2Server("i-099x123", "54.210.2.1", "t3.medium")
db_server = EC2Server("i-088x456", "10.0.1.4", "r5.large")

# Managing the infrastructure via Python
print(web_server.start_server())
print(f"Database Server Status: {db_server.status}")