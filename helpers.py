def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Помилка: Невірне значення.якщо телефон то 10цифр а як дата то у форматі ДД.ММ.РРРР"
        except KeyError:
            return "Помилка: Ключ не знайдено."
        except IndexError:
            return "Помилка: Неправильна кількість аргументів."
        except Exception as e:
            return f"Невідома помилка: {str(e)}"
    return wrapper