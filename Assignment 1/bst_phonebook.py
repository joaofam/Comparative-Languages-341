class Node:
    # intialize values to left, right, name, phone and address nodes
    def __init__(self, name, phone, address):
        self.left = None
        self.right = None
        self.name = name
        self.phone = phone
        self.address = address
    # string function to build the strings and return an output with the variable names and their assigned values.
    def __str__(self):
        string = "" #empty
        string = string + f"Name: {self.name}\n"
        string = string + f"Phone Number: {self.phone}\n"
        string = string f"Address: {self.address}\n"
        return string


class Name:
    def __init__(self):
        # set the root to none
        self.root = None

    # str function to join the string message as one
    def __str__(self):
        node_strs = [str(node) for node in self.inorder()]
        return "-----------------\n".join(node_strs)
    
    # insert function to insert nodes into BST
    def insert(self, name, phone, address):
        if self.root is None:
            self.root = Node(name, phone, address)
        else:
            self.rec_insert(self.root, name, phone, address)

    # recursion of insert
    def rec_insert(self, presentNode, name, phone, address):
        if name < presentNode.name:
            if presentNode.left:
                self.rec_insert(presentNode.left, name, phone, address)
            else:
                presentNode.left = Node(name, phone, address)
        elif name > presentNode.name:
            if presentNode.right:
                self.rec_insert(presentNode.right, name, phone, address)
            else:
                presentNode.right = Node(name, phone, address)
    # find function to search for certain node within BST
    def find(self, name):
        return self.rec_find(name, self.root)
        if name is None:
            print(node)
        else:
            return False
    # recursion of find in order to find node.
    def rec_find(self, name, node):
        if name == node.name:
            # if it exists print success
            print(node)
            return True
        
        if name < node.name:
            if node.left == None:
                # if it does not exist print error
                print("Name does not exist in the Phonebook\n")
                return False
            return self.rec_find(name, node.left)
        
        if node.right == None:
            # if it does not exist print error
            print("Name does not exist in the Phonebook\n")
            return False
        return self.rec_find(name, node.right)
    '''
    remove function in order to remove a name from the phonebook
    function was created with the aid of https://www.youtube.com/watch?v=LSju119w8BE
    '''
    def remove(self, name):
        # initaialize root as empty
        if self.root is None:
            return False
        
        # search for name within tree

        elif self.root.name == name:
            if self.root.left is None and self.root.right is None:
                self.root == None
            elif self.root and self.root.right is None:
                self.root == self.root.left
            elif self.root.left is None and self.root.right:
                self.root == self.root.right
            elif self.root.left and self.root.right:
                deleteParent = self.root
                deleteNode = self.root.right
                while deleteNode.left:
                    deleteParent = deleteNode
                    deleteNode = deleteNode.left
                
                self.root.name = deleteNode.name
                self.root.phone = deleteNode.phone
                self.root.address = deleteNode.address

                if deleteNode.right:
                    if deleteParent.name > deleteNode.name:
                        deleteParent.left = deleteNode.right
                    elif deleteParent.name < deleteNode.name:
                        deleteParent.right = deleteNode.right
                else:
                    if deleteNode.name < deleteParent.name:
                        deleteParent.left = None
                    else:
                        deleteParent.right = None

            return True
    
        parent = True
        node = self.root

        # find node to remove
        while node and node.name != name:
            parent = node
            if name < node.name:
                node = node.left
            elif name > node.name:
                node = node.right

        # if name does not exst within tree then output an error
        if node is None or node.name != name:
            print("Name does not exist within the PhoneBook\n")
            return False

        # remove node has no children (following BST rules)

        elif node.left is None and node.right is None:
            if name < parent.name:
                parent.left = None
            else:
                parent.right = None
            return True
        
        # remove node has left child only (following BST rules)

        elif node.left and node.right is None:
            if name < parent.name:
                parent.left = node.left
            else:
                parent.right = node.left
            return True

        # remove node that has right child only (following BST rules)

        elif node.left is None and node.right:
            if name < parent.name:
                parent.left = node.right
            else:
                parent.right = node.right
            return True

        # remove node that has left and right children (following BST rules)

        else:
            deleteParent = node
            deleteNode = node.right
            while deleteNode.left:
                deleteParent = deleteNode
                deleteNode = deleteNode.left
            
            node.name = deleteNode.name
            node.phone = deleteNode.phone
            node.address = deleteNode.address
            if deleteNode.right:
                if deleteParent.name > deleteNode.name:
                    deleteParent.left = deleteNode.right
                elif deleteParent.name < deleteParent.name:
                    deleteParent.right = deleteNode.right
            else:
                if deleteNode.name < deleteParent.name:
                    deleteParent.left = None
                else:
                    deleteParent.right = None
            
            return True

    # inorder function to display nodes added in an order of inorder
    def inorder(self):
        return self.rec_inorder(self.root, [])
    # recursion of inorder
    def rec_inorder(self, presentNode, lst):
        if presentNode.left:
            self.rec_inorder(presentNode.left, lst)
        if presentNode:
            lst.append(presentNode)
        if presentNode.right:
            self.rec_inorder(presentNode.right, lst)
        return lst

