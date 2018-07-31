# app.py is de file die naar everything else leid.
# STAP 1: Flask openen. Na import Flask met hoofdletter!
# STAP 2: ook render_template importen
from flask import Flask, render_template
from data import Articles

# Creating an instance of the flask class
# __name__ is placeholder for the current module (in this case app.py)
app = Flask(__name__)

Articles = Articles()

# route for 'index'
@app.route('/')
# STAP 2: hier definen welke template je wil oproepen. (html template)
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/articles')
def articles():
	return render_template('articles.html',articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
	return render_template('article.html',id=id)

# Checken of de __name__ value gelijk is aan __main__. 
# Als dat zo is zal het script ge-execute worden.
# Werk in Debug mode. 
# Op deze manier moet je niet altijd de local server heropstarten.
if __name__ == '__main__':
	app.run(debug=True)