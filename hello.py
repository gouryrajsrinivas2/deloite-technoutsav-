from flask import Flask, render_template,request, redirect, Response
import random, json
import pickle
import numpy as np
from sklearn.externals import joblib

app = Flask(__name__)      
 
ip=open("srinivas",'rb')
m=pickle.load(ip)
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/submit')
def submit():
	return render_template('about-us.html')
def worker():
	# read json + reply
	data = request.get_json()
	print(data)

@app.route('/sub',methods=['POST'])
def fun():
	if request.method == 'POST':
		#data=request.form
		amount=float(request.form['amount'])
		oldbalanceorg=float(request.form['oldbalanceorg'])
		newbalanceorg=float(request.form['newbalanceorg'])
		oldbalancedest=float(request.form['oldbalancedest'])
		newbalancedest=float(request.form['newbalancedest'])
		k=[[amount,oldbalanceorg,newbalanceorg,oldbalancedest,newbalancedest]]
		pre=m.predict(k)
		print("debugging")
		print("debugging")
		print("debugging")
		print("debugging")
		print(pre)
		if pre==[0.]:
    			return "false"
		else:
    			return "true"
    						

	#	return(pre)
 
if __name__ == '__main__':
  app.run(debug=True)