from flask import Flask, redirect, url_for
from flask import render_template
app = Flask(__name__)


@app.route('/HomePage')
@app.route('/home')
@app.route('/')
def hello_func():
    return render_template('cv.html', name='Omri')

@app.route('/about')
def about_func():
    return render_template('about.html')

@app.route('/catalog')
def catalog_func():
    # return 'Welome to catalog page'
    return render_template('catalog.html')


@app.route('/Assignment8', methods=['GET', 'POST'])
def Assignment_func():
    name = 'Omri'
    second_name = 'Canaan'
    uni = 'BGU'
    return render_template('Assignment8.html',
                           profile={'name': 'Omri',
                                    'second_name': 'Canaan',
                                    'Middle_name': 'null'},
                           name=name,
                           university=uni,
                           second_name=second_name,
                           degreas=['BSc', 'MSc', 'Phd'],
                           hobbies=('Programming', 'football', 'sql'))

if __name__ == '__main__':
    app.run(debug=True)