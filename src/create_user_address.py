import json
import mysqlutility

def create_user_address(event):
    body = json.loads(event["body"])
    userId =  body.get('userId', "")
    address = body.get('address', "")
    cnx = mysqlutility.get_connection()
    cursor = cnx.cursor()

    # Check if item exists
    query = ("SELECT address FROM Address "
            "WHERE address = %s")
    cursor.execute(query, (address,))

    result = {}
    statusCode = 200
    itemFound = False
    for (address) in cursor:
        itemFound = True
        break

    if itemFound:
        result["message"] = "Address already exists!"
        cursor.close()
        mysqlutility.close_connection(cnx)
        return {
        "statusCode": 300,
        "body": json.dumps(result),
        }

    # Check if user id is valid
    query = ("SELECT name FROM Users "
            "WHERE id = %s")
    cursor.execute(query, (userId,))

    result = {}
    statusCode = 200
    itemFound = False
    for (name) in cursor:
        itemFound = True
        break

    if not itemFound:
        statusCode = 404
        result["message"] = "User Id not found"
        cursor.close()
        mysqlutility.close_connection(cnx)
        return {
        "statusCode": statusCode,
        "body": json.dumps(result),
        }

    # If item not exists and user Id valid then INSERT Item.
    cnx.autocommit = False
    # Create the new Address
    sql_insert_query = "INSERT INTO Address VALUES( %s, 0.0, 0.0, 0.0);"
    cursor.execute(sql_insert_query, (address, ))

    # Create the relationship between user and address 
    sql_insert_query = "INSERT INTO User_Address VALUES(default, %s, %s);"
    cursor.execute(sql_insert_query, (userId, address))
    print("Record Updated successfully.")

    # Commit your changes
    cnx.commit()
    cursor.close()
    mysqlutility.close_connection(cnx)
    statusCode = 200
    result["message"] = "Address added successfully"
    return {
        "statusCode": statusCode,
        "body": json.dumps(result),
    }