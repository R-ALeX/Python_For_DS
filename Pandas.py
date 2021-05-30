# Задание 1

# Импортируйте библиотеку Pandas и дайте ей псевдоним pd.
# Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные:
# [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].

# Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:
# [1, 1, 1, 2, 2, 3, 3],
# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
# [450, 300, 350, 500, 450, 370, 290].

import pandas as pd

print(f' ---TASK1--- \n')

authors = pd.DataFrame({'author_id':[1, 2, 3],
                        'author_name':['Тургенев', 'Чехов', 'Островский']},
                       columns=['author_id', 'author_name'])
print(authors)

print(f'\n --------- \n')

book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],
                     'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                     'price':[450, 300, 350, 500, 450, 370, 290]},
                    columns=['author_id', 'book_title', 'price'])
print(book)

print(f'\n --------- \n')

#Задание 2
#Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.

print(f'\n ---TASK2--- \n')

authors_price = pd.merge(authors, book, on = 'author_id', how = 'outer')
print(authors_price)

print(f'\n --------- \n')

#Задание 3
#Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.

print(f'\n ---TASK3--- \n')

top5 = authors_price.nlargest(5, 'price')
print(top5)

print(f'\n --------- \n')

#Задание 4
# Создайте датафрейм authors_stat на основе информации из authors_price.
# В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.

print(f'\n ---TASK4--- \n')

authors_stat = authors_price['author_name'].value_counts()
print(authors_stat)

print(f'\n --------- \n')

authors_stat = authors_price.groupby('author_name').agg({'price':['min', 'max', 'mean']})
authors_stat = authors_stat.rename(columns={'min':'min_price', 'max':'max_price', 'mean':'mean_price'})
print(authors_stat)

print(f'\n --------- \n')

