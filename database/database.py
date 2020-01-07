import sqlite3

def open_connection():
    connection = sqlite3.connect("exercise.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection, cursor):
    connection.close()

def db_query(query, params=None):
    try:
        connection, cursor = open_connection()
        if params:
            cursor.execute(query)
            connection.commit()
        else:
            for i in cursor.execute(query):
                print(i)
    except sqlite3.DatabaseError as error:
       print(error)
    finally:
        close_connection(connection, cursor)

def exercise0():
    query = "SELECT * FROM employees"
    db_query(query)

def exercise1():
    query = "SELECT first_name, last_name, salary FROM employees WHERE salary NOT BETWEEN 10000 and 15000"
    db_query(query)

def exercise2():
    query = "SELECT first_name, last_name, department_id FROM employees ORDER BY department_id ASC LIMIT 100"
    db_query(query)

def exercise3():
    query = "SELECT first_name, last_name, salary, department_id FROM employees WHERE salary NOT BETWEEN 10000 and 15000 ORDER BY department_id ASC LIMIT 100"
    db_query(query)

def exercise4():
    query = "SELECT first_name FROM employees WHERE first_name LIKE '%b%c%'"
    db_query(query)


def exercise5():
    query = "SELECT last_name, job_id, salary FROM employees WHERE job_id LIKE 'PU%'"
    db_query(query)


def exercise6():
    query = "SELECT first_name, last_name FROM employees WHERE first_name = 6"
    db_query(query)

exercise6()