from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/HomePage')
@app.route('/Home')
@app.route('/')
def hello_func():  # put application's code here
    return render_template(index.html)
@app.route('/about', methods=['GET','POST'])
def about_func():
    # TODO
    # Do Something With dB
    print('I am in About')
    # return redirect(url_for('catalog_func'))
    return 'Welcome to About!'
@app.route('/catalog')
def catalog_func():
    return 'Welome to catalouge page'

if __name__ == '__main__':
    app.run(debug=True)
