from flask import *
from commands import *

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/create',methods=['GET','POST'])
def creating():
	createf()
	return render_template('index.html')

@app.route('/list',methods=['GET','POST'])
def listing():
	listf()
	return render_template('index.html')

@app.route('/upload',methods=['GET','POST'])
def uploading():
	uploadf()
	return render_template('index.html')
	
@app.route('/download',methods=['GET','POST'])
def downloading():
	downloadf()
	return render_template('index.html')

@app.route('/delete',methods=['GET','POST'])
def deleting():
	deletef()
	return render_template('index.html')
	
app.run()
