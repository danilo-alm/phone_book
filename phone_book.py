from typing import List

class Contact:
    def __init__(self, name: str, phone_number: str = 'Empty',
                 email: str = 'Empty'):
        self.name = name.title()
        self.phone_number = str(phone_number)
        self.email = email
    
class Node:
    def __init__(self, contact: Contact, previous: 'Node' = None, next: 'Node' = None):
        self.prev = previous
        self.contact = contact
        self.next = next

class PhoneBook:

    def __init__(self, head=None):
        self.head = self.tail = head
        self.length = 1 if head else 0

    def push(self, node: Node):
        """
        Add a new Node to the beginning of the PhoneBook

        Args:
            node (Node): `Node` to be added
            
        
        Returns:
            None
        """
        node.next = self.head
        self.head.prev = node
        self.head = node

    def append(self, node: Node):
        """
        Add a new Node to the end of the PhoneBook

        Args:
            node (Node): `Node` to be added
        
        Returns:
            None
        """
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def add(self, contacts: List[Contact] or Contact):
        """
        Adds new contacts in the PhoneBook respecting alphabetic order

        Args:
            contacts (List[Contact] or Contact): Contact(s) to be added to list
        
        Returns:
            None
        """
        if not isinstance(contacts, list):
            contacts = [contacts]

        if self.head is None:
            self.head = self.tail = Node(contact=contacts.pop(0))
            self.length += 1

        while contacts:
            node = Node(contact=contacts.pop(0))

            curr = self.head
            while (curr.next is not None) and (node.contact.name > curr.next.contact.name):
                curr = curr.next
            
            if (curr == self.head) and (node.contact.name < curr.contact.name):
                self.push(node=node)
            elif curr.next is None:
                self.append(node=node)
            else:
                node.next = curr.next
                node.prev = curr
                curr.next.prev = node
                curr.next = node
            self.length += 1

    def get(self, index: int):
        """
        Return the `Contact` located in the index `index`

        Args:
            index (int): The index of the contact
        
        Returns:
            The `Contact` object you asked for
        """
        if index >= self.length:
            return IndexError
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        return curr.contact


    def remove(self, index: int, confirmation=True):
        """
        Remove the element in the index `index` from the PhoneBook

        Args:
            index (int): Index of the element to be removed
            confirmation (bool): show contact information and \
            ask whether user really wants to remove it
        
        Returns:
            the removed element
        """
        if index >= self.length:
            return IndexError
        
        if index == 0:
            curr = self.head
        elif index == self.length - 1:
            curr = self.tail
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        
        conf = True

        if confirmation:
            text = \
f'''Do you wish to remove the contact:\n{"-"*30}
Name: {curr.contact.name}
Phone Number: {curr.contact.phone_number}
Email: {curr.contact.email}\n{"-"*30}
(Yes/no): '''
            
            if input(text).strip().upper() != 'YES':
                conf = False

        return_value = None

        if conf:
            if index == 0:
                # Remove first element
                return_value = self.head
                self.head = self.head.next
                self.head.prev = None
            elif index == self.length - 1:
                # Remove last element
                return_value = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                return_value = curr
                curr.prev.next = curr.next
                curr.next.prev = curr.prev

        return return_value

    def print_contacts(self):
        """
        Iterate through every contact in the PhoneBook and print its information

        Args:
            None
        Returns:
            None
        """
        curr = self.head
        while curr is not None:
            name, email, phone_number = curr.contact.name, \
                                        curr.contact.email, \
                                        curr.contact.phone_number
            print('-'*30)
            print(f'Name: {name}\nEmail: {email}\nPhone Number: {phone_number}')
            curr = curr.next
    
    def print_debug(self):
        """
        Prints relevant information for debugging, such as some of PhoneBook's attributes
        and information about each PhoneBook's Node

        Args:
            None
        
        Returns:
            None
        """
        if self.head is None:
            return

        print('----- DEBUGGING -----')
        print(f'LIST\'S HEAD: {self.head.contact.name}\nLIST\'S TAIL: {self.tail.contact.name}\nLIST\'S SIZE: {self.length}')

        curr = self.head
        while curr is not None:
            print('-'*30)
            if curr.prev is not None:
                previous_name = curr.prev.contact.name
            else:
                previous_name = 'None'

            if curr.next is not None:
                next_name = curr.next.contact.name
            else:
                next_name = 'None'
            print(f'Previous: {previous_name}\nSelf: {curr.contact.name}\nNext: {next_name}')
            curr = curr.next
    
    def save_to_file(self, filepath: str):
        """
        Saves a doubly linked list to disk using pickle

        Args:
            filepath (str): The file path to save the linked list to.

        Returns:
            None
        """
        with open(filepath, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

# Debugging
if __name__ == '__main__':
    from random import shuffle
    import pickle

    pb = PhoneBook()
    contacts = []
    for name in ('ademar', 'bruno', 'cabral', 'daniel', 'zaratusta'):
        contacts.append(Contact(name=name, email='foo.bar@example.com', phone_number='00 1234 5678'))

    pb.add(contacts=contacts)
    pb.remove(index=1)
    pb.print_contacts()
