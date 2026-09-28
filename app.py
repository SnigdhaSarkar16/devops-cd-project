from flask import Flask, jsonify, render_template

app = Flask(__name__)


def add(a, b):
    return a + b


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/api/status")
def status():
    return jsonify(
        application="Flask Web App",
        version="1.0",
        ci_cd="GitHub Actions",
        testing="PyTest",
        container="Docker",
        status="running"
    )


@app.route("/add/<int:a>/<int:b>")
def add_route(a, b):
    return jsonify(result=add(a, b))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
