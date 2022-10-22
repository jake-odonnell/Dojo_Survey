from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'akfnbj4fnsdv;lkndfv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def p_submit():
    session['f_name'] = request.form['f_name']
    session['l_name'] = request.form['l_name']
    session['current_stack'] = request.form['current_stack']
    session['know'] = request.form.getlist('stack')
    print(request.form['stack'])
    return redirect('/result')

@app.route('/result')
def r_result():
    print(session['know'])
    return render_template('result.html', f_name = session['f_name'], l_name = session['l_name'], stack = session['current_stack'], stacks = session['know'])

if __name__ == '__main__':
    app.run(debug = True)