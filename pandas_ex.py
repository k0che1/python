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


'''
Переменная df - DataFrame.Переменная age_between содержит 2 числа. Выведите только те строки датафрейма, возраст в которых находится в интервале между числами age_between (включая границы).
'''
#1
print(df[(df['age']>=age_between[0]) & (df['age']<=age_between[1])])
#2
print(df[df['age'].between(*age_between)])


'''
Переменная df содержит DataFrame. Переменная index содержит строку ИЛИ число (индекс).Увеличьте значение возраста в строке индексом равным index на 1.
'''
#1
df.loc[index,'age']+=1
#2
df['age'][index] += 1


'''
Переменная df содержит DataFrame. Выведите на печать сумму всех возрастов в df.
'''
#1
print(df['age'].sum())
#2
print(np.sum(df.age))


'''
Переменная df содержит DataFrame.Выведите на печать для каждого столбца, содержащего числа его имя и сумму через двоеточие.
'''
#1
for x in df.describe():
    print(x + ":" + str(df[x].sum()))

#2
c=df.sum(numeric_only=True).index.values.tolist()
a=df.sum(numeric_only=True)
for i in range(len(c)):
  print(f'{c[i]}:{a[i]}')


'''
df - DataFrame.Переменная group_by содержит имя колонки по которой производится группировка. Найдите средние значение возраста по всем записям, сгруппированным по значению 
в колонке group_by и выведите на печать. Например, если group_by='animal', то для первого Dataframe надо получить таблицу со средними для каждого вида животных: кошек, собак, змей.
'''
print(df.groupby([group_by])['age'].mean())


'''
Переменная df содержит DataFrame. new_index - индекс для строки, которую надо добавить, new_data - значения для строки, которую надо добавить, del_index - индекс строки, которую надо удалить.
Добавьте новую строку (с индексом new_index и значениями new_data) и удалите одну из старых (del_index)
'''
df.loc[new_index]=new_data
df.drop(del_index, inplace=True)
# df = df.drop(del_index)


'''
Переменная df содержит DataFrame.Переменная group_by содержит имя колонки по которой производится группировка. Найдите количество записей каждого типа, сгруппированным 
по значению в колонке group_by.Например, если group_by='animal', то для первого Dataframe надо получить таблицу с количеством каждого вида животных: кошек, собак, змей.
'''
print(df[group_by].value_counts())


'''
Переменная df содержит DataFrame.Переменная sort_by содержит список из 2 строк - имён столбцов по которым необходимо провести сортировку.
Отсортируйте сперва по уменьшению 1 поля из списка sort_by, а при равенстве значений по увеличению 2.
'''
#1
df.sort_values(*[sort_by],ascending=[False,True], inplace=True)
print(df)
#2
print(df.sort_values(sort_by, ascending=(False, True)))


'''
Переменная df содержит DataFrame. Переменная column содержит имя колонки, содержащей строковые значения "yes", "no", либо числовые 1 или 0.
Замените в column: "yes" и 1 на True, "no" и 0 на False
'''
#1
z = {'yes': True, 'no': False, 0: False, 1: True
df[column] =df[column].map(z)
#2
df[column] = df[column].isin([1, 'yes'])


'''
Переменная df содержит DataFrame. Переменная column содержит имя колонки, значения в которой надо модифицировать. Переменные old_value и new_value содержат старое 
и новое значения, соответственно.Замените все старые значения на новые в соответсвующей колонке.
'''
df[column]=df[column].replace(old_value,new_value)


'''
В файле torg.csv представлена выгрузка со склада интернет-магазина. Товаров какого цвета больше всего на складе?
'''
df = pd.read_csv('torg.csv', sep=';')
df_group = df[['IP_PROP30', 'CP_QUANTITY']].groupby('IP_PROP30')
print(df_group.sum().idxmax())


'''
В файле torg.csv представлена выгрузка со склада интернет-магазина. Сгруппируйте размеры представленных товаров по суммарному количеству единиц товара на складе.
'''
df_group = df[['IP_PROP32', 'CP_QUANTITY']].groupby('IP_PROP32')
print(df_group.sum().sort_values(by='CP_QUANTITY'))


'''
В этом задании представлена выгрузка складских остатков. Найдите суммарную стоимость всех розовых (pink) вещей большого размера (XL).
'''
df['cost'] = df.CP_QUANTITY * df.CR_PRICE_1_USD
df=df[(df['IP_PROP30']=='pink')&(df['IP_PROP32']=='XL')].cost.sum()
