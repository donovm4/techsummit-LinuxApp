"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from LinuxApp import app
import pyodbc

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

# def query_db_customers():
#     # Could potentially move some of the database connection outside to enhance overall speed of query function
#     connect_str = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=9.169.70.172,1433;DATABASE=MyAppDB;UID=SQLAdmin;PWD=P@55w0rd1234;Encrypt=no;TrustServerCertificate=yes;"
#     with pyodbc.connect(connect_str) as conn:
#         with conn.cursor() as cursor:
#             cursor.execute(
#                 "SELECT CustomerID, FirstName, LastName, Email FROM Customers"
#             )
#             # map column names to values
#             # cols = [col[0] for col in cursor.description]
#             # return [dict(zip(cols, row)) for row in cursor.fetchall()]

#             # simplified
#             customers = cursor.fetchall()
#             return customers

# @app.route('/customers')
# def customers():
#     customers = query_db_people()
#     return render_template('customers.html',
#                            title='MyAppDB',
#                            year=datetime.now().year,
#                            customers=customers,
#                            message='Let\'s query the Customers table of our database!'
#                            )

def query_db_people():
    # Could potentially move some of the database connection outside to enhance overall speed of query function
    connect_str = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=172.17.195.4,1433;DATABASE=AdventureWorksPTO;UID=appuser;PWD=StrongP@ssword123!;Encrypt=no;TrustServerCertificate=yes;"
    with pyodbc.connect(connect_str) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT Title, FirstName, MiddleName, LastName FROM Person.Person"
            )
            # map column names to values
            # cols = [col[0] for col in cursor.description]
            # return [dict(zip(cols, row)) for row in cursor.fetchall()]

            # simplified
            people = cursor.fetchall()
            return people

@app.route('/people')
def people():
    people = query_db_people()
    return render_template('people.html',
                           title='AdventureWorksPTO',
                           year=datetime.now().year,
                           people=people,
                           message='Let\'s query the Person.Person table of our database!'
                           )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )



