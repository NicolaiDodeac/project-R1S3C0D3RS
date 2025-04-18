from collections import UserDict
from datetime import datetime, timedelta
from .validation import is_valid_email


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value) if self.value else "No value"


class Name(Field):
    def __init__(self, value):
        super().__init__(value.lower())


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain 10 digits")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            bday = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(bday)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, value):
        self.birthday = Birthday(value)

    def add_email(self, email):
        if not is_valid_email(email):
            raise ValueError("❌ Некоректний email e.g. name1@mail.ua")
        self.email = email

    def edit_phone(self, old, new):
        for i, p in enumerate(self.phones):
            if p.value == old:
                self.phones[i] = Phone(new)
                return True
        return False

    def remove_phone(self, phone):
        for p in self.phones[:]:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError("Phone number not found")

    def remove_birthday(self):
        self.birthday = None

    def remove_email(self):
        self.email = None

    def find_phone(self, number):
        return next((p for p in self.phones if p.value == number), None)

    def __str__(self):
        bday = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{bday}, email: {self.email}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self, days=7):
        today = datetime.today().date()
        upcoming = []

        for record in self.data.values():
            if record.birthday:
                original_birthday = record.birthday.value
                bday_this_year = original_birthday.replace(year=today.year)

                if bday_this_year < today:
                    bday_this_year = bday_this_year.replace(year=today.year + 1)

                if 0 <= (bday_this_year - today).days <= days:

                    if bday_this_year.weekday() >= 5:
                        bday_this_year += timedelta(days=(7 - bday_this_year.weekday()))

                    upcoming.append({
                        "name": record.name.value,
                        "congratulation_date": bday_this_year.strftime("%d.%m.%Y"),
                        "original_birthday": original_birthday
                    })

        return upcoming
