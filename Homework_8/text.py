main_menu = '''/nГлавное меню:
        1. Открыть файл
        2. Записать файл
        3. Показать контакт
        4. Добавить контакт
        5. Найти контакт
        6. Изменить контакт
        7. Удалить контакт
        8. Выход/n'''

input_choice = 'Выберите пункт меню: '

load_successful = 'Телефонная книга успешно открыта'

load_error = 'Телефонная книга пуста или не открыта'

input_contact = {'name':'Введите имя: ',
                 'phone':'Введите телефон: ',
                 'comment':'Ведите комментарий: '}

new_contact = 'Введите данные нового контакта (пустое поле для отмены): '

def new_contact_successful(name: str) -> str:
    return f'Контакт {name} успешно добавлен'

cancel_input = 'Отмена ввода'

