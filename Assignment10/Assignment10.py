from flask import Flask, render_template, url_for, session, request, redirect, Blueprint, flash
# import mysql
import mysql.connector
import mysql
import requests


app = Flask(__name__)
app.secret_key = "123"

Assignment10 = Blueprint(
    'Assignment10',
    __name__,
    static_folder='static',
    static_url_path='/Assignment10',
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
    query = "select * from myflaskproject.users"
    query_result = interact_db(query=query, query_type='fetch')
    if session.get('messages'):
        msg = session['messages']
        session.pop('messages')
        return render_template('Assignment10.html', users=query_result, messages=msg)
    else:
        return render_template('Assignment10.html', users=query_result)


@Assignment10.route('/insert', methods=['GET', 'POST'])
def Insert():
    if request.method == 'POST':
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        Email = request.form['email']
        check_Mail = "SELECT Email FROM myflaskproject.users WHERE Email='%s';" % Email
        answer = interact_db(query=check_Mail, query_type='fetch')
        if len(answer) == 0:
            interact_db(query="insert into myflaskproject.users(username, firstname ,lastname, Email)\
                                 value ('%s', '%s', '%s','%s');" % (username, firstname, lastname, Email),
                        query_type='commit')
            session['messages'] = 'User has been added successfully'
            return redirect('/Assignment10')
        else:
            session['messages'] = 'Email address already exists, please enter new one'
            return redirect('/Assignment10')
    return render_template('Assignment10.html', req_method=request.method)


@Assignment10.route('/update', methods=['GET', 'POST'])
def Update():
    USER = request.form['username']
    NAME = request.form['firstname']
    FAM = request.form['lastname']
    MAIL = request.form['email']
    interact_db(query=" UPDATE myflaskproject.users SET username='%s',firstname='%s' ,lastname='%s' WHERE Email='%s';" % \
                      (USER, NAME, FAM, MAIL), query_type='commit')
    session['messages'] = 'User info has been updated successfully'
    return redirect('/Assignment10')


@Assignment10.route('/delete', methods=['POST'])
def Delete():
    userMail = request.form['email']
    check = "SELECT username FROM myflaskproject.users WHERE Email='%s';" % userMail
    ans = interact_db(query=check, query_type='fetch')
    if len(ans) > 0:
        query = "DELETE from myflaskproject.users where Email='%s';" % userMail
        interact_db(query=query, query_type='commit')
        session['messages'] = 'User has been deleted from DataBase'
        return redirect('/Assignment10')
    else:
        session['messages'] = 'Email address doesnt exists in DataBase'
        return redirect('/Assignment10')

    @app.route('/Assignment11')
    def Assignment11_func():  # put application's code here
        return render_template('Assignment11.html', non="non")

    def get_users(num):
        res = requests.get(f'https://reqres.in/api/users/{num}')
        res = res.json()
        return res

    @app.route('/Assignment11/users')
    def DB_to_json_func():  # put application's code here
        return_dict = {}
        query = "SELECT * FROM myflaskproject.users ;"
        answer = interact_db(query=query, query_type='fetch')
        for user in answer:
            return_dict[f'user_{user.id}'] = {
                'id': user.username,
                'name': user.firstname,
                'email': user.lastname,
                'password': user.Email
            }
        return render_template('Assignment11.html', answer=return_dict, non="non")

    @app.route('/Assignment11/outer_source', methods=['post'])
    def outer_source_func():
        if "frontend" in request.form:
            num = int(request.form['frontend'])
            return render_template('Assignment11.html', frontend=num)
        elif "backend" in request.form:
            num = int(request.form["backend"])
            user = get_users(num)
            return render_template('Assignment11.html', backend=user)
        else:
            return render_template('Assignment11.html')