from typing import List

class Contact:
    def __init__(self, name: str, phone_number: str = 'Empty',
                 email: str = 'Empty'):
        self.name = name
        self.phone_number = phone_number
        self.email = email
    
class Node:
    def __init__(self, contact: Contact, previous: 'Node' = None, next: 'Node' = None):
        self.previous = previous
        self.contact = contact
        self.next = next

class PhoneBook:

    size = 0

    def __init__(self, head=None):
        self.head = head
        if head is not None:
            size += 1

    def add(self, contacts: List[Contact]):

        if not isinstance(contacts, list):
            contacts = [contacts]

        if self.head is None:
            self.head = Node(contact=contacts.pop(0))

        if contacts:
            curr = self.head
            while curr.next is not None:
                curr = curr.next

            while contacts:
                node = Node(contact=contacts.pop(0))
                node.previous = curr
                curr.next = node
                curr = curr.next
    
    def print(self):
        curr = self.head
        while curr is not None:
            name, email, phone_number = curr.contact.name, \
                                        curr.contact.email, \
                                        curr.contact.phone_number
            print('-'*30)
            print(f'Name: {name}\nEmail: {email}\nPhone Number: {phone_number}')
            curr = curr.next
    
    def print_nodes(self):
        print('----- DEBUGGING -----')
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
    c1 = Contact(name='Joao', email='foo.bar@example.com', phone_number='00 1234 5678')
    c2 = Contact(name='Lucas', email='bar.baz@example.com', phone_number='00 1234 5678')
    c3 = Contact(name='Mateus', email='baz.foo@example.com', phone_number='00 1234 5678')
    pb.add([c1, c2, c3, c1, c2, c3])
    pb.print()
    print()
    pb.print_nodes()