from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    render_template('index.html', test_string="Hello World!")

if __name__ == "__main__":
    app.run(debug=True)