from phone_book import PhoneBook, Contact
import os

def main():
    if os.path.exists(FILENAME):
        try:
            pb = PhoneBook.load_from_file(filename=FILENAME)
        except EOFError:
            pb = PhoneBook()
    else:
        pb = PhoneBook()
    
    options = (
        'Add a new contact',
        'Delete a contact',
        'Search for a contact',
        'See all contacts',
        'Delete ALL contacts',
        'Exit'
    )

    while True:
        print('\n' + '-'*40)

        for index, opt in enumerate(options):
            print(f'{index + 1}. {opt}')

        try:
            chosen = int(input(f'Choose an option (1-{len(options)}): '))
        except ValueError:
            continue

        if not 0 < chosen < len(options):
            continue

        chosen = options[chosen - 1]

        match chosen:

            case 'Add a new contact':
                name = input('Name: ')
                email = input('Email: ')
                phone_number = input('Phone Number: ')
                pb.add(contacts=[Contact(name=name, email=email, phone_number=phone_number)])
                pb.save_to_file(FILENAME)

            case 'Delete a contact':
                return NotImplementedError
                pb.delete()

            case 'Search for a contact':
                return NotImplementedError
                pb.search()

            case 'See all contacts':
                pb.print_contacts()

            case 'Delete ALL contacts':
                check = input('THIS WILL DELETE ALL THE CONTACTS. TYPE "I\'M SURE" IF YOU\'RE SURE: ')
                if check == 'I\'M SURE':
                    pb = PhoneBook()
                    pb.save_to_file(FILENAME)

            case 'Exit':
                exit()

FILENAME = 'phonebook.pkl'

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
