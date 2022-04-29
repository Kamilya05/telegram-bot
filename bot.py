import logging
from math import *
from telegram.ext import MessageHandler, Filters, ConversationHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove, Update
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.ext import InlineQueryHandler, CallbackContext
from telegram.utils.helpers import escape_markdown
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
TOKEN = '5345895427:AAG1bO9iRxMp-HVm0PQO3ZC3PJQ8ygb3C4I'


def start(update, _):
    update.message.reply_text(
        "Я бот-справочник. Какая информация вам нужна?",
        reply_markup=menu_markup()
    )
    return MENU


def help_(update, _):
    update.message.reply_text('''Бот для решения задач по алгебре/геометрии.
Есть калькулятор и таблицы по математическим/тригонометрическим операциям.

/start - начать 
/exit - завершить работу

По всем вопросам к @Duchess_Hrushess''')
    return MENU


def menu_markup():
    reply_keyboard = [
                      ['Таблицы'],
                      ['Калькулятор'],
                      ['Геометрия'],
                      ['Тригонометрия'],
                      ['/exit']
    ]

    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    return markup


def tables(update, _):
    keyboard = [
            [InlineKeyboardButton("Таблица степеней", callback_data='sq')],
            [InlineKeyboardButton("Таблица квадратов", callback_data='sq2')],
            [InlineKeyboardButton("Таблица кубов", callback_data='sq3')],
            [InlineKeyboardButton("Таблица натуральных логарифмов", callback_data='ln')],
            [InlineKeyboardButton("Таблица десятичных логарифмов", callback_data='lg')],
            [InlineKeyboardButton("Таблица логарифмов по основанию а", callback_data='log')],
            [InlineKeyboardButton("Таблица Брадиса", callback_data='brad')],
            [InlineKeyboardButton("sin, cos", callback_data='brad1'),
             InlineKeyboardButton("tg, ctg", callback_data='brad2')]
        ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Таблицы:', reply_markup=reply_markup)
    return MENU


def tables_answer(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'sq':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='''Таблица степеней.

m - число, а - степень.''')
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo='http://www.mathtask.ru/page-0014/t1_deg.png')
    elif query.data == 'sq2':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='''Таблица квадратов.''')
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo='http://www.mathtask.ru/page-0014/t2_square.png')
    elif query.data == 'sq3':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='''Таблица кубов.''')
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo='http://www.mathtask.ru/page-0014/t3_cube.png')
    elif query.data == 'ln':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='''Таблица натуральных логарифмов.''')
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo='http://www.mathtask.ru/page-0014/t4_ln.png')
    elif query.data == 'lg':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='''Таблица десятичных логарифмов.''')
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo='http://www.mathtask.ru/page-0014/t5_lg.png')
    elif query.data == 'log':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='''Таблица логарифмов по основанию а.''')
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo='http://www.mathtask.ru/page-0014/t6_log.png')
    elif query.data == 'brad':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='''Таблица Брадиса
                                 
sin, cos''')
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo='http://www.mathtask.ru/page-0014/t7_brad1.png')
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='''Таблица Брадиса
                                 
tg, ctg''')
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo='http://www.mathtask.ru/page-0014/t7_brad2.png')
    elif query.data == 'brad1':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='''Таблица Брадиса
                                 
sin, cos''')
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo='http://www.mathtask.ru/page-0014/t7_brad1.png')
    elif query.data == 'brad2':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='''Таблица Брадиса
tg, ctg''')
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo='http://www.mathtask.ru/page-0014/t7_brad2.png')
    return MENU


