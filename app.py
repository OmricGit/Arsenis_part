from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/HomePage')
@app.route('/Home')
@app.route('/')
def hello_func():  # put application's code here
    found = True
    if found:
        name = 'Omri'
        else
        name = None
 return render_template('index.html', name='Omri', second_name = 'Canaan')
@app.route('/about', methods=['GET','POST'])
def about_func():
    # TODO
    # Do Something With dB
    print('I am in About')
    # return redirect(url_for('catalog_func'))
    return render_template('about.html',
                           uni='BGU'
                           profile={'name': 'Omri',
                                    'second_name': 'Canaan',
                                    'Middle_name': 'null'},
                           degrees={'BSc'},
                           Hobbies={'programming','hiking','football'}
    )
@app.route('/catalog')
def catalog_func():
    #return 'Welome to catalouge page'
    return render_template('catalog.html', color='green')

if __name__ == '__main__':
    app.run(debug=True)
