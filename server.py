from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'akfnbj4fnsdv;lkndfv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def p_submit():
    session['f_name'] = request.form['f_name']
    session['l_name'] = request.form['l_name']
    session['current_stack'] = request.form['current_stack']
    return redirect('/result')

@app.route('/result')
def r_result():
    return render_template('result.html', f_name = session['f_name'], l_name = session['l_name'], stack = session['current_stack'])

if __name__ == '__main__':
    app.run(debug = True)