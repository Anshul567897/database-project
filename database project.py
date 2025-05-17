import mysql.connector

class ProductDatabase:
    def __init__(self, host, user, password, database, port):
        try:
            self.mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
            )
            self.mycursor = self.mydb.cursor()
            print("Database connected")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.mydb = None

    def add(self):
        try:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            sql = "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)"
            val = (name, price, stock)

            self.mycursor.execute(sql, val)
            self.mydb.commit()
            print(self.mycursor.rowcount, "record inserted")
       
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
    
    def update(self):
        try:
            productid = int(input("Enter the product ID "))

            print("which field do you want to modify")
            print("1. Product name")
            print("2. Product price")
            print("3. Product stock")
            d = int(input("Enter your choice "))
            
            if d == 1:
                new_name = input("Enter new product name: ")
                sql = "UPDATE products SET name = %s WHERE id = %s"
                val = (new_name, productid)
                self.mycursor.execute(sql, val)
                self.mydb.commit()
                print(self.mycursor.rowcount, "record updated with new name.")
            
            elif d == 2:
                new_price = float(input("Enter new product price: "))
                sql = "UPDATE products SET price = %s WHERE id = %s"
                val = (new_price, productid)
                self.mycursor.execute(sql, val)
                self.mydb.commit()
                print(self.mycursor.rowcount, "record updated with new price.")
            
            elif d == 3:
                new_stock = int(input("Enter new product stock: "))
                sql = "UPDATE products SET stock = %s WHERE id = %s"
                val = (new_stock, productid)
                self.mycursor.execute(sql, val)
                self.mydb.commit()
                print(self.mycursor.rowcount, "record updated with new stock.")
            
            else:
                print("Invalid choice. No changes made.")
        
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
        
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            print(self.mycursor.rowcount, "record updated")
        
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")

    def delete(self):
        try:
            productid = int(input('Enter product ID to delete: '))
            sql = "DELETE FROM products WHERE id = %s"
            val = (productid,)  
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            print(self.mycursor.rowcount, "record deleted")
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")

    def modify(self):
        try:
            print("Which column would you like to modify?")
            print("1. Modify column data type")
            print("2. Modify column name")
            print("3. Add or change constraints")
        
            choice = int(input("Enter your choice  "))
        
            if choice == 1:
                column = input("Enter column name to modify (e.g., price): ")
                n_type = input(f"Enter the new data type for {column}: ")
                
                sql = "ALTER TABLE products MODIFY COLUMN %s %s;"
                val = (column, n_type)
                self.mycursor.execute(sql,val)
                self.mydb.commit()
                print("data type changed")
        
            elif choice == 2:
                o_name = input("Enter the current column name: ")
                n_name = input(f"Enter the new name for column ")
                sql = "ALTER TABLE products CHANGE %s %s VARCHAR(255);"
                val = (o_name, n_name)
                self.mycursor.execute(sql,val)
                self.mydb.commit()
                print('renamed')
        
            elif choice == 3:
                column = input("Enter the column name ")
                constraint = input("Enter the constraint  ")
            
                sql = "ALTER TABLE products MODIFY COLUMN %s VARCHAR(255) %s;"
                val = (column, constraint)
                self.mycursor.execute(sql,val)
                self.mydb.commit()
                print('constraint modified')
        
            else:
                print("Invalid choice")
        
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
            
    def search(self):
        try:
            name = input("Enter product name to search: ")
            sql = "SELECT * FROM products WHERE name = %s"
            val = (name,)
            self.mycursor.execute(sql, val)
            results = self.mycursor.fetchall()

            if results:
                for row in results:
                    print('Record found:', row)
            else:
                print('No records found')
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
    
    def menu(self):
        while True:
            print("\n1. Add product")
            print("2. Update product")
            print("3. Delete product")
            print("4. Modify product")
            print("5. Search product")
            print("6. Exit")    

            try:
                a = int(input("Enter your choice: "))
                
                if a == 1:
                    self.add()
                elif a == 2:
                    self.update()
                elif a == 3:
                    self.delete()
                elif a == 4:
                    self.modify()
                elif a == 5:
                    self.search()
                elif a == 6:
                    self.mycursor.close()
                    print('Now exiting')
                    break
                else:
                    print("Invalid choice. Please try again.")
           
            except mysql.connector.Error as err:
                print(f"Database Error: {err}")
           


db = ProductDatabase(host="localhost", user="root", password="Lokeshh@7869", database="product_info", port=3345)

db.menu()