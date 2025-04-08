from classes import AddressBook, Record
import pickle

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено

#! в мене вже була реалізація готова до того як ми познайомились з pickle. Залишу тут для наглядності наскільки простіше з pickle

# CONTACTS_FILE = "contact_book.txt"

# def load_contacts():
#     book = AddressBook()
#     try:
#         with open(CONTACTS_FILE, "r", encoding="utf-8") as file:
#             for line in file:
#                 parts = line.strip().split("|")
#                 name = parts[0]
#                 phones = parts[1].split(";") if parts[1] else []
#                 birthday = parts[2] if len(parts) > 2 and parts[2] else None

#                 record = Record(name)
#                 for phone in phones:
#                     record.add_phone(phone)

#                 if birthday:
#                     record.add_birthday(birthday)

#                 book.add_record(record)
#     except FileNotFoundError:
#         pass
#     return book

# def save_contacts(book: AddressBook):
#     with open(CONTACTS_FILE, "w", encoding="utf-8") as file:
#         for record in book.data.values():
#             phones_str = ";".join([phone.value for phone in record.phones])
#             birthday_str = record.birthday.value.strftime("%d.%m.%Y") if record.birthday else ""
#             file.write(f"{record.name.value}|{phones_str}|{birthday_str}\n")