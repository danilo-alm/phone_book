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
        return NotImplementedError

    def add(self, contacts: List[Contact]):

        if not isinstance(contacts, list):
            contacts = [contacts]

        if self.head is None:
            self.head = self.tail = Node(contact=contacts.pop(0))
            self.length += 1

        if not contacts:
            return

        while contacts:
            node = Node(contact=contacts.pop(0))

            curr = self.head
            while (curr.next is not None) and (curr.next.contact.name < node.contact.name):
                curr = curr.next
            
            if curr.next is None:
                # If `curr` is `self.head`
                if curr.previous is None:
                    if curr.contact.name > node.contact.name:
                        node.next = curr
                        curr.previous = node
                        self.head = node
                        self.tail = curr
                    else:
                        node.previous = curr
                        curr.next = node
                        self.tail = node
                else:
                    # If `curr` is `self.tail`
                    node.previous = curr
                    curr.next = node
                    self.tail = node
            else:
                # Add before
                if curr == self.head:
                    node.next = curr
                    curr.previous = node
                    self.head = node
                    self.tail = curr
                else:
                    curr.previous.next = node
                    node.previous = curr.previous
                    curr.previous = node
                    node.next = curr
            self.length += 1

    def print(self):
        curr = self.head
        while curr is not None:
            name, email, phone_number = curr.contact.name, \
                                        curr.contact.email, \
                                        curr.contact.phone_number
            print('-'*30)
            print(f'Name: {name}\nEmail: {email}\nPhone Number: {phone_number}')
            curr = curr.next
    
    def print_debug(self):
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