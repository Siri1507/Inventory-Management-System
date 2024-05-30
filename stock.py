import mysql.connector
from mysql.connector import Error

def check_stock(x):
    if x < 2:
        print('Stock is Less')
    else:
        print('Enough Stock')

def main():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='inv_manage',  
            user='root',            
            password='root'        
        )
        
        if connection.is_connected():
            b = int(input("Enter product ID: "))
            cursor = connection.cursor()
            cursor.execute("SELECT p_stock FROM product WHERE pid = %s", (b,))
            row = cursor.fetchone()

            if row:
                p_stock = row[0]
                check_stock(p_stock)
            else:
                print("Product ID not found")

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    main()
