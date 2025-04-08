def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "❌ Невірне значення (телефон — 10 цифр, дата — ДД.ММ.РРРР)"
        except IndexError:
            return "❌ Неправильна кількість аргументів"
        except KeyError:
            return "❌ Ключ не знайдено"
        except Exception as e:
            return f"❌ Невідома помилка: {e}"
    return wrapper
