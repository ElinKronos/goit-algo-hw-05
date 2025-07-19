# Here begins a new world...

# Ця програма створює невеличкий CLI застосунок для збереження імен користувачів та їхніх телефонних номерів

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

# Функція створення декоратора
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Name not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the right command."
    return inner

# Парсер команд
def parse_input(user_input):
    if not user_input.strip():
        return "", []
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args

# Додавання контакту
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Зміна контакту
@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."
    
# Виводить номер телефону вибраного користувача
@input_error
def show_phone(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"
    
# Виводить усі збережені контакти
@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

if __name__ == "__main__":
    main()
