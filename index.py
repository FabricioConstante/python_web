import os
import glob, os.path
import pandas as pd
# import string
from flask import *
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['xlsx'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return render_template('upload_file.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/matriz')
def matriz():
    return render_template('matriz.html')

@app.route('/llamar_matriz')
def llamar_matriz():
    documento = "uploads/data.xlsx"
    ingresar_documento = pd.ExcelFile( documento )
    hojas = []
    for valor in ingresar_documento.sheet_names:
        hojas.append (valor)
            # for i 
        print(valor)
    print(len(hojas))
    print(ingresar_documento.sheet_names)
    lectura_del_documento = pd.read_excel( ingresar_documento , index_col=0, header=1,sheet_name='Personal')
    return lectura_del_documento.to_html()

# @app.route('/dropdown', methods=['GET'])
# def dropdown():
#     colours = ['Red', 'Blue', 'Black', 'Orange']
#     return render_template('test.html', colours=colours)

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