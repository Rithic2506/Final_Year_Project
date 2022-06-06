import csv
import os
from difflib import SequenceMatcher
from urllib import request

from flask import Flask, render_template, request, session
from werkzeug.utils import secure_filename

import ar_master
# ps = PorterStemmer()
import csv_data_result

app = Flask(__name__, static_folder='static',template_folder='templates',static_url_path='/static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

mm = ar_master.master_flask_code('python_customer_behaviour')



@app.route("/")
def homepage():
    return render_template('index.html')
@app.route("/admin")
def admin():
    return render_template('admin.html')
@app.route("/admin_login", methods = ['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['pass'] == 'admin':
            return render_template('admin_home.html',error=error)
        else:
            return render_template('admin.html', error=error)
@app.route("/admin_home")
def admin_home():
    return render_template('admin_home.html')
@app.route("/employee")
def employee():
    return render_template('employee.html')
@app.route("/manager")
def manager():
    return render_template('manager.html')
@app.route("/admin_add_dataset", methods=['GET', 'POST'])
def admin_add_dataset():
    if request.method == 'POST':
        file = request.files['file']
        print(file)
        f = request.files['file']
        f.save(os.path.join("static/uploads/", secure_filename('dataset.csv')))
        f.save(os.path.join("static/uploads/", secure_filename('dataset1.csv')))
        return render_template('admin_add_dataset.html', msg="Success")
    else:
        return render_template('admin_add_dataset.html')
    return render_template('admin_add_dataset.html')
@app.route("/admin_add_manager", methods=['GET', 'POST'])
def admin_add_manager():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']
        maxin = mm.find_max_id("manager_details")
        qq = "insert into manager_details values('" + str(maxin) + "','" + str(name) + "','" + str(contact) + "','" + str(
            email) + "','" + str(address) + "','" + str(username) + "','" + str(password) + "','0','0')"
        result = mm.insert_query(qq)

        if (result == 1):
            return render_template('admin_add_manager.html', msg="Success")
        else:
            return render_template('admin_add_manager.html')

        return render_template('admin_add_manager.html', msg="Success")
    else:
        return render_template('admin_add_manager.html')
    return render_template('admin_add_manager.html')


@app.route("/admin_search_product", methods=['GET', 'POST'])
def admin_search_product():
    # qry=("delete from search_details")
    # result=mm.insert_query(qry)
    if request.method == 'POST':
        total_quantity=0
        data = request.form['name']
        csv_file1 = os.path.join("static/uploads/", ('dataset.csv'))
        result_data=[]
        with open(csv_file1, mode='r', encoding="cp437") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                Member_number = row['Member_number']
                itemDescription=row['itemDescription']
                Quantity=row['Quantity']
                data = data.lower()
                itemDescription = itemDescription.lower()
                result = SequenceMatcher(None, data, itemDescription).ratio()
                if (result >= 1):
                    result_data.append([Member_number,itemDescription,Quantity],)
                    total_quantity = total_quantity + (int(Quantity))
        #             result = result + 1

        #             mm.insert_query("insert into search_details values('"+str(Member_number)+"','"+str(itemDescription)+"','"+str(Quantity)+"')")
        # items=mm.select_direct_query("select * from search_details")
        return render_template('admin_search_product1.html',items=result_data,total_quantity=total_quantity)
    return render_template('admin_search_product.html')



@app.route("/manager_login",methods = ['GET', 'POST'])
def manager_login():
    msg=None
    if request.method == 'POST':
        n = request.form['uname']
        g = request.form['pass']
        n1=str(n)
        g1=str(g)

        q=("SELECT * from manager_details where username='" + n1 + "' and password='" + str(g) + "'")
        data=mm.select_direct_query(q)
        if data==0:
            return render_template('manager.html',error=msg)
        else:
            msg='Success'
            session['manager'] =n
            return render_template('manager_home.html',sid=n)
    return render_template('manager.html',error=msg)

@app.route("/manager_home")
def manager_home():
    return render_template('manager_home.html')


@app.route("/manager_add_employee", methods=['GET', 'POST'])
def manager_add_employee():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']
        maxin = mm.find_max_id("employee_details")
        qq = "insert into employee_details values('" + str(maxin) + "','" + str(name) + "','" + str(contact) + "','" + str(
            email) + "','" + str(address) + "','" + str(username) + "','" + str(password) + "','0','0')"
        result = mm.insert_query(qq)

        if (result == 1):
            return render_template('manager_add_employee.html', msg="Success")
        else:
            return render_template('manager_add_employee.html')

        return render_template('manager_add_employee.html', msg="Success")
    else:
        return render_template('manager_add_employee.html')
    return render_template('manager_add_employee.html')


@app.route("/manager_search_product", methods=['GET', 'POST'])
def manager_search_product():
    # qry=("delete from search_details")
    # result=mm.insert_query(qry)
    if request.method == 'POST':
        total_quantity=0
        data = request.form['name']
        csv_file1 = os.path.join("static/uploads/", ('dataset.csv'))
        result_data=[]
        with open(csv_file1, mode='r', encoding="cp437") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                Member_number = row['Member_number']
                itemDescription=row['itemDescription']
                Quantity=row['Quantity']
                data = data.lower()
                itemDescription = itemDescription.lower()
                result = SequenceMatcher(None, data, itemDescription).ratio()
                if (result >= 1):
                    result_data.append([Member_number,itemDescription,Quantity],)
                    total_quantity = total_quantity + (int(Quantity))
        #             result = result + 1

        #             mm.insert_query("insert into search_details values('"+str(Member_number)+"','"+str(itemDescription)+"','"+str(Quantity)+"')")
        # items=mm.select_direct_query("select * from search_details")
        return render_template('manager_search_product1.html',items=result_data,total_quantity=total_quantity)
    return render_template('manager_search_product.html')

@app.route("/employee_login",methods = ['GET', 'POST'])
def employee_login():
    msg=None
    if request.method == 'POST':
        n = request.form['uname']
        g = request.form['pass']
        n1=str(n)
        g1=str(g)

        q=("SELECT * from employee_details where username='" + n1 + "' and password='" + str(g) + "'")
        data=mm.select_direct_query(q)
        if data==0:
            return render_template('employee.html',error=msg)
        else:
            msg='Success'
            session['employee'] =n
            return render_template('employee_home.html',sid=n)
    return render_template('employee.html',error=msg)

@app.route("/employee_home")
def employee_home():
    return render_template('employee_home.html')


@app.route("/employee_add_sales", methods=['GET', 'POST'])
def employee_add_sales():
    employee=session['employee']
    if request.method == 'POST':
        invoice_no = request.form['invoice_no']
        customer_id = request.form['customer_id']
        contact = request.form['contact']
        product = request.form['product']
        price = request.form['price']
        quantity = request.form['quantity']
        total = request.form['total']
        maxin = mm.find_max_id("sales_details")
        qq = "insert into sales_details values('" + str(maxin) + "','" + str(employee) + "','" + str(invoice_no) + "','" + str(
            customer_id) + "','" + str(contact) + "','" + str(product) + "','" + str(price) + "','" + str(quantity) + "','" + str(total) + "','0','0')"
        result = mm.insert_query(qq)

        if (result == 1):
            return render_template('employee_add_sales.html', msg="Success")
        else:
            return render_template('employee_add_sales.html')

    return render_template('employee_add_sales.html')


@app.route("/employee_view_sales",methods = ['GET', 'POST'])
def employee_view_sales():
    employee=session['employee']
    q=("SELECT employee,invoice_no,customer_id,product,price,quantity,total from sales_details where employee='" + str(employee) + "'")
    data=mm.select_direct_query(q)
    return render_template('employee_view_sales.html',items=data)





@app.route("/manager_total_sales",methods = ['GET', 'POST'])
def manager_total_sales():

    q=("SELECT employee,invoice_no,customer_id,product,price,quantity,total from sales_details")
    data=mm.select_direct_query(q)
    return render_template('manager_total_sales.html',items=data)



@app.route("/admin_sales_track")
def admin_sales_track():
    ra= csv_data_result.ar_csv()
    ra.read_dataset_result()
    items=mm.select_direct_query("select * from  search_result order by count DESC")
    return render_template('admin_sales_track.html',items=items)

@app.route("/manager_customer_behaviouor")
def manager_customer_behaviouor():
    ra= csv_data_result.ar_csv()
    ra.customer_behaviour()
    items=mm.select_direct_query("select * from  search_result1")
    return render_template('manager_customer_behaviouor.html',items=items)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

