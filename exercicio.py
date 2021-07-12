import pandas
import math

#Exercicio 1
dataBase = pandas.read_json('broken-database.json')
dataBase["name"] = dataBase["name"].replace({"æ":"a", "¢":"c", "ø":"o", "ß":"b"},regex=True)

#Exercicio 2
j = 0
for i in dataBase["price"]:
    if(type(i)==str):
        dataBase["price"][j] = float(i)
    j = j+1

#Exercicio 3
j = 0
for i in dataBase["quantity"]:
    if(math.isnan(i)):
        dataBase["quantity"][j] = 0
    j = j+1
print(dataBase["quantity"])