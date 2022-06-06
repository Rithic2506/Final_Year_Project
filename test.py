import csv
import os

csv_file1 = os.path.join("static/uploads/", ('dataset.csv'))
no_of_items=[]
with open(csv_file1, mode='r', encoding="cp437") as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        itemDescription=row['itemDescription']
        no_of_items.append(itemDescription)
res = []
for i in no_of_items:
    if i not in res:
        res.append(i)

res.remove('')
mydictionary={}
for i in res:
    mydictionary[i]=0
print(mydictionary)
f.close()


csv_file2 = os.path.join("static/uploads/", ('dataset1.csv'))
print(csv_file2)
with open(csv_file2, mode='r') as f1:
    reader1 = csv.DictReader(f1, delimiter=',')
    for row1 in reader1:
        itemDescription=row1['itemDescription']
        Quantity = row1['Quantity']

        if(itemDescription!=''):
            newcount=int(Quantity)
            prevoius = int(mydictionary[itemDescription])
            total = prevoius + newcount
            mydictionary[itemDescription] = total
print(mydictionary)
