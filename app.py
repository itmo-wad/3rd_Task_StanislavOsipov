import hashlib
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():    
    return render_template("index.html") 

	
@app.route('/cabinet',methods=['POST'])
def login():
	f = open('static/db/users.db','r')
	string=f.read()
	string=string.split(sep='\n')
	for i in range(len(string)):
		string[i]=string[i].split(sep=',')
	f.close
	user_name=request.form['user_name']
	user_password=request.form['user_password']
	user_password=hashlib.md5(user_password.encode()).hexdigest()
	for i in range(len(string)):
		if user_name==string[i][0] and user_password==string[i][1]:
			return render_template('cabinet.html',user_name=user_name)
	else:
		return render_template('index.html',error="Invalid login or password")

@app.route('/logout',methods=['POST'])
def logout():
	return render_template('index.html')

@app.route('/register')
def reg():
	return render_template('registration.html')

@app.route('/newuser',methods=['POST'])
def newuser():
	f = open('static/db/users.db','a')
	user_name=request.form['user_name']
	user_password=request.form['user_password']
	user_password=hashlib.md5(user_password.encode()).hexdigest()
	user_email=request.form['user_email']
	string=user_name+","+user_password+","+user_email
	f.write(string)
	f.write('\n')
	f.close
	return render_template('cabinet.html',user_name=user_name)
	
@app.errorhandler(405)
def page_not_found(e):
  return render_template('405.html')
	
if __name__ == "__main__":    
    app.run()
	