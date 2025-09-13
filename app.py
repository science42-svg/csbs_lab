from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/about')
def about():
    return "This is the About page."

@app.route('/contact')
def contact():
    return "This is the Contact page."

@app.route('/user/<username>')
def user_profile(username):
    return f"Welcome, {username}!"

@app.route('/square/<int:number>')
def square(number):
    return f"The square of {number} is {number ** 2}"

if __name__ == '__main__':
    app.run(debug=True)