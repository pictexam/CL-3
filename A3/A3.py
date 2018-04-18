from flask import *
from bitstring import BitArray

app=Flask(__name__)

@app.route('/')
def fun():
	return render_template('index.html')

@app.route('/',methods=['POST'])
def g():
	text1=int(request.form['text1'])
	text2=int(request.form['text2'])
	n,m=booth(text1,text2,8,8)
	return "Answer in binary: "+str(n)+"<br>Answer: "+str(m)

def booth(m,r,x,y):
	tot=x+y+1;
	mA=BitArray(int=m,length=tot)
	print mA
	A=mA<<(y+1)
	mA1=BitArray(int =-m,length=tot)
	B=mA1<<(y+1)
	P=BitArray(int=r,length=x)
	P.prepend(BitArray(int=0,length=y))
	P=P<<(1)
	for i in range(0,y):
		if(P[-2:]=='0b01'):
			P=BitArray(int=P.int+A.int,length=tot)
		elif(P[-2:]=='0b10'):
			P=BitArray(int=P.int+B.int,length=tot)
		P=BitArray(int=P.int>>(1),length=tot)
	P=P[:-1]
	return P.bin,P.int

app.run()