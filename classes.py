from collections import UserDict 
from datetime import datetime, timedelta

class Field:
    def __init__(self, value): 
        self.value = value

    def __str__(self): 
        if not self.value: 
            return "No value"
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value.lower())

class Phone(Field):
        def __init__(self, value):
            if not value.isdigit() or len(value) != 10: 
                raise ValueError ("Phone number must contain 10 digits")
            super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            birthday_day = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(birthday_day)

            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name): 
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def add_birthday(self, value):
       self.birthday = Birthday(value)
          
         
    def remove_phone(self, phone_number):
        self.phones = [phone for phone in self.phones if phone.value != phone_number]

    def edit_phone(self, old_phone, new_phone): 
        for i, phone in enumerate(self.phones): # перебираємо телефони в запису і визначаємо їх позицію
            if phone.value == old_phone: # якщо знайшли телефон, який потрібно змінити
                self.phones[i] = Phone(new_phone) # Замінюємо старий телефон на новий на тій самій позиції та з валідацією
                return True # повертаємо True, якщо зміна пройшла успішно
        return False # повертаємо False, якщо телефон не знайдено

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None
              
    def __str__(self):
        bday_str = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{bday_str}"

        # return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


    def find(self, name):
        return self.data.get(name)
    
    def get_upcoming_birthdays(self):
        today_date = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday is None:
                continue
            
            b_day = record.birthday.value
            birthday_this_year = b_day.replace(year=today_date.year)
            
            if birthday_this_year < today_date:
                birthday_this_year = birthday_this_year.replace(year=today_date.year + 1)

            if 0 <= (birthday_this_year - today_date).days <= 7:
                if birthday_this_year.weekday() in [5,6]:
                    birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
                upcoming_birthdays.append({
                    "name":  record.name.value,
                    "congratulation_date": birthday_this_year.strftime("%d.%m.%Y")
                })
        return upcoming_birthdays
          

    def delete(self, name):
        if name in self.data:
            del self.data[name]


# Створення нової адресної книги
# book = AddressBook()
# print(book)

    # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")

#     # Додавання запису John до адресної книги
# book.add_record(john_record)

#     # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# jane_record.add_birthday("29.12.1977")
# book.add_record(jane_record)

# print(jane_record.birthday)

# #     # Виведення всіх записів у книзі
# # for name, record in book.data.items():
# #     print(record)

#     # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

#     # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
# book.delete("Jane")
# for name, record, birthday in book.data.items():
#     print(record)