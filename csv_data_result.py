import csv
import os

import ar_master

mm = ar_master.master_flask_code('python_customer_behaviour')
class ar_csv:
    def __init__(self):
        ar=0
    def read_dataset_result(self):
        csv_file1 = os.path.join("static/uploads/", ('dataset.csv'))
        no_of_items = []
        with open(csv_file1, mode='r', encoding="cp437") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                itemDescription = row['itemDescription']
                no_of_items.append(itemDescription)
        res = []
        for i in no_of_items:
            if i not in res:
                res.append(i)

        res.remove('')
        mydictionary = {}
        for i in res:
            mydictionary[i] = 0

        f.close()

        csv_file2 = os.path.join("static/uploads/", ('dataset1.csv'))

        with open(csv_file2, mode='r') as f1:
            reader1 = csv.DictReader(f1, delimiter=',')
            for row1 in reader1:
                itemDescription = row1['itemDescription']
                Quantity = row1['Quantity']

                if (itemDescription != ''):
                    newcount = int(Quantity)
                    prevoius = int(mydictionary[itemDescription])
                    total = prevoius + newcount
                    mydictionary[itemDescription] = total
        mm.insert_query("delete from search_result")
        for x in mydictionary:
            data=x
            result=mydictionary[data]
            mm.insert_query("insert into search_result values('"+str(data)+"','"+str(result)+"')")

    def customer_behaviour(self):
        csv_file1 = os.path.join("static/uploads/", ('dataset.csv'))
        no_of_items = []
        with open(csv_file1, mode='r', encoding="cp437") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                itemDescription = row['itemDescription']
                Member_number = row['Member_number']
                no_of_items.append(Member_number)
        res = []
        for i in no_of_items:
            if i not in res:
                res.append(i)

        res.remove('')
        mydictionary = {}
        for i in res:
            mydictionary[i] = ''

        f.close()

        csv_file2 = os.path.join("static/uploads/", ('dataset.csv'))
        print(csv_file2)
        with open(csv_file2, mode='r') as f1:
            reader1 = csv.DictReader(f1, delimiter=',')
            for row1 in reader1:
                Member_number = row1['Member_number']
                itemDescription = row1['itemDescription']
                if (itemDescription != ''):
                    prevoius = (mydictionary[Member_number])
                    total = prevoius +''+ itemDescription+','
                    mydictionary[Member_number] = total

        mm.insert_query("delete from search_result1")
        ar_qry="insert into search_result1 values "
        for x in mydictionary:
            data = x
            result = mydictionary[data]
            ar_qry+=" ('" + str(data) + "','" + str(result) + "'),"
            # mm.insert_query(" values('" + str(data) + "','" + str(result) + "')")\
        ar_qry = ar_qry[:-1]

        print(ar_qry)
        mm.insert_query(ar_qry)



# dd=ar_csv()
# dd.customer_behaviour()

