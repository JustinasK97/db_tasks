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
    query = "SELECT first_name, last_name FROM employees WHERE LENGTH(last_name) = 6"
    db_query(query)

def exercise7():
    query = "SELECT job_id, COUNT(*) FROM employees GROUP BY job_id"
    db_query(query)

# Antra dalis

def exercise8():
    query = """SELECT DISTINCT job_id FROM employees """

    db_query(query)


def exercise9():
    query = """SELECT SUM(salary) as total_salary FROM employees"""

    db_query(query)



def exercise10():
    query = """SELECT salary FROM employees
            ORDER by salary ASC
            LIMIT 1"""

    db_query(query)

def exercise11():
    query = """SELECT salary FROM employees
            ORDER by salary DESC
            LIMIT 1"""

    db_query(query)


def exercise12():
    query = """SELECT AVG(salary) as avg_salary, COUNT(employee_id) FROM employees
            WHERE department_id = 90"""

    db_query(query)


def exercise13():
    query = """SELECT MIN(salary), MAX(salary), SUM(salary), AVG(salary) FROM employees"""

    db_query(query)


def exercise14():
    query = """SELECT job_id, COUNT(*)  FROM employees
               GROUP BY job_id"""

    db_query(query)


def exercise15():
    query = """SELECT (MAX(salary) - MIN(salary)) as DIF_salary FROM employees"""

    db_query(query)


def exercise16():
    query = """SELECT department_id, SUM(salary) FROM employees
               GROUP BY department_id"""

    db_query(query)


def exercise17():
    query = """SELECT AVG(salary), job_id FROM employees
                WHERE NOT job_id = 'IT_PROG'
               GROUP BY job_id"""

    db_query(query)


def exercise18():
    query = """SELECT MIN(salary), manager_id, job_id FROM employees
                GROUP by manager_id
               """

    db_query(query)

# Trečia dalis

def names_view():
    query = """ CREATE VIEW IF NOT EXISTS names
                AS SELECT
                first_name,
                last_name
                FROM employees"""

    query_database(query)
    query_database("SELECT * FROM names")

def exercise19():
    query = """ SELECT first_name, last_name, salary
                FROM employees
                WHERE salary > (SELECT salary FROM employees WHERE last_name = 'Bull')"""

    query_database(query)


def exercise20():
    query = """ SELECT first_name, last_name, employee_id, manager_id, job_id
            FROM employees
            WHERE (employee_id IN (SELECT manager_id FROM employees))"""

    query_database(query)


def exercise21():
    query = """ SELECT first_name, last_name, salary
                FROM employees
                WHERE salary > (SELECT AVG(salary) FROM employees)"""

    query_database(query)


def exercise22():
    query = """ SELECT first_name, last_name, salary
            FROM employees
            WHERE salary = (SELECT min_salary FROM jobs
            WHERE employees.job_id = jobs.job_id)"""

    query_database(query)


def exercise23():
    query = """ SELECT first_name, last_name, salary
                FROM employees
                WHERE department_id IN (SELECT department_id FROM departments
                WHERE depart_name LIKE 'IT%' AND
                salary > (SELECT AVG(salary) from employees))"""

    query_database(query)


def exercise24():
    query = """ SELECT first_name, last_name, salary
                FROM employees
                WHERE salary IN (SELECT salary FROM employees ORDER BY salary desc limit 3)"""

    query_database(query)


def eercise25():
    query = """ SELECT first_name, last_name FROM employees
                WHERE manager_id IN (SELECT employee_id FROM employees
                WHERE department_id IN (SELECT department_id FROM departments
                WHERE location_id IN (SELECT location_id FROM locations WHERE country_id = 'US')))"""

    query_database(query)

