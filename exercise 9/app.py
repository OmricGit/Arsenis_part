#import asyncio
import mysql, json
import mysql.connector
import requests
from flask import Flask, render_template, session, request, redirect, Blueprint, jsonify
from flask import jsonify

# import random
from interact_with_Db import interact_db

app = Flask(__name__)
app.secret_key = '123'

from Assignment10.Assignment10 import Assignment10
app.register_blueprint(Assignment10)

from Assignment11.Assignment11 import Assignment11
app.register_blueprint(Assignment11)

# Assignment10 = Blueprint(
#     'Assignment10',
#     __name__,
#     static_folder='static',
#     static_url_path='/Assignment10',
#     template_folder='templates'
# )

users = {"user1": {"First Name": "Omri","Last Name": "Canaan", "Email": "Omricanaan1@gmail.com", "Username": "Omric"},
         "user2": {"First Name": "Avi", "Last Name": "Nimni", "Email": "leolam8@gmail.com" , "Username": "Macabi"},
         "user3": {"First Name": "Elyakir", "Last Name": "Benzino", "Email": "Elyak@gmail.com", "Username": "elyak"},
         "user4": {"First Name": "Vladimir", "Last Name": "Putin", "Email": "Russia@walla.com","Username": "ussr"},
         "user5": {"First Name": "Bukayo", "Last Name": "Saka", "Email": "saka7@gmail.com","Username": "Lilchili"}
         }

@app.route('/HomePage')
@app.route('/home')
@app.route('/')
def hello_func():
    return render_template('cv.html', name='Omri')

@app.route('/Assignment9', methods=['GET', 'POST'])
def login_func():
    #session['username'] = ''
    #username=session['username'],
    if request.method == 'GET':
        if 'search_user' in request.args:
            search_user = request.args['search_user']
            return render_template('Assignment9.html', username=session['username']
                                                     , search_user=search_user
                                                     , users=users)
        return render_template('Assignment9.html', users=users)
    if request.method == 'POST':
        #DB
        username = request.form['username']
        Password = request.form['password']
        Password2 = request.form['password2']
        found = True
        if found:
            # session['username'] = username
            session['username'] = request.form['username']
            session['user_login'] = True
            return render_template('Assignment9.html', username=username, users=users)
        else:
            return render_template('Assignment9.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout_func():
    session['username'] = ''
    return render_template('cv.html')

@app.route('/db_users')
def get_user_func():
    query = 'select * from users'
    return users



# @app.route('/users')
# def users_func():
#     query = "select * from users"
#     query_result = interact_db(query=query, query_type='fetch')
#     # session['users'] = query_result
#     # return redirect(url_for('users_func'))
#     return render_template('users.html', users=query_result)

# @app.route('/insert_user', methods=['POST'])
# def insert_user_func():
#      name = request.form['name']
#      email = request.form['email']
#      password = request.form['password']
#
#      query = "Insert into users(name,email,password) VALUES ('%s', '%s','%s')" % (name,email,password)
#     interact_with_Db(query=query, query_type='commit')
#    return redirect('/users')
#
# @app.route('/delete_user', methods=['POST'])
# def delete_user_func():
#     user_d = request.form['id']
#     query = "DELETE FROM user where id='%s';" % user_id
#     interact_db(query,query_type='commit')
#     return redirect('/users')

@app.route('/about')
def about_func():
    return render_template('about.html')

@app.route('/catalog')
def catalog_func():
    # return 'Welcome to catalog page'
    return render_template('catalog.html')


@app.route('/Assignment8', methods=['GET', 'POST'])
def Assignment_func():
    name = 'Omri'
    second_name = 'Canaan'
    uni = 'BGU'
    FootballTeams=("Maccabi", "Barca", "Arsenal", "hapoel")
    return render_template('Assignment8.html',
                           profile={'name': 'Omri',
                                    'second_name': 'Canaan',
                                    'Middle_name': 'null'},
                           name=name,
                           university=uni,
                           second_name=second_name,
                           degrees=['BSc', 'MSc', 'Phd'],
                           hobbies=('Programming', 'football', 'sql','hiking'),
                           FootballTeams =FootballTeams )
@app.route('/req_frontend')
def front_func():
    return render_template('req_frontend')

# def main_2():
#     asyncio.run(async_gather())

if __name__ == '__main__':
    app.run(debug=True)

    Assignment10 = Blueprint(
        'Assignment10',
        __name__,
        static_folder='static',
        static_url_path='../Assignment10',
        template_folder='templates'
    )


    def interact_db(query, query_type: str):
        return_value = False
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='root',
                                             database='myflaskproject')
        cursor = connection.cursor(named_tuple=True)
        cursor.execute(query)

        if query_type == 'commit':
            connection.commit()
            return_value = True
        if query_type == 'fetch':
            query_result = cursor.fetchall()
            return_value = query_result

        connection.close()
        cursor.close()
        return return_value


