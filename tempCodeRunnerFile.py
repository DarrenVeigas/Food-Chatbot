import mysql.connector
con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="adis",
        database="pandeyji_eatery",
        port=3305
    )
def get_order_status(order_id):
    
    if con.is_connected():
        cursor=con.cursor()
        query="SELECT STATUS FROM ORDER_TRACKING WHERE ORDER_ID = %s"
        cursor.execute(query, (order_id,))
        result=cursor.fetchone()
        cursor.close()
        if result is not None:
            return result
        else:
            return None
def get_next_order_id():

    if con.is_connected():

        cursor = con.cursor()

        # Executing the SQL query to get the next available order_id
        query = "SELECT MAX(order_id) FROM orders"
        cursor.execute(query)

        # Fetching the result
        result = cursor.fetchone()[0]

        # Closing the cursor
        cursor.close()

        # Returning the next available order_id
        if result is None:
            return 1
        else:
            return result + 1
    else:
        print('no')
def insert_order_item(food_item, quantity, order_id):

    if con.is_connected():
    
        try:
            cursor = con.cursor()
            # Calling the stored procedure
            cursor.callproc('insert_order_item', (food_item, quantity, order_id))
            # Committing the changes
            con.commit()
            # Closing the cursor
            cursor.close()
            print("Order item inserted successfully!")
            return 1

        except mysql.connector.Error as err:
            print(f"Error inserting order item: {err}")

            # Rollback changes if necessary
            con.rollback()

            return -1

        except Exception as e:
            print(f"An error occurred: {e}")
            # Rollback changes if necessary
            con.rollback()

            return -1

# Function to insert a record into the order_tracking table
def insert_order_tracking(order_id, status):
    if con.is_connected():

        cursor = con.cursor()

        # Inserting the record into the order_tracking table
        insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
        cursor.execute(insert_query, (order_id, status))

        # Committing the changes
        con.commit()

        # Closing the cursor
        cursor.close()
def get_total_order_price(order_id):
    if con.is_connected():

        cursor = con.cursor()

        # Executing the SQL query to get the total order price
        query = f"SELECT get_total_order_price({order_id})"
        cursor.execute(query)

        # Fetching the result
        result = cursor.fetchone()[0]

        # Closing the cursor
        cursor.close()

        return result

con.close()
