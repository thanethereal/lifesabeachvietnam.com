from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/beach_bar_restaurant')
def beach_bar_restaurant():
    return render_template('beach_bar_restaurant.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/accomodations')
def accomodations():
    return render_template('accomodations.html')

@app.route('/gettinghere')
def gettinghere():
    return render_template('gettinghere.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000)
