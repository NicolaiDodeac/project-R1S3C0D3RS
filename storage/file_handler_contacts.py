import os
import sys
import pickle
from contacts.models import AddressBook

# Визначення шляху для зберігання даних
if getattr(sys, 'frozen', False):  # Запущено як .exe
    BASE_DIR = os.path.dirname(sys.executable)
else:  # Запущено як .py
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STORAGE_DIR = os.path.join(BASE_DIR, "storage", "data")
FILENAME = os.path.join(STORAGE_DIR, "addressbook.pkl")


def ensure_storage_dir():
    try:
        os.makedirs(STORAGE_DIR, exist_ok=True)
    except Exception as e:
        print(f"[ERROR] Не вдалося створити директорію для збереження: {e}")


def save_data(book, filename=FILENAME):
    ensure_storage_dir()
    try:
        with open(filename, "wb") as f:
            pickle.dump(book, f)
    except Exception as e:
        print(f"[ERROR] Не вдалося зберегти дані: {e}")


def load_data(filename=FILENAME):
    ensure_storage_dir()
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
    except Exception as e:
        print(f"[ERROR] Не вдалося завантажити дані: {e}")
        return AddressBook()
