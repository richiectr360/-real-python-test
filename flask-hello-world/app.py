#Flask Hello World

#Import the flask class from the flask package
from flask import Flask

#Create the application object
app = Flask(__name__)

#Use the decorator pattern to
#Link the view function to a url
#You can access the web in 2 ways with nth or /hello
@app.route("/")
@app.route("/hello")

#define the view using a function, which returns a string
def hello_world():
	return "Hello, World!"


#Start the development server using the eun() method
if __name__ == "__main__":
	app.run()


