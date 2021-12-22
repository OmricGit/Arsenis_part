from flask import Flask, redirect, url_for
from flask import render_template
from flask import session
from flask import request
# from interact_with_Db import interact_db

app = Flask(__name__)
app.secret_key = '1234'


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

if __name__ == '__main__':
    app.run(debug=True)