class OrganizationChart:
    def __init__(self) -> None:
        self.graph = {} 

    # add employees  # employee details : node, vertices 
    def add_employee(self, employee_id,employee_name):
        self.graph[employee_id] = {'name': employee_name, 'report_to' : []}
    
    # add the edges to my nodes 
    def add_relationships(self, employee_id, manager_id):
        self.graph[manager_id]['report_to'].append(employee_id)

    # display chart 
    def display_organization(self):
        for employee_id, details in self.graph.items():
            employee_name = details["name"]
            reports_to = details["report_to"]
            manager_name = [self.graph[manager_id]["name"] for manager_id in reports_to]
            print(f"employee id : {employee_id}, Employee Name: {employee_name}, Reports to: {manager_name}")



# Example usage: Organization chart as a graph
org_graph = OrganizationChart()
# Add employees
org_graph.add_employee(101, "John Doe")
org_graph.add_employee(105, "Alice Smith")
org_graph.add_employee(98, "Bob Johnson")
org_graph.add_employee(110, "Eve Williams")

# establish the graph relationship 
org_graph.add_relationships(98,101)
org_graph.add_relationships(110, 105)
org_graph.add_relationships(101,98)

# display ]
print("Organization")
org_graph.display_organization()