@Assignment10.route('/Assignment10')
def users():
    usersTable = interact_db(query="select * from myflaskproject.users", query_type='fetch')
    if session.get('messages'):
        x = session['messages']
        session.pop('messages')
        return render_template('Assignment10.html', users=usersTable, messages=x)
    else:
        return render_template('Assignment10.html', users=usersTable)


# @Assignment10.route('/insert', methods=['GET', 'POST'])
# def insert():
#     if request.method == 'POST':
#         username = request.form['username']
#         firstname = request.form['firstname']
#         lastname = request.form['lastname']
#         Email = request.form['Email']
#         check_Email = "SELECT Email FROM myflaskproject.users WHERE Email='%s';" % email
#         answer = interact_db(query=check_Email, query_type='fetch')
#         if len(answer) == 0:
#             interact_db(query="insert into myflaskproject.users(username, firstname ,lastname, Email)\
#                                      value ('%s', '%s', '%s','%s');" % (username, firstname, lastname, email),
#                         query_type='commit')
#             session['messages'] = 'User has been added successfully'
#             return redirect('/Assignment10')
#         else:
#             session['messages'] = 'Email address already exists, please enter new one'
#             return redirect('/Assignment10')
#     return render_template('Assignment10.html', req_method=request.method)


@Assignment10.route('/update', methods=['GET', 'POST'])
def update():
    user = request.form['username']
    FN = request.form['firstname']
    LN = request.form['lastname']
    E = request.form['email']
    interact_db(
        query=" UPDATE myflaskproject.users SET username='%s',firstname='%s' ,lastname='%s' WHERE email='%s';" % \
              (user, FN, LN, E), query_type='commit')
    session['messages'] = 'User has been added successfully'
    return redirect('/Assignment10')


@Assignment10.route('/delete', methods=['POST'])
def deleteUsers():
    userEmail = request.form['Email']
    check = "SELECT username FROM myflaskproject.users WHERE Email='%s';" % userEmail
    answer = interact_db(query=check, query_type='fetch')
    if len(answer) > 0:
        query = "delete from myflaskproject.users where Email='%s';" % userEmail
        interact_db(query=query, query_type='commit')
        session['messages'] = 'User has been deleted from DataBase'
        return redirect('/Assignment10')
    else:
        session['messages'] = 'Email address doesnt exists in DataBase'
        return redirect('/Assignment10')

@app.route('/assignment11')
def assignment11_func():  # put application's code here
    return render_template('assignment11.html', non="non")

def get_users(num):
    res = requests.get(f'https://reqres.in/api/users/{num}')
    res = res.json()
    return res

@app.route('/assignment11/users')
def DB_to_json_func():  # put application's code here
    return_dict = {}
    query = "SELECT * FROM myflaskproject.users ;"
    answer = interact_db(query=query, query_type='fetch')
    for user in answer:
        return_dict[f'user_{user.id}'] = {
            'id': user.id,
            'username': user.username,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'email': user.email
        }
    return render_template('assignment11.html', answer=return_dict, non="non")

@app.route('/assignment11/outer_source',  methods=['post'])
def outer_source_func():
    if "frontend" in request.form:
        num = int(request.form['frontend'])
        return render_template('assignment11.html', frontend=num)
    elif "backend" in request.form:
        num = int(request.form["backend"])
        user = get_users(num)
        return render_template('assignment11.html', backend=user)
    else:
        return render_template('assignment11.html')



@app.route('/assignment12/restapi_users', defaults={'user_id': 1})
@app.route('/assignment12/restapi_users/<int:user_id>')
def get_users_json_func(user_id):
    query = 'SELECT * FROM myflaskproject.users where id=%s;' % user_id
    users = interact_db(query=query, query_type='fetch')
    if len(users) == 0:
        return_dict = {
            'status': 'failed',
            'message': 'user not found'
        }
    else:
        return_dict = {
            'status': 'success',
            f'id': users[0].id,
            'username': users[0].username,
            'firstname': users[0].firstname,
            'lastname': users[0].lastname,
            'email': users[0].email,
        }
    return jsonify(return_dict)