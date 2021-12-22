import mysql.connector
from mysql.connector import connection


def interact_db(query, query_type: str):
    return_value = False
    connection - mysql.connector.connet(host='localhost',
                                        user= 'root',
                                        passwd='root',
                                        database='myflaskproject')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        reeturn_value = query_result

    connection.close()
    cursor.close()
    return reeturn_value

