# project-R1S3C0D3RS

# Структура проєкту:

# main.py — головна точка входу до додатку

# contacts/models.py — класи Contact, AddressBook та валідація полів

# notes/models.py — класи Note, NoteBook, логіка тегів

# processing/commands.py — логіка обробки команд користувача

# helpers/decorators.py — декоратори для обробки помилок

# storage/file_handler.py — логіка збереження/завантаження з файлу

# Створюємо каркас структури у файлах:

# main.py

"""
Запускає програму, обробляє введення користувача
"""

# contacts/models.py

"""
Класи:

- Field, Name, Phone, Birthday
- Record (контакт з полями)
- AddressBook (словник контактів)

* валідація телефонів, імейлів
  """

# notes/models.py

"""
Класи:

- Note (текст, дата створення, теги)
- NoteBook (словник нотаток)

* логіка пошуку за тегами
  """

# processing/commands.py

"""
Команди користувача:

- add, change, delete
- search, show_all, help
- обробка команд
  """

# helpers/decorators.py

"""
Декоратор @input_error для обробки ValueError, IndexError, KeyError
"""

# storage/file_handler.py

"""
Збереження та завантаження:

- save_contacts
- load_contacts
- save_notes
- load_notes
  """

# tests/ (необов'язково, але бажано)

# test_contacts.py

# test_notes.py

# README.md

"""
Інструкція:

- Як запускати
- Які команди є
- Як зберігаються дані
  """

# .gitignore

**pycache**/
_.pyc
_.pkl
\*.json

# requirements.txt (якщо буде використання бібліотек)
