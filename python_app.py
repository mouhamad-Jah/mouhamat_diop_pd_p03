transactions_list = [250, 12, 45, 32, 23, 25, 250, 12]
# Écris un programme qui fait la somme des transactions.
valeur_totale = sum(transactions_list)

print(valeur_totale)

#Afficher la 5eme transaction 

print(transactions_list[4])

#Ordonner la liste (asc)

transactions_list.sort()
print('List in Ascending Order: ', transactions_list)


#Transformer la liste en tuple


liste_tuple = tuple(transactions_list)
print(transactions_list)

#Afficher la transaction la plus petite


valeur_totale =min (transactions_list)
print(valeur_totale)
#Afficher la dernière transaction
transactions_list= transactions_list
print(transactions_list[-1])
#Supprimer les transactions dupliquées




resultantList = []
 
for element in transactions_list:
    if element not in resultantList:
        resultantList.append(element)

print(resultantList)

#Supprimer la dernière transaction



del transactions_list [-1]
print(transactions_list)

#Créer une copie des transactions



# copying a list
numbers = transactions_list.copy()
print('Copied List:', numbers)

#Écris un programme qui fait la moyenne des transactions.

def Average(l): 
    avg = sum(l) / len(l) 
    return avg
 
average = Average(transactions_list) 
  
print("Average of my_list is", average)

#Convertir la liste en dictionnaire

 
  
transactions_list_dictionary = { stu : "Passed" for stu in transactions_list }  
  
print(transactions_list)  


# Convertir la liste en tuple

liste_tuple = tuple(transactions_list)
print(transactions_list)
