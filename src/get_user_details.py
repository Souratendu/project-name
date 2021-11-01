import json
import mysqlutility

def get_user_details(event):
    cnx = mysqlutility.get_connection()
    cursor = cnx.cursor()

    query = ("SELECT name, address, email FROM Users "
            "WHERE id = %s")

    id = event.get("queryStringParameters", {}).get('userId', "")
    print(id)
    cursor.execute(query, (id,))

    result = {}
    statusCode = 200
    itemFound = False
    for (name, address, email) in cursor:
        result['name'] = name
        result['address'] = address
        result['email'] = email
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