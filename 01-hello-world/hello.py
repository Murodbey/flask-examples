from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<!DOCTYPE html>
<html>
<head>
  <title>class</title>
</head>
<body style="background-color:powderblue;">
<h1 style="color:red;text-align:center">The content of the document...... </h1>
  <a href="https://evolvecyber.com">Visit Evolve Cyber!</a> <br />
  <p1><a href="https://google.com">Visit Google!</a></p1> <br />
  <a href="http://thecatapi.com"><img src="http://thecatapi.com/api/images/get?format=src&type=gif"></a>
  <a href="http://thecatapi.com"><img src="http://thecatapi.com/api/images/get?format=src&type=gif"></a>
  <a href="http://thecatapi.com"><img src="http://thecatapi.com/api/images/get?format=src&type=gif"></a>
  <a href="http://thecatapi.com"><img src="http://thecatapi.com/api/images/get?format=src&type=gif"></a> <br />
  <p1>This coool website is done with my students</p1>
  
  
  <address style="border: 10px solid Tomato;">
  Written by Evolve Cyber. <br>
    Visit us at: <br>
    Evolvecyber.com <br>
    5636 n Western ave <br>
    Chicago IL 60659 <br>
    </address>
</body>
</html>"

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, {0}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

