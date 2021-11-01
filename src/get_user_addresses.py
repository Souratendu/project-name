import json
import mysqlutility

def get_user_addresses(event):
    cnx = mysqlutility.get_connection()
    cursor = cnx.cursor()

    query = ("SELECT userId, address from User_Address " +
            "WHERE userId = %s")

    userId = event.get("queryStringParameters", {}).get('userId', "")
    print(userId)
    cursor.execute(query, (userId,))

    result = {
        "userId": userId,
        "addresses": []
    }

    statusCode = 200
    for (userId, address) in cursor:
        result['addresses'].append(address)

    cursor.close()
    mysqlutility.close_connection(cnx)
    return {
        "statusCode": statusCode,
        "body": json.dumps(result),
    }   