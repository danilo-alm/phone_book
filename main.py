from phone_book import PhoneBook, Contact
import os

def main():
    pb = load_phonebook()
    
    options = ('Add a new contact',
               'Delete a contact',
               'Search for a contact',
               'See all contacts',
               'Delete ALL contacts',
               'Exit')

    while True:
        print('\n' + '-'*40)

        for index, option in enumerate(options):
            print(f'{index + 1}. {option}')

        try:
            chosen = int(input(f'Choose an option (1-{len(options)}): '))
        except ValueError:
            print('Invalid option.')
            continue

        if not 0 < chosen < len(options):
            continue

        match chosen:

            case 1:  # Add
                name = input('Name: ')
                email = input('Email: ')
                phone_number = input('Phone Number: ')
                pb.add(contacts=[Contact(name=name, email=email, phone_number=phone_number)])
                pb.save_to_file(FILENAME)

            case 2:  # Delete
                return NotImplementedError
                pb.delete()

            case 3:  # Search
                return NotImplementedError
                pb.search()

            case 4:  # Print
                pb.print_contacts()

            case 5:  # Delete ALL
                check = input('THIS WILL DELETE ALL THE CONTACTS. TYPE "I\'M SURE" IF YOU\'RE SURE: ')
                if check == 'I\'M SURE':
                    pb = PhoneBook()
                    pb.save_to_file(FILENAME)

            case 'Exit':
                exit()

def load_phonebook():
    if os.path.exists(FILENAME):
        return PhoneBook.load_from_file(filename=FILENAME)
    else:
        return PhoneBook()


FILENAME = 'phonebook.pkl'

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
