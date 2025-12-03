df = pd.DataFrame({'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
                   'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
                   'name': ['Murzik', 'Pushok', 'Kaa', 'Bobik', 'Strelka', 'Vaska', 'Kaa2', 'Murka', 'Graf', 'Muhtar'],
                   'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                   'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']},
                   index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
'''
Создайте Dataframe из словаря data. В качестве подписей строк используйте список labels.
'''
import pandas as pd
#1
df = pd.DataFrame(data=data,index=labels)
#2
df = pd.DataFrame(data,labels)


'''
Переменная df содержит DataFrame.Переменная col содержит имя колонки.Переменная row содержит имя ИЛИ индекс строки.Выведите на печать содержимое ячейки.
'''
#1
print(df.loc[row,col])
#2
print(df.at[row, col])


'''
Переменная df содержит DataFrame.Выведите на печать:число непустых (не null) значений в колонке 'age',75% квантиль для значений в колонке 'age'
'''
#1
buffer = io.StringIO() 
df.info(buf=buffer)
a= buffer.getvalue()
L=[]
a.splitlines()
for line in a.splitlines():
  L.append(line.split())
print(float(L[6][2]))
print(df["age"].quantile(0.75))
#2
print(df.describe()['age']['count'])
print(df.describe()['age']['75%'])


'''
Переменная df содержит DataFrame. Выведите на печать 3 первых строки.
'''
#1
print(df[:3])
#2
print(df.iloc[:3])
#3
print(df.head(3))


'''
Переменная df содержит DataFrame. Выведите на печать строки с индексами 0, 2, 3.
'''
print(df.iloc[[0,2,3]])


'''
Переменная df содержит DataFrame. Выведите на печать только столбцы 'name' и 'age'
'''
#1
print(df.loc[:,['name','age']])
#2
print(df[['name', 'age']])


'''
Переменная df содержит DataFrame.Выведите на печать только столбцы 'name' и 'age' И строки 0, 2, 3
'''
print(df.iloc[[0,2,3]][['name', 'age']])


'''
Переменная df содержит DataFrame. Выведите на печать только данные, относящиеся к записям, возраст которых больше, указанного в переменной critical_age.
'''
print(df[df.age>critical_age])


'''
Переменная df содержит DataFrame.Выведите на печать только данные, в которых не заполнен возраст (в графе 'age' стоит null).
'''
print(df[df.age.isna()])


'''
Переменная df содержит DataFrame. Переменная filter_names содержит список имён столбцов по которым происходит фильтрация. Переменная filter_values содержит список 
из 2 значений по которым происходит фильтрация. 1 значение проверяется на равенство. 2 значение должно быть меньше указанного в фильтре. 
Выведите только те строки датафрейма, которые удовлетворяют условиям обоих фильтров.
'''
print(df[(df[filter_names[0]]==filter_values[0]) & (df[filter_names[1]]<filter_values[1])])