def geometry(update, _):
    keyboard = [
        [InlineKeyboardButton("ПЛАНИМЕТРИЯ", callback_data='g11'),
         InlineKeyboardButton("СТЕРЕОМЕТРИЯ", callback_data='g12')],
        [InlineKeyboardButton("Треугольник", callback_data='g21'),
         InlineKeyboardButton("Пирамида", callback_data='g22')],
        [InlineKeyboardButton("Квадрат", callback_data='g31'), InlineKeyboardButton("Куб", callback_data='g32')],
        [InlineKeyboardButton("Прямоугольник", callback_data='g41'),
         InlineKeyboardButton("Параллелепипед", callback_data='g42')],
        [InlineKeyboardButton("Параллелограм", callback_data='g51'),
         InlineKeyboardButton("Призма", callback_data='g52')],
        [InlineKeyboardButton("Ромб", callback_data='g61'), InlineKeyboardButton("Цилиндр", callback_data='g62')],
        [InlineKeyboardButton("Трапеция", callback_data='g71'), InlineKeyboardButton("Конус", callback_data='g72')],
        [InlineKeyboardButton("Окружность", callback_data='g81'), InlineKeyboardButton("Шар", callback_data='g82')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query = update.callback_query
    if query:
        query.answer()

        if query.data == 'return_1':
            query.edit_message_text('Таблицы:', reply_markup=reply_markup)
    else:
        update.message.reply_text('Таблицы:', reply_markup=reply_markup)
    return MENU


def geometry_answer(update, _):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("Назад ↩️", callback_data='return_1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if query.data == 'g11':
        query.edit_message_text(text='Планиметрия.\n\nПланиметрия - наука, изучающий двумерные (одно'
                                     'плоскостные) фигуры, то есть фигуры, которые можно расположить'
                                     ' в пределах одной плоскости.\n\n'
                                     'https://ru.wikipedia.org/wiki/%D0%9F%D0%BB%D0%B0%D0%BD%D0%B8%D'
                                     '0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%8F',
                                     reply_markup=reply_markup)
    elif query.data == 'g12':
        query.edit_message_text(text='''Стереометрия.
        
Стереометрия - наука, изучающая пространственные фигуры и их свойства.

https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B5%D1%80%D0%B5%D0%BE%D0%BC%D0%B''' +
                                     '5%D1%82%D1%80%D0%B8%D1%8F',
                                reply_markup=reply_markup)
    elif query.data == 'g21':
        query.edit_message_text(text='''Треугольник.

Треугольник - геометрическая фигура, образованная тремя отрезками, 
которые соединяют три точки, не лежащие на одной прямой. 
Указанные три точки называются вершинами треугольника, а отрезки сторонами треугольника.

S = 1/2a*h
S = √(p*(p-a)*(p-b)*(p-c))
S = 1/2a*b*sinc
S = (a*b*c)/R
S = p*r
a - сторона треугольника
h - высота (в данном случае непосредственно падающая на сторону a)
p - полупериметр
sinc - синус угла между сторонами a и b
R - радиус описанной окружности
r - радиус вписанной окружности

https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B5%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA''',
                                reply_markup=reply_markup)
    elif query.data == 'g22':
        query.edit_message_text(text='''Пирамида.

Пирамида - многогранник у которого одна грань- произвольный многоугольник, называемое основанием,
 а остальные грани треугольники имеющие общую вершину.

S = площади всех треугольников и основания
S(треугольника) = (а*h)/2
S основания вычисляется в зависимости от его формы, универсальной формулы нет.

https://ru.wikipedia.org/wiki/%D0%9F%D0%B8%D1%80%D0%B0%D0%BC%D0%B8%D0%B4%D0%B0''',
                                reply_markup=reply_markup)
    elif query.data == 'g31':
        query.edit_message_text(text='''Квадрат.

Квадрат - правильный четырёхугольник у которого все углы и всё стороны равны. 
Квадрат является частным случаем ромба и прямоугольника.

S = a^2
Р = 4а.
a - сторона квадрата

https://ru.wikipedia.org/wiki/%D0%9A%D0%B2%D0%B0%D0%B4%D1%80%D0%B0%D1%82''',
                                reply_markup=reply_markup)
    elif query.data == 'g32':
        query.edit_message_text(text='''Куб

Куб - правильный многогранник, каждая грань которого представляет собой квадрат. 
Частный случай параллелипипеда и призмы.

S = 6а^2
Р = 12*а
а - ребро.

https://ru.wikipedia.org/wiki/%D0%9A%D1%83%D0%B1''', reply_markup=reply_markup)
    elif query.data == 'g41':
        query.edit_message_text(text='''Прямоугольник.

Прямоугольник - четырехугольник, у которого все углы прямые(90градусов).

S= a*b
P = 2(a+b)
a и b - стороны прямоугольника.

https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D1%8F%D0%BC%D0%BE%D1%83%D0%''' +
                                     'B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA',
                                reply_markup=reply_markup)
    elif query.data == 'g42':
        query.edit_message_text(text='''Параллелепипед.

Параллелипипед - призма, основанием которой служит параллелограмм, или многогранник, 
у которого шесть граней и каждая является параллелограммом.

S = 2(ab+bc+ac)
Р = 4(а+b+c)
a,b и с - рёбра параллелепипеда.

https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D1%80%D0%B0%D0%BB%D0%BB%''' +
                                     'D0%B5%D0%BB%D0%B5%D0%BF%D0%B8%D0%BF%D0%B5%D0%B4',
                                reply_markup=reply_markup)
    elif query.data == 'g51':
        query.edit_message_text(text='''Параллелограмм.

Параллелограмм - четырехугольник, у которого стороны попарно параллельны. 
Признаки параллелограмма: Если противоположные стороны четырехугольника попарно параллельны, 
то этот четырехугольник называется параллелограммом.

S = a*h
P = 2*(a+b)
h - высота непосредственно падающая на сторону a.

https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D1%80%D0%B0%D0%BB%D0%BB%D0%B5%D0%''' +
                                     'BB%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC',
                                reply_markup=reply_markup)
    elif query.data == 'g52':
        query.edit_message_text(text='''Призма.
        
Призма -  многогранник, две грани которого являются равными многоугольниками, лежащими в параллельных плоскостях,
а остальные грани — параллелограммами, имеющими общие стороны с этими многоугольниками. 

Многоугольник, лежащий в основании, определяет название призмы
Призма является частным случаем цилиндра в общем смысле (некругового).
        
https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B8%D0%B7%D0%BC%D0%B0_(%D0%B3%D0%B5%D0%BE%D0%''' +
                                     'BC%D0%B5%D1%82%D1%80%D0%B8%D1%8F)',
                                reply_markup=reply_markup)
    elif query.data == 'g61':
        query.edit_message_text(text='''Ромб.

Ромб - параллелограмм, у которого все стороны равны.

S = 1/2*d1*d2
S = ah
P = 4a
d1 и d2 - диагонали ромба
h - высота ромба
a - сторона ромба.

https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D0%BC%D0%B1''',
                                reply_markup=reply_markup)
    elif query.data == 'g62':
        query.edit_message_text(text='''Цилиндр.

Цилиндр -  геометрическое тело, ограниченное цилиндрической поверхностью и двумя параллельными плоскостями, 
пересекающими её.

Для прямого кругового цилиндра:
P = 2*pi*r
S = P*h
S = 2*pi*r*h
pi - число пи
h - высота цилиндра
r - радиус основания.

https://ru.wikipedia.org/wiki/%D0%A6%D0%B8%D0%BB%D0%B8%D0%BD%D0%B4%D1%80''',
                                reply_markup=reply_markup)
    elif query.data == 'g71':
        query.edit_message_text(text='''Трапеция.

Трапеция - выпуклый четырехугольник, у которого две стороны параллельны, а две другие нет. 
Две параллельные стороны трапеции называются её основаниями, а две другие- боковыми сторонами.

S = (a+b)/2*h
S = (a+b)/2*√(c^2-(((a-b)^2+c^2-d^2)/2*(a-b))^2)
Р = a+b+c+d
a - верхнее основание
b - нижнее основание
c и d - боковые стороны
h - высота непосредственно подающая с верхнего основания на нижнее.

https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BF%D0%B5%D1%86%D0%B8%D1%8F''',
                                reply_markup=reply_markup)
    elif query.data == 'g72':
        query.edit_message_text(text='''Конус.

Конус - тело в евклидовом пространстве полученное объединением всех лучей исходящих, 
из одной точки и проходящих через плоскую поверхность.

S = πr^2+πRl
l- образующая конуса.

https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BD%D1%83%D1%81''',
                                reply_markup=reply_markup)
    elif query.data == 'g81':
        query.edit_message_text(text='''Круг.

Круг - часть плоскости, лежащая внутри окружности. 
Другими словами, это геометрическое место точек плоскости, расстояние от которых до заданной точке,
называемой центром круга, не превышает заданного неотрицательного числа называется радиусом данного круга.

S = πr^2
P = 2πr
r - радиус круга
π - 3,1415926535897....

https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D1%83%D0%B3''',
                                reply_markup=reply_markup)
    elif query.data == 'g82':
        query.edit_message_text(text='''Сфера.

Сфера - геометрическое место точек в пространстве, равно удаленные от некоторой заданной точки. 
Расстояние от центра сферы до её любой точки называется её радиусом. Сфера радиуса 1 называется единичной сферой.

S = 4πR^2.

https://ru.wikipedia.org/wiki/%D0%A1%D1%84%D0%B5%D1%80%D0%B0''',
                                reply_markup=reply_markup)
    return MENU


def trigonometric(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='''Основные тригонометрические тождества.
https://telegra.ph/Osnovnye-trigonometricheskie-tozhdestva-04-08''')
    return MENU


def calc(update, _):
    keyboard = [
        [InlineKeyboardButton("Сложение", callback_data='c1'),
         InlineKeyboardButton("Вычитание", callback_data='c2')],
        [InlineKeyboardButton("Умножение", callback_data='c3')],
        [InlineKeyboardButton("Деление", callback_data='c4.1'),
         InlineKeyboardButton("Деление с остатком", callback_data='c4.2')],
        [InlineKeyboardButton("Возвести в степень", callback_data='c5.1'),
         InlineKeyboardButton("Извлечь корень", callback_data='c5.2')],
        [InlineKeyboardButton("Логарифм", callback_data='c6')],
        [InlineKeyboardButton("Синус", callback_data='c7.1'),
         InlineKeyboardButton("Косинус", callback_data='c7.2')],
        [InlineKeyboardButton("Тангенс", callback_data='c8.1'),
         InlineKeyboardButton("Котангенс", callback_data='c8.2')],
        [InlineKeyboardButton("Факториал", callback_data='c9')],
        [InlineKeyboardButton("НОД", callback_data='c10.1'),
         InlineKeyboardButton("НОК", callback_data='c10.2')],
        [InlineKeyboardButton("Проценты", callback_data='c11')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Что вы хотите вычислить?', reply_markup=reply_markup)
    return MENU


def calc_choice(update, context):
    global op
    reply_keyboard = [
                      ['Отмена']
    ]

    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    query = update.callback_query
    query.answer()
    s = ''
    op = query.data

    if query.data == 'c1':
        s = 'два числа, которые вы хотите сложить, через пробел.'
    elif query.data == 'c2':
        s = 'два числа a и b, разность которых вы хотите получить(a - b), через пробел.'
    elif query.data == 'c3':
        s = 'два числа, которые вы хотите перемножить, через пробел.'
    elif query.data == 'c4.1':
        s = 'делимое и делитель (не 0), чтобы получить частное, через пробел.'
    elif query.data == 'c4.2':
        s = 'делимое и делитель (не 0), чтобы получить частное с остатком, через пробел.'
    elif query.data == 'c5.1':
        s = 'число и степень, в которую вы хотите возвести это число, через пробел.'
    elif query.data == 'c5.2':
        s = 'число и степень извлечения корня, через пробел.'
    elif query.data == 'c6':
        s = 'число, которое нужно возвести в логарифм, и основание логарифма через пробел.'
    elif query.data in 'c7.1|c7.2|c8.1|c8.2':
        s = 'градус угла фигуры.'
    elif query.data == 'c9':
        s = 'число для вычисления его факториала.'
    elif query.data == 'c10.1':
        s = 'два числа через пробел для вычиления НОД.'
    elif query.data == 'c10.2':
        s = 'два числа через пробел для вычиления НОК.'
    elif query.data == 'c11':
        s = 'число и процент через пробел, для нахождения процента от данного числа.'

    context.bot.send_message(text='Отправьте ' + s + '''\nДля нецелых чисел используйте точку.''',
                             chat_id=update.effective_chat.id, reply_markup=markup)
    return CALC


def calc_input(update, context):
    global op
    try:
        nums = [float(i) for i in update.message.text.split()]
        answer = ''
        if not ((op in 'c1|c2|c3|c4.1|c4.2|c5.1|c5.2|c6|c10.1|c10.2|c11' and len(nums) == 2) or
                (op in 'c7.1|c7.2|c8.1|c8.2|c9' and len(nums) == 1)):
            raise SystemError
        if int(nums[0]) == float(nums[0]):
            nums[0] = int(nums[0])
        if len(nums) == 2:
            if int(nums[1]) == float(nums[1]):
                nums[1] = int(nums[1])
        if op == 'c1':
            answer = f'{nums[0]} + {nums[1]} = {sum(nums)}'
        elif op == 'c2':
            answer = f'{nums[0]} - {nums[1]} = {nums[0] - nums[1]}'
        elif op == 'c3':
            answer = f'{nums[0]} * {nums[1]} = {nums[0] * nums[1]}'
        elif op == 'c4.1' or op == 'c4.2':
            if nums[1] == 0:
                context.bot.send_message(text='Ошибка!\n\nНа ноль делить нельзя.\n'
                                              'Попробуйте ввести ещё раз.',
                                         chat_id=update.effective_chat.id)
                return CALC
            if op == 'c4.1':
                answer = f'{nums[0]} : {nums[1]} = {nums[0] / nums[1]}'
            elif op == 'c4.2':
                answer = f'{nums[0]} : {nums[1]} = {nums[0] // nums[1]}(ост.{nums[0] % nums[1]})'
        elif op == 'c5.1':
            answer = f'{nums[0]} ^ {nums[1]} = {nums[0] ** nums[1]}'
        elif op == 'c5.2':
            answer = f'Корень в степени {nums[1]} числа {nums[0]} = {nums[0] ** (1 / nums[1])}'
        elif op == 'c6':
            answer = f'Логарифм числа {nums[0]} по основанию {nums[1]} = {log(nums[0], nums[1])}'
        elif op == 'c7.1':
            answer = f'sin {nums[0]}° = {sin(radians(nums[0]))}'
        elif op == 'c7.2':
            answer = f'cos {nums[0]}° = {cos(radians(nums[0]))}'
        elif op == 'c8.1':
            if nums[0] % 90 == 0 and nums[0] % 180 != 0:
                answer = f'tg {nums[0]}° не существует'
            else:
                answer = f'tg {nums[0]}° = {tan(radians(nums[0]))}'
        elif op == 'c8.2':
            if nums[0] % 180 == 0:
                answer = f'сtg {nums[0]}° не существует'
            else:
                answer = f'ctg {nums[0]}° = {1 / tan(radians(nums[0]))}'
        elif op == 'c9':
            answer = f'{nums[0]}! = {factorial(nums[0])}'
        elif op == 'c10.1' or op == 'c10.2':
            if nums[0] <= 0 or nums[1] <= 0:
                context.bot.send_message(text='Ошибка!\n\nВы ввели не натуральные числа.\n'
                                              'Попробуйте ввести ещё раз.',
                                         chat_id=update.effective_chat.id)
                return CALC
            elif type(nums[0]) == int and type(nums[1]) == int:
                if op == 'c10.1':
                    answer = f'НОД({nums[0]}, {nums[1]}) = {gcd(int(nums[0]), int(nums[1]))}'
                elif op == 'c10.2':
                    m = min(nums[0], nums[1])
                    while not (m % nums[0] == 0 and m % nums[1] == 0):
                        m += 1
                    answer = f'НОК({nums[0]}, {nums[1]}) = {m}'
            else:
                context.bot.send_message(text='Ошибка!\n\nВы ввели не целые числа.\n'
                                              'Попробуйте ввести ещё раз.',
                                         chat_id=update.effective_chat.id)
                return CALC
        elif op == 'c11':
            answer = f'{nums[1]}% от числа {nums[0]} = {nums[0] * nums[1] / 100}'
    except Exception:
        context.bot.send_message(text='Ошибка!\n\nБыли введены некорректные данные.\n'
                                      'Попробуйте ввести ещё раз.',
                                 chat_id=update.effective_chat.id)
        return CALC
    op = ''
    context.bot.send_message(text=answer, chat_id=update.effective_chat.id, reply_markup=menu_markup())
    return MENU


def cancel(update, context):
    global op
    op = ''
    context.bot.send_message(chat_id=update.effective_chat.id, text='Отменено.', reply_markup=menu_markup())

    return MENU


def exit_(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    reply_keyboard = [
                      ['/start'],
                      ['/help']]

    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text(
        'Надеюсь, когда-нибудь снова сможем поговорить.\n'
        'До новых встреч!',
        reply_markup=markup)
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    MENU, TABLES, CALC = range(3)
    op = ''

    dispatcher.add_handler(CommandHandler("help", help_))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            MENU: [
                   CommandHandler('start', start),
                   MessageHandler(Filters.regex('^(Таблицы)$'), tables),
                   CallbackQueryHandler(tables_answer, pattern='^(sq|sq2|sq3|ln|log|lg|'
                                                               'brad|brad1|brad2)$'),
                   MessageHandler(Filters.regex('^(Геометрия)$'), geometry),
                   CallbackQueryHandler(geometry, pattern='^(return_1)$'),
                   CallbackQueryHandler(geometry_answer, pattern='^(g11|g12|g21|g22|g31|g32|g41|g42|'
                                                                 'g51|g52|g61|g62|g71|g72|g81|g82)$'),
                   MessageHandler(Filters.regex('^(Тригонометрия)$'), trigonometric),
                   MessageHandler(Filters.regex('^(Калькулятор)$'), calc),
                   CallbackQueryHandler(calc_choice, pattern='^(c1|c2|c3|c4.1|c4.2|c5.1|c5.2|c6|c7.1|'
                                                             'c7.2|c8.1|c8.2|c9|c10.1|c10.2|c11)$')
                   ],
            CALC: [CallbackQueryHandler(calc_choice, pattern='^(c1|c2|c3|c4.1|c4.2|c5.1|c5.2|c6|c7.1|'
                                                             'c7.2|c8.1|c8.2|c9|c10.1|c10.2|c11)$'),
                   MessageHandler(Filters.regex('^(Отмена)$'), cancel),
                   MessageHandler(Filters.text, calc_input)
                   ]
        },

        fallbacks=[CommandHandler('exit', exit_)]
        )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()
