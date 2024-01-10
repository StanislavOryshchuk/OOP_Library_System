'''
Варіант 12

Приклади використання методів, яких немає тут пристутні у файлі Oryshchuk_UI_OOP_LibrarySystem.py
'''

# декоратор, що перевіряє рік видання на реалістичність


def validate_year_published(func):
    def validate(self, title, author, ISBN, year_published):
        current_year = 2024  # Поточний рік
        year_published = int(year_published)
        if year_published > current_year or year_published < 0:
            return None, ValueError("Невірний рік видання книги")  # можна встановити логічну межу років минулого,
                                                                   # щоб книга не була дуже давньою
        else:
            return func(self, title, author, ISBN, year_published)
    return validate
# за подібною аналогією тут можна було б додати, наприклад, валідацію номера ISBN


class Book:
    @validate_year_published  # використання декоратора валідації
    def __init__(self, title, author, ISBN, year_published):
        self.title = str(title)
        self.author = str(author)
        self.ISBN = str(ISBN)
        self.year_published = str(year_published)

    # виведення інформації про книгу
    def __str__(self):
        info = {'Назва': self.title,
                'Автор': self.author,
                'ISBN': self.ISBN,
                'Рік видання': self.year_published}
        return info

    # метод для виведення інформації про книгу в більш зручному вигляді (по рядках), спеціально для print'ів

    def __print__(self):
        print('Назва:  ', example_1_book.__str__()['Назва'], end='\n')
        print('Автор:  ', example_1_book.__str__()['Автор'], end='\n')
        print('ISBN:  ', example_1_book.__str__()['ISBN'], end='\n')
        print('Рік видання:  ', example_1_book.__str__()['Рік видання'], end='\n')

    # порівння книг за ISBN(перевірка рівності)
    def __check_equality__(self, other):
        return self.ISBN == other.ISBN


example_1_book = Book("Кобзар", "Тарас Шевченко", "9793161584200", 2018)
example_2_book = Book("Молоко і мед", "Рупі Куар", "9793-16-1584200", 2020)
example_3_book = Book("Мистецтво стратегії", "Ігор Гринів", "8783271684200", 2022)
# Приклад невалідної книги (з майбутнього) bad_book = Book("Стів Джобс", "Волтер Айзексон",  "8784671684200", 2056)

print("___________BOOK___________")
print(example_1_book.__str__())  # використання методу __str__

print("________________________________")  # тут, і далі подбіні рядки, служать розділювачами
print("________________________________")  # для покращення сприйняття результатів роботи коду (перепрошую за них)

example_2_book.__print__()  # використання методу __print__

print("________________________________")
print("________________________________")


print("використання ____check_equality__")
print(example_1_book.__str__(), "==", example_2_book.__str__())
print(example_1_book.__check_equality__(example_2_book))  # використання ____check_equality__

print(example_1_book.__str__(), "==", example_3_book.__str__())
print(example_1_book.__check_equality__(example_3_book))

print("_________________><_________________")

''' 
клас програм для читанння, 
необіхдний для перевірки сумісності форматів 
'''


class ReaderApp:
    def __init__(self, reader_name, suported_formats):
        self.reader_name = str(reader_name)
        self.suported_formats = suported_formats


example_reader = ReaderApp('Ex_reader', ['pdf', 'doc', 'epb'])
pdf_reader = ReaderApp('Ex_reader', ['pdf'])
text_reader = ReaderApp('Ex_reader', ['doc', 'txt', 'docx'])


class DigitalBook(Book):
    def __init__(self, title, author, ISBN, year_published, file_format):
        super().__init__(title, author, ISBN, year_published)
        self.file_format = file_format

    def __str__(self):
        dg_info = {'Назва': self.title,
                'Автор': self.author,
                'ISBN': self.ISBN,
                'Рік видання': self.year_published,
                'Формат': self.file_format}
        return dg_info

    ''' перевірка чи сумісний формат файлу з певною програмамою для читання '''

    def __check_suporting_in__(self, reader):
        suported_formats = reader.suported_formats
        if self.file_format in suported_formats:
            return "Сумісний"
        else:
            return "Не сумісний"


ex1_dg_book = DigitalBook("Часу немає", "Рустем Халіл", "978-3-16-148410-0", 2023, "pdf")
# приклад цифрової книги
ex2_dg_book = DigitalBook("Мистецтво програмуванння", "Дональд Кнут", "978-3-16-148410-0", 2023, "fb2")

print("___________Digital_book___________")
print("___________str___________")
print(ex1_dg_book.__str__())  # використання методу __str__ класу Book для виведення DigitalBook

# для демонстрації наслідування
# використання Book.__check_equality__ для порівняння цифрових книг за ISBN
print("___________check_equality___________")
print(ex1_dg_book.__str__(), "==", ex2_dg_book.__str__())
print(ex1_dg_book.__check_equality__(ex2_dg_book))


print(f"Формат {ex1_dg_book.title, ex1_dg_book.author} з  програмою {example_reader.reader_name}")
print(ex1_dg_book.__check_suporting_in__(example_reader))  # використання __check_suporting_in__

print(f"Формат {ex2_dg_book.title, ex2_dg_book.author} з  програмою {pdf_reader.reader_name}")
print(ex2_dg_book.__check_suporting_in__(pdf_reader))


class LibrarySystem:

    def __init__(self):
        self.books = []

    def __iter__(self):
        self.index = 0
        return self

    # ітератор
    def __next__(self):
        if self.index in range(len(self.books)):
            current_book = self.books[self.index]
            self.index += 1
            return current_book
        else:
            raise StopIteration

    # вивидення книг
    def __print_books__(self):
        printed_books = []
        for i in range(len(self.books)):
            printed_books.append([i+1, self.books[i]])
        return printed_books

    # додавання книги
    def __add_book__(self, book):
        added_book = book.__str__()
        self.books.append(added_book)

    # пошук за назвою і ISBN (для зручності можна додати перевірку за іншими параметрами,
    # для ефективності - навпаки залишити лише унікальний ISBN)
    def __search_book__(self, book):
        for ii in range(len(self.books)):
            if self.books[ii]['Назва'] == book.title or self.books[ii]['ISBN'] == book.ISBN:
                search_result = [ii+1, self.books[ii]]
                return search_result
            else:
                return "не знайдено"

    # видалення книги
    def __delate_book__(self, book):
        deleted_index = int(self.__search_book__(book)[0]) - 1
        self.books.pop(deleted_index)


MY_LIBRARY = LibrarySystem()  # створення бібліотеки
MY_LIBRARY.__add_book__(example_1_book)  # додання книг в бібліотеку
MY_LIBRARY.__add_book__(example_2_book)
MY_LIBRARY.__add_book__(example_3_book)

MY_LIBRARY.__add_book__(ex1_dg_book)  # додання цифрової книги в бібліотеку

print("___________Бібліотека___________")

# використанння методу __print_books__ для виведення книг
print(MY_LIBRARY.__print_books__())

# приклад роботи ітератора в LibrarySystem
print("__________iter_________")
for book in MY_LIBRARY:
    print(book)


# Використання методів додавання, видалення і пошуку (наочно) реалізовано в ui частині
# (Oryshchuk_UI_OOP_LibrarySystem)




