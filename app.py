from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import webbrowser
from mysql.connector import Error

app = Flask(__name__)

# Insert function
def insert_record(table_name, values):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='inv_manage',
            user='root',
            password='root'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            sql_insert_query = ""
            if table_name == 'brands':
                sql_insert_query = "INSERT INTO brands(bid,bname) VALUES (%s, %s)"
            elif table_name == 'inv_user':
                sql_insert_query = "INSERT INTO inv_user(user_id,user_name,user_password,last_login,user_type) VALUES (%s, %s, %s, %s, %s)"
            elif table_name == 'categories':
                sql_insert_query = "INSERT INTO categories(cid,category_name) VALUES (%s, %s)"
            elif table_name == 'customer_cart':
                sql_insert_query = "INSERT INTO customer_cart(cust_id,user_name,mobno) VALUES (%s, %s, %s)"
            elif table_name == 'select_product':
                sql_insert_query = "INSERT INTO select_product(cust_id,pid,quantity) VALUES (%s, %s, %s)"
            elif table_name == 'transactions':
                sql_insert_query = "INSERT INTO transactions(id,total_amount,paid,due,gst,discount,payment_method,cart_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            elif table_name == 'invoice':
                sql_insert_query = "INSERT INTO invoice(item_no,product_name,quantity,net_price,transaction_id) VALUES (%s, %s, %s, %s, %s)"
            elif table_name == 'product':
                sql_insert_query = "INSERT INTO product(pid,cid,bid,sid,pname,p_stock,price,added_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            elif table_name == 'stores':
                sql_insert_query = "INSERT INTO stores(sid,sname,address,mobno) VALUES (%s, %s, %s, %s)"
            elif table_name == 'provides':
                sql_insert_query = "INSERT INTO provides(bid, sid, discount) VALUES (%s, %s, %s)"

            cursor.execute(sql_insert_query, values)
            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Update function
def update_record(table_name, values):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='inv_manage',
            user='root',
            password='root'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # sql_update_query = ""
            if table_name == 'brands':
                sql_update_query = "UPDATE brands SET bname = %s WHERE bid = %s"
            elif table_name == 'inv_user':
                sql_update_query = "UPDATE inv_user SET user_name = %s WHERE user_id = %s"
            elif table_name == 'categories':
                sql_update_query = "UPDATE categories SET category_name = %s WHERE cid = %s"
            elif table_name == 'customer_cart':
                sql_update_query = "UPDATE customer_cart SET user_name = %s, mobno = %s WHERE cust_id = %s"
            elif table_name == 'select_product':
                sql_update_query = "UPDATE select_product SET quantity = %s WHERE cust_id = %s AND pid = %s"
            elif table_name == 'transactions':
                sql_update_query = "UPDATE transactions SET total_amount = %s, paid = %s, due = %s, gst = %s, discount = %s, payment_method = %s, cart_id = %s WHERE id = %s"
            elif table_name == 'invoice':
                sql_update_query = "UPDATE invoice SET item_no = %s, product_name = %s, quantity = %s, net_price = %s WHERE transaction_id = %s"
            elif table_name == 'product':
                sql_update_query = "UPDATE product SET cid = %s, bid = %s, sid = %s, pname = %s, p_stock = %s, price = %s, added_date = %s WHERE pid = %s"
            elif table_name == 'stores':
                sql_update_query = "UPDATE stores SET sname = %s, address = %s, mobno = %s WHERE sid = %s"
            elif table_name == 'provides':
                sql_update_query = "UPDATE provides SET discount = %s WHERE bid = %s AND sid = %s"

            cursor.execute(sql_update_query, values)
            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Select function
def select_records(table_name):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='inv_manage',
            user='root',
            password='root'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            sql_select_query = ""
            if table_name == 'brands':
                sql_select_query = "SELECT * FROM brands"
            elif table_name == 'inv_user':
                sql_select_query = "SELECT * FROM inv_user"
            elif table_name == 'categories':
                sql_select_query = "SELECT * FROM categories"
            elif table_name == 'customer_cart':
                sql_select_query = "SELECT * FROM customer_cart"
            elif table_name == 'select_product':
                sql_select_query = "SELECT * FROM select_product"
            elif table_name == 'transactions':
                sql_select_query = "SELECT * FROM transactions"
            elif table_name == 'invoice':
                sql_select_query = "SELECT * FROM invoice"
            elif table_name == 'product':
                sql_select_query = "SELECT * FROM product"
            elif table_name == 'stores':
                sql_select_query = "SELECT * FROM stores"
            elif table_name == 'provides':
                sql_select_query = "SELECT * FROM provides"

            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            return records

    except Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
  
def delete_records(table_name,record_id):
    try:
            connection = mysql.connector.connect(
            host='localhost',
            database='inv_manage',
            user='root',
            password='root'
            )
            if connection.is_connected():
                cursor = connection.cursor()
                if table_name == 'brands':
                    sql_delete_query = "DELETE FROM brands WHERE bid = %s"
                elif table_name == 'inv_user':
                    sql_delete_query = "DELETE FROM inv_user WHERE user_id = %s"
                elif table_name == 'categories':
                    sql_delete_query = "DELETE FROM categories WHERE cid = %s"
                elif table_name == 'customer_cart':
                    sql_delete_query = "DELETE FROM customer_cart WHERE cust_id = %s"
                elif table_name == 'select_product':
                    sql_delete_query = "DELETE FROM select_product WHERE cust_id = %s AND pid = %s"
                elif table_name == 'transactions':
                    sql_delete_query = "DELETE FROM transactions WHERE id = %s"
                elif table_name == 'invoice':
                    sql_delete_query = "DELETE FROM invoice WHERE transaction_id = %s"
                elif table_name == 'product':
                    sql_delete_query = "DELETE FROM product WHERE pid = %s"
                elif table_name == 'stores':
                    sql_delete_query = "DELETE FROM stores WHERE sid = %s"
                elif table_name == 'provides':
                    sql_delete_query = "DELETE FROM provides WHERE bid = %s AND sid = %s"

                cursor.execute(sql_delete_query, (record_id,))
                connection.commit()
    except Error as e:
            print("Error while connecting to MySQL:", e)
    finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return redirect(url_for('index'))          
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        table_name = request.form['table_name']
        values = tuple(request.form['values'].split(','))
        insert_record(table_name, values)
        return redirect(url_for('index'))
    return render_template('insert.html')

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        table_name = request.form['table_name']
        values = tuple(request.form['values'].split(','))
        update_record(table_name, values)
        return redirect(url_for('index'))
    return render_template('update.html')

@app.route('/select', methods=['GET', 'POST'])
def select():
    records = None
    if request.method == 'POST':
        table_name = request.form['table_name']
        records = select_records(table_name)
    return render_template('select.html', records=records)

@app.route('/delete', methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        table_name = request.form['table_name']
        record_id = request.form['record_id']
        delete_records(table_name,record_id)
    return render_template('delete.html')
        
webbrowser.open('http://127.0.0.1:5000')

if __name__ == '__main__':
    app.run(debug=True)
