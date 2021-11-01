import json
import mysqlutility
import requests

def sync_addresses(event):
    body = json.loads(event["body"])
    address = body.get('address', "")

    cnx = mysqlutility.get_connection()
    cursor = cnx.cursor()

    # check if address exists
    query = ("SELECT address FROM Address "
            "WHERE address = %s")
    cursor.execute(query, (address,))

    result = {}
    statusCode = 200
    itemFound = False
    for (address) in cursor:
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

    # If address found call blockchair API to get updated Address details.
    address = body.get('address', "")
    print("https://api.blockchair.com/bitcoin/dashboards/address/{}?key=A___SqwAVl2ueyKyjIS9dgdDOX8fThEy".format(address))
    response = requests.get("https://api.blockchair.com/bitcoin/dashboards/address/{}".format(address))
    balance = float(response.json()["data"][address]["address"]["balance_usd"])
    spent = float(response.json()["data"][address]["address"]["spent_usd"])
    received = float(response.json()["data"][address]["address"]["received_usd"])
    print("Balance: {}, Spent: {}, Received: {}, Address: {}")
    sql_update_query = "Update Address set balance_usd = %s, spent_usd = %s, received_usd = %s where address = %s"
    cursor.execute(sql_update_query, (balance, spent, received, address))
    cnx.commit()
    statusCode = 200
    result["message"] = "Successfully Synchronized address"
    cursor.close()
    mysqlutility.close_connection(cnx)
    return {
        "statusCode": statusCode,
        "body": json.dumps(result),
    }
