documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_person():
    doc_number = input("Введите номер документа: ")
    for doc in documents:
        if doc['number'] == doc_number:
            return doc['name']
    return "Документ не найден"


def get_shelf():
    doc_number = input("Введите номер документа: ")
    for shelf, docs in directories.items():
        if doc_number in docs:
            return shelf
    return "Документ не найден на полках"


def display_documents():
    for doc in documents:
        print(f"{doc['type']} \"{doc['number']}\" \"{doc['name']}\"")


def add_document():
    doc_number = input("Введите номер документа: ")
    doc_type = input("Введите тип документа: ")
    doc_name = input("Введите имя владельца: ")
    shelf_number = input("Введите номер полки: ")

    if shelf_number not in directories.keys():
        return "Такой полки не существует"

    documents.append({"type": doc_type, "number": doc_number, "name": doc_name})
    directories[shelf_number].append(doc_number)
    return "Документ успешно добавлен"


# Пример использования пользовательских команд
command = input("Введите команду (p, s, l, a): ")
if command == "p":
    print(get_person())
elif command == "s":
    print(get_shelf())
elif command == "l":
    display_documents()
elif command == "a":
    print(add_document())
else:
    print("Некорректная команда")
