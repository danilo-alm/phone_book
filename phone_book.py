
class Contact:
    def __init__(self, name, phone_number='Empty', email='Empty'):
        self.name = name
        self.phone_number = phone_number
        self.email = email
    
class Node:
    def __init__(self, previous: 'Node', contact: Contact, next: 'Node'):
        self.previous = previous
        self.contact = contact
        self.next = next
