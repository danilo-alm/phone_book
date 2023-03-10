from phone_book import PhoneBook
import os
from time import sleep

def main():
    pb = load_phonebook()

    options = ('Add a new contact',
               'See all contacts',
               'Search for a contact',
               'Delete a contact',
               'Delete ALL contacts',
               'Clear screen',
               'Exit')

    while True:
        print('- '*30)
        for index, option in enumerate(options):
            print(f'{index + 1}. {option}')

        try:
            chosen = int(input(f'Choose an option (1-{len(options)}): '))
        except ValueError:
            print('Invalid option.')
            sleep(.5)
            continue

        if not 0 < chosen <= len(options):
            continue

        match chosen:

            case 1:  # Add
                pb.add(interactive=True)
                pb.save_to_file(FILENAME)

            case 2:  # Print
                pb.print_contacts()

            case 3:  # Search
                pb.search(interactive=True)

            case 4:  # Delete
                index = input('What index do you want to delete? ')
                try:
                    pb.delete(int(index))
                except IndexError:
                    print('Index doesn\'t exist')
                except ValueError:
                    print('Not a number')

            case 5:  # Delete ALL
                check = input('THIS WILL DELETE ALL THE CONTACTS. TYPE "I\'M SURE" IF YOU\'RE SURE: ')
                if check == 'I\'M SURE':
                    pb = PhoneBook()
                    pb.save_to_file(FILENAME)

            case 6:
                os.system('cls||clear')

            case 7:
                exit()
        
        if chosen not in (2, 3):
            os.system('cls||clear')

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
