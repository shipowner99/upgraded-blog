from flask import Flask, render_template, request
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c30ea4f6d9c5343811cb")
data = response.json()


@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=data)

@app.route('/about')
def about():
    return render_template("about.html", posts=data)

@app.route('/contact')
def contact():
    return render_template("contact.html", posts=data)

@app.route('/post/<int:num>')
def post(num):
    return render_template("post.html", number=num, posts=data)

@app.route('/submit', methods=["POST"])
def receive_data():
    data = request.form
    print(data["username"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])

    return "<h1>Successfully sent your message</h1>"

if __name__ == "__main__":
    app.run(debug=True)