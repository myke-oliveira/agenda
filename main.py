#! /usr/bin/python3

from os import system, name as os_name
from time import sleep

def show_menu():
    clear_screen()
    print('='*30)
    print(f"{' Menu Principal ':=^30}")
    print('='*30)
    print("1. Salvar novo contato")
    print("2. Editar contato")
    print("3. Deletar contato")
    print("4. Marcar contato como favorito")
    print("5. Mostrar todos os contatos")
    print("6. Mostrar contatos favoritos")
    print("7. Sair")
    print()

    option = input("Digite a opcao desejada: ")
    print()

    return option

def save_new_contact(contacts, name, telephone, email):
    new_contact = {
        "name": name,
        "telephone": telephone,
        "email": email,
        "favorite": False
    }

    contacts.append(new_contact)
    return

def edit_contact(contacts, index, name, telephone, email):
    try:
        contact = contacts[index]
    except IndexError:
        raise ContactNotFound()
    contact['name'] = name
    contact['telephone'] = telephone
    contact['email'] = email
    return

def delete_contact(contacts, index):
    try:
        del contacts[index]
    except IndexError:
        raise ContactNotFound()
    return

def mark_contact_as_favorite(contacts, index):
    try:
        contacts[index]['favorite'] = True
    except IndexError:
        raise ContactNotFound()
    return

def show_contacts(contacts):
    if len(contacts) == 0:
        print("Nenhum contato para apresentar!!")

    for index, contact in enumerate(contacts, start=1):
        favorite_mark = '✓' if contact['favorite'] else '✕'
        print(f"Contato #{index}")
        print()
        print(f"Nome: {contact['name']}")
        print(f"Telefone: {contact['name']}")
        print(f"E-mail: {contact['name']}")
        print(f"Favorito: {favorite_mark}")
        print()

def show_favorite_contacts(contacts):
    if len(contacts) == 0:
        print("Nenhum contato para apresentar!!")

    for index, contact in enumerate(contacts, start=1):
        if (not contact['favorite']):
            continue

        favorite_mark = '✓' if contact['favorite'] else '✕'
        print(f"Contato #{index}")
        print()
        print(f"Nome: {contact['name']}")
        print(f"Telefone: {contact['name']}")
        print(f"E-mail: {contact['name']}")
        print(f"Favorito: {favorite_mark}")
        print()

class ContactNotFound(Exception):
    pass

def clear_screen():
    system('cls' if os_name == 'nt' else 'clear')


def main():
    contacts = []
    while True:
        option = show_menu()

        if option == '1':
            print("Entre com as informações do novo contato.")
            name = input("Nome: ")
            telephone = input("Telefone: ")
            email = input("E-mail: ")

            save_new_contact(contacts, name, telephone, email)
            print(f"Contato {name} salvo com sucesso!!")
            sleep(2)

        elif option == '2':
            index = int(input("Entre o índice do contato que deseja alterar: "))
            print("Entre com as informações do novo contato.")
            name = input("Nome: ")
            telephone = input("Telefone: ")
            email = input("E-mail: ")

            try:
                edit_contact(contacts, index - 1, name, telephone, email)
            except ContactNotFound:
                print(f"Contato de índice {index} não foi encontrado.")
            else:
                print(f"Contato {name} alterado com sucesso!!")
            finally:
                sleep(2)

        elif option == '3':
            index = int(input("Entre o índice do contato que deseja deletar: "))

            try:
                delete_contact(contacts, index - 1)
            except ContactNotFound:
                print(f"Contato de índice {index} não foi encontrado.")
            else:
                print(f"Contato de índice {index} foi deletado!!")
            finally:
                sleep(2)

        elif option == '4':
            index = int(input("Entre o índice do contato que deseja marcar como favorito: "))
            
            try:
                mark_contact_as_favorite(contacts, index - 1)
            except ContactNotFound:
                print(f"Contato de índice {index} não foi encontrado.")
            else:
                print(f"Contato de índice {index} foi marcado como favorito!!")
            finally:
                sleep(2)

        elif option == '5':
            show_contacts(contacts)
            input("Pressione [Enter] para continuar.")

        elif option == '6':
            show_favorite_contacts(contacts)
            input("Pressione [Enter] para continuar.")

        elif option == '7':
            # Sair
            return
        else:
            print("Opção inválida")
            sleep(2)

if __name__ == "__main__":
    main()
