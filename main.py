from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html")

@app.route('/<name>')
def get_page(name):
    return render_template(f"{name}")


if __name__ == "__main__":
    app.run(debug=True)