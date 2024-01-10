'''
В цьому файлі наведений приклад візувального використання LibrarySystem, окрім чаcтини з DigitalBook.
Виведення даних не дуже user friendly, але все таки дає змогу краще побачити реалізацію класів і методів
'''

from Oryshchuk_OOP_LibrarySystem import Book, LibrarySystem
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

ctk.set_appearance_mode("dark")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("950x850")
        self.title("Бібліотека")


app = App()

ex_book = Book("48 законів влади", "Роберт Грін", "9793161584200", 2004)

book_entry = ctk.CTkEntry(master=app, width=450, height=40)
book_entry.grid(row=1, column=0, padx=10, pady=10)


def show_book():
    book_entry.delete(0, 'end')
    info = ex_book.__str__()
    book_entry.insert(0, str(info))
    #book_isbn = info.split('ISBN')[1]


show_btn = ctk.CTkButton(master=app, text="Показати приклад книги", command=show_book)
show_btn.grid(row=2, column=0, padx=10, pady=10)


label_title = ctk.CTkLabel(app, text="Назва", fg_color="transparent")
label_title.grid(row=2, column=1, pady=10)
entry_title = ctk.CTkEntry(master=app, width=140, height=40)
entry_title.grid(row=2, column=2, pady=10)

label_author = ctk.CTkLabel(app, text="Автор", fg_color="transparent")
label_author.grid(row=3, column=1, pady=10)
entry_author = ctk.CTkEntry(master=app, width=140, height=40)
entry_author.grid(row=3, column=2, padx=10, pady=10)

label_ISBN = ctk.CTkLabel(app, text="ISBN", fg_color="transparent")
label_ISBN.grid(row=4, column=1, pady=10)
entry_ISBN = ctk.CTkEntry(master=app, width=140, height=40)
entry_ISBN.grid(row=4, column=2, padx=10, pady=10)

label_year_published = ctk.CTkLabel(app, text="Рік публікації", fg_color="transparent")
label_year_published.grid(row=5, column=1, pady=10)
entry_year_published = ctk.CTkEntry(master=app, width=140, height=40)
entry_year_published.grid(row=5, column=2, padx=10, pady=10)


MY_LIBRARY = LibrarySystem()


def add_book():
    try:
        if len(entry_title.get()) > 1:
            a_title = entry_title.get()
        if len(entry_author.get()) > 1:
            a_author = entry_author.get()
        if len(entry_ISBN.get()) > 1:
            a_ISBN = entry_ISBN.get()
        if len(entry_year_published.get()) > 1:
            a_year_published = entry_year_published.get()
            added_book = Book(a_title, a_author, a_ISBN, a_year_published)
            MY_LIBRARY.__add_book__(added_book)
    except Exception:
        CTkMessagebox(master=app, title="Невалідні дані",
                      message="Введіть коректний рік видання", icon="info")

    ''' https://prnt.sc/JGenGvtcug2t '''


add_btn = ctk.CTkButton(master=app, text="Додати книгу в бібліотеку", command=add_book)
add_btn.grid(row=6, column=2, padx=10, pady=10)

library_entry = ctk.CTkEntry(master=app, width=500, height=60)
library_entry.grid(row=6, column=0, padx=10, pady=10)

''' 
приклад реалізації інтерфейсу для додавання цифроої книги:
 - Кнопка dg_book_btn, яка виводить на екран ще одне поле(для введення формату), а також 
 кнопку add_dg_book_btn, що в свою чергу викликає відповідну функцію додавання цифрової книги.'''

'''можлива інтерфейсна реалізація __check_suporting_in__:
  (інтерфейс, який з'являється в меню DigitalBook, що з'являється після кліку по dg_book_btn)
- список check-boxs, що відповіадють екземплярам класу програм для читання 
 - кнопка check_suporting_in_btn, що уже викликає цей метод
- поле виводу результату перевірки entry_check_suporting_in 
 '''


# показати бібліотеку
def show_library():
    library_entry.delete(0, 'end')
    info = MY_LIBRARY.__print_books__()
    library_entry.insert(0, str(info))  # можна було б виводити в більш кращому форматі


show_lib_btn = ctk.CTkButton(master=app, text="Показати бібліотеку", command=show_library)
show_lib_btn.grid(row=7, column=0, padx=10, pady=10)


def delete_book():
    deleted_book = Book(entry_title.get(),
                        entry_title.get(),
                        entry_ISBN.get(),
                        entry_year_published.get())
    MY_LIBRARY.__delate_book__(deleted_book)


delete_book_btn = ctk.CTkButton(master=app, text="Видалити книгу", command=delete_book)
delete_book_btn.grid(row=4, column=3, padx=10, pady=10)

search_result_entry = ctk.CTkEntry(master=app, width=200, height=40)
search_result_entry.grid(row=5, column=4, padx=10, pady=10)


def search_book():
    search_result_entry.delete(0, 'end')
    s_title = entry_title.get()
    s_author = entry_author.get()
    s_ISBN = entry_ISBN.get()
    s_year_published = entry_year_published.get()
    searched_book = Book(s_title, s_author, s_ISBN, s_year_published)
    search_result = MY_LIBRARY.__search_book__(searched_book)
    search_result_entry.insert(0, str(search_result))


search_book_btn = ctk.CTkButton(master=app, text="Шукати книгу", command=search_book)
search_book_btn.grid(row=5, column=3, padx=10, pady=10)


app.mainloop()