class Phone:
    def __init__(self):
        # set the root to empty
        self.root = None
    
    # string function to display phone contacts
    def __str__(self):
        node_strs = [str(node) for node in self.inorder()]
        return "-----------------\n".join(node_strs)

    # insert function to insert phone numbers into BST
    def insert(self, name, phone, address):
        if self.root is None:
            self.root = Node(name, phone, address)
        else:
            self.rec_insert(self.root, name, phone, address)
    # recursion of insert function
    def rec_insert(self, presentNode, name, phone, address):
        if phone < presentNode.phone:
            if presentNode.left:
                self.rec_insert(presentNode.left, name, phone, address)
            else:
                presentNode.left = Node(name, phone, address)
        elif phone > presentNode.phone:
            if presentNode.right:
                self.rec_insert(presentNode.right, name, phone, address)
            else:
                presentNode.right = Node(name, phone, address)
    # find function to search for phone numbers within phonebook
    def find(self, phone):
        self.rec_find(phone, self.root)
        if phone is None:
            print(node)
        else:
            return False
    # recursion of find function
    def rec_find(self, phone, node):
        if phone == node.phone:
            print(node)
            return True
        # if phone number does not exist in phonebook print error
        if phone < node.phone:
            if node.left == None:
                print("Phone number does not exist in PhoneBook\n")
                return False
            return self.rec_find(phone, node.left)
        # if phone number does not exist in phonebook print error
        if node.right == None:
            print("Phone number does not exist in PhoneBook\n")
            return False
        return self.rec_find(phone, node.right)
    '''
    remove function in order to remove a phone from the phonebook
    function was created with the aid of https://www.youtube.com/watch?v=LSju119w8BE
    '''
    def remove(self, phone):
        # initaialize root as empty
        if self.root is None:
            return False
        
       # search for name within tree

        elif self.root.phone == phone:
            if self.root.left is None and self.root.right is None:
                self.root == None
            elif self.root and self.root.right is None:
                self.root == self.root.left
            elif self.root.left is None and self.root.right:
                self.root == self.root.right
            elif self.root.left and self.root.right:
                deleteParent = self.root
                deleteNode = self.root.right
                while deleteNode.left:
                    deleteParent = deleteNode
                    deleteNode = deleteNode.left
                
                self.root.name = deleteNode.name
                self.root.phone = deleteNode.phone
                self.root.address = deleteNode.address

                if deleteNode.right:
                    if deleteParent.phone > deleteNode.phone:
                        deleteParent.left = deleteNode.right
                    elif deleteParent.phone < deleteNode.phone:
                        deleteParent.right = deleteNode.right
                else:
                    if deleteNode.phone < deleteParent.phone:
                        deleteParent.left = None
                    else:
                        deleteParent.right = None

            return True
    
        parent = True
        node = self.root

        # find node to remove
        while node and node.phone != phone:
            parent = node
            if phone < node.phone:
                node = node.left
            elif phone > node.phone:
                node = node.right

        # if number does not exst within tree then output an error
        if node is None or node.phone != phone:
            print("Phone number does not exist within the PhoneBook\n")
            return False

        # remove node has no children (following BST rules)

        elif node.left is None and node.right is None:
            if phone < parent.phone:
                parent.left = None
            else:
                parent.right = None
            return True
        
        # remove node has left child only (following BST rules)

        elif node.left and node.right is None:
            if phone < parent.phone:
                parent.left = node.left
            else:
                parent.right = node.left
            return True

        # remove node that has right child only (following BST rules)

        elif node.left is None and node.right:
            if phone < parent.phone:
                parent.left = node.right
            else:
                parent.right = node.right
            return True

        # remove node that has left and right children (following BST rules)

        else:
            deleteParent = node
            deleteNode = node.right
            while deleteNode.left:
                deleteParent = deleteNode
                deleteNode = deleteNode.left
            
            node.phone = deleteNode.phone
            node.name = deleteNode.name
            node.address = deleteNode.address
            if deleteNode.right:
                if deleteParent.phone > deleteNode.phone:
                    deleteParent.left = deleteNode.right
                elif deleteParent.phone < deleteParent.phone:
                    deleteParent.right = deleteNode.right
            else:
                if deleteNode.phone < deleteParent.phone:
                    deleteParent.left = None
                else:
                    deleteParent.right = None
            
            return True
    # inorder function to display nodes added in an order of inorder
    def inorder(self):
        return self.rec_inorder(self.root, [])
    # recursion of inorder  
    def rec_inorder(self, presentNode, lst):
        if presentNode.left:
            self.rec_inorder(presentNode.left, lst)
        if presentNode:
            lst.append(presentNode)
        if presentNode.right:
            self.rec_inorder(presentNode.right, lst)
        return lst

