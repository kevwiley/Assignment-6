class EmployeeNode:

    def __init__(self, name): 
        self.name = name 
        self.left = None 
        self.right = None 

class TeamTree:
    
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):

        if self.root is None: #accounts for edge case of no root being entered
            print("No root, please add one before entering employees.")
            return
        
        if current_node is None: #allows value to be assigned to root if it doesn't already have one
            current_node = self.root

        if current_node.name == manager_name:
            if side == "left" and current_node.left is None:#checks if user entered left, and if the left node is empty
                current_node.left = EmployeeNode(employee_name) #if left node is empty, replaces the None with input
                return True
            elif side == "right" and current_node.right is None: #same as left checks if user entered right, and if the right node is empty
                current_node.right = EmployeeNode(employee_name) #if right node is empty, replaces the None with input
                return True
            else:
                print(f"{manager_name} already has 2 employees") #if both left and right are filled tells user and doesn't replace anything.
                return True

        found_left = False
        found_right = False

        if current_node.left: # checks through left and right nodes using recursion
            found_left = self.insert(manager_name, employee_name, side, current_node.left)
        if current_node.right:
            found_right = self.insert(manager_name, employee_name, side, current_node.right)

        if not(found_left or found_right): # prints if node doesn't exist
            if current_node == self.root:
                print(f"Parent node {manager_name} not found in the tree.")
            return False
        return

    def print_tree(self, node=None, level=0):#prints out the contents of the tree

        if self.root is None: #maccounts for edge case to makes sure the tree has data in it
            print("Please enter data before trying to print list")
            return

        if node is None:
            if level == 0:
                node = self.root
            else:
                return
        
        indent = "    " * level #increases 
        print(f"{indent}-{node.name}") #prints indent then the name of node

        self.print_tree(node.left, level + 1) #increases node count each recursion until left or right node equals None
        self.print_tree(node.right, level + 1)


# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")
            

company_directory()




