import pandas as pd
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/matriz')
def matriz():
    # prueba fallida de subida del documento excel
    # xlsx_file=pd.ExcelFile('C:\\Users\\Adminpc\\Desktop\\pyton_web\\uploads\\27001.xlsx')
    # return xlsx_file.to_html()
    df = pd.read_excel( "C:\\Users\\Adminpc\\Desktop\\pyton_web\\uploads\\27001.xlsx" )
    return df.to_html()

@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error='Credenciales invalidad. Intente denuevo.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html',error=error)

@app.route('/upload')
def upload():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)