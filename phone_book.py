from typing import List

class Contact:
    def __init__(self, name: str, phone_number: str = 'Empty',
                 email: str = 'Empty'):
        self.name = name.title()
        self.phone_number = str(phone_number)
        self.email = email
    
class Node:
    def __init__(self, contact: Contact, previous: 'Node' = None, next: 'Node' = None):
        self.previous = previous
        self.contact = contact
        self.next = next

class PhoneBook:
    length = 0

    def __init__(self, head=None):
        self.head = self.tail = head
        if head is not None:
            size += 1

    def sort(self):
        """
        Sort PhoneBook using TODO: DEFINE SORTING METHOD

        Args:
            None
        
        Returns:
            None
        """
        return NotImplementedError

    def push(self, node: Node, update_tail: bool = False):
        """
        Add an element before the PhoneBook's head

        Args:
            node: `Node` to be added
            update_tail: whether to set the new tail as the old head
        
        Returns:
            None
        """
        node.next = self.head
        self.head.previous = node
        self.head = node
        if update_tail:
            self.tail = self.head

    def append(self, node: Node):
        """
        Add a new element to the PhoneBook's end

        Args:
            node: `Node` to be added
        
        Returns:
            None
        """
        self.tail.next = node
        node.previous = self.tail
        self.tail = node

    def add(self, contacts: List[Contact] or Contact):
        """
        Adds new contacts in the phone book respecting alphabetic order

        Args:
            contacts: List of `Contact` or a single `Contact` object
        
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
            while (curr.next is not None) and (curr.next.contact.name < node.contact.name):
                curr = curr.next
            
            if curr == self.head:
                self.push(node=node, update_tail=True)
            elif curr.next is None:
                self.append(node=node)
            else:
                curr.previous.next = node
                node.previous = curr.previous
                curr.previous = node
                node.next = curr
            self.length += 1

    def print(self):
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
        print('----- DEBUGGING -----')
        print(f'LIST\'S HEAD: {self.head.contact.name}\nLIST\'S TAIL: {self.tail.contact.name}\nLIST\'S SIZE: {self.length}')

        curr = self.head
        while curr is not None:
            print('-'*30)
            if curr.previous is not None:
                previous_name = curr.previous.contact.name
            else:
                previous_name = 'None'

            if curr.next is not None:
                next_name = curr.next.contact.name
            else:
                next_name = 'None'
            print(f'Previous: {previous_name}\nSelf: {curr.contact.name}\nNext: {next_name}')
            curr = curr.next

# Debugging
if __name__ == '__main__':
    pb = PhoneBook()
    contacts = []
    for name in ('ademar', 'bruno', 'cabral', 'daniel', 'erick', 'fabiana', 'gabriel', 'heitor'):
        contacts.append(Contact(name=name, email='foo.bar@example.com', phone_number='00 1234 5678'))
    pb.add(contacts=contacts[::-1])
    pb.print()
    print()
    pb.print_debug()