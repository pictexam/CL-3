from flask import Flask, render_template, request

app= Flask (__name__)

@app.route('/')
def fun():
	return render_template('index.html', msg="")
@app.route('/', methods=['POST'])
def check():
	a=checker(request.form['string'])
	return render_template('index.html', msg=a)

def checker(str1):
	with open('data.txt', 'r') as f:
		filedata=f.read()
	unwanted_char="!@#$%^&*():;,.'"
	for j in unwanted_char:
		filedata=filedata.replace(j, "")
		str1=str1.replace(j, "")
	a=filedata.split()
	b=str1.split()
	print "A" , a
	print "B" , b
	count=0
	for word in b:
		if word in a:
			count=count+1
	
	percent=str(float(count)/len(a)*100) + "%"
	return percent

app.run()