# Main function where functions and operations take place to display outputs and the phonebook

def main():
    # Assigning variables to call classes for name and phone
    phone = Phone()
    name = Name()

    # print function to display a welcoming to phonebook
    print("--------Welcome to the PhoneBook--------\nHere is a list of contacts contained within the PhoneBook:\n")
    # displaying contacts using name insert function
    name.insert("Joao", "08356456", "Portugal")
    name.insert("Cillian", "08746564", "Wexford")
    name.insert("John", "085546456", "Dublin 4")
    name.insert("Terry", "081665464", "Dublin 2")
    name.insert("Conor", "089234324", "Dublin 1")
    name.insert("Aisling", "082324324", "Dublin 13")
    # print contacts
    print(name)
    # displaying contacts using phone insert function
    phone.insert("Adam", "083423432", "Portugal")
    phone.insert("Brendo", "084464647", "Wexford")
    phone.insert("Stacey", "085656456", "Dublin 4")
    phone.insert("Amy", "081645646", "Dublin 2")
    phone.insert("Kerri", "0896456456", "Dublin 1")
    phone.insert("Kanya", "0826456464", "Dublin 13")
    # print contacts
    print(phone)
    
    # use of find function to see if name exits within phonebook
    print("Let's see if Aisling is in the PhoneBook:")
    name.find("Aisling")
    print("Let's see if Timmy is in the PhoneBook:")
    # if name does not exist an error will occur
    name.find("Timmy")

    # use of find function to see if phone exits within phonebook
    print("Let's see if 081645646 is in the PhoneBook:")
    phone.find("081645646")
    print("Let's see if 081645646 is in the PhoneBook:")
    # if phone does not exist an error will occur
    phone.find("0349383863")

    # use of remove function to remove a certain name and its contacts from the phonebook
    print("Remove Joao from PhoneBook:\n")
    print("Updated PhoneBook")
    name.remove("Joao")

    # dislay new updated phonebook
    print(name, phone)
    

    print("Remove Chandler from PhoneBook:")
    # if trying to remove a name and name does not exist an error is outputted
    name.remove("Chandler")
    # use of remove function to remove a certain phone and its contacts from the phonebook
    print("Remove 0896456456 from PhoneBook:\n")
    print("Updated PhoneBook")
    phone.remove("0896456456")

    # dislay new updated phonebook
    print(name, phone)

    print("Remove 09745734 from PhoneBook:")
    # if phone does not exist in phonebook, an error is outputted
    phone.remove("09745734")

if __name__ == "__main__":
    main()

# resources
# https://www.youtube.com/watch?v=LSju119w8BE
# https://www.tutorialspoint.com/python_data_structure/python_tree_traversal_algorithms.htm
# https://qvault.io/python/binary-search-tree-in-python/