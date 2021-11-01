import json
import mysqlutility

def get_address_details(event):
    cnx = mysqlutility.get_connection()
    cursor = cnx.cursor()

    query = ("SELECT address, balance_usd, received_usd, spent_usd FROM Address "
            "WHERE address = %s")

    address = event.get("queryStringParameters", {}).get('address', "")
    print(address)
    cursor.execute(query, (address,))

    result = {}
    statusCode = 200
    itemFound = False
    for (address, balance_usd, received_usd, spent_usd) in cursor:
        result['address'] = address
        result['balance'] = balance_usd
        result['received'] = received_usd
        result['spent'] = spent_usd
        itemFound = True
        break

    if not itemFound:
        statusCode = 404
        result["message"] = "Address not found"
    cursor.close()
    mysqlutility.close_connection(cnx)
    return {
        "statusCode": statusCode,
        "body": json.dumps(result),
    }