from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c30ea4f6d9c5343811cb")
data = response.json()
print(data)
@app.route('/')
def get_all_posts():
    return render_template("index.html")

@app.route('/<name>')
def get_page(name):
    return render_template(f"{name}")


if __name__ == "__main__":
    app.run(debug=True)