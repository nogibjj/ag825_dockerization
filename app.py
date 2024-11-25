from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def start_joke():
    return """
        <p>Knock, knock!</p>
        <form action="/whos-there" method="post">
            <button type="submit">Who's there?</button>
        </form>
    """


@app.route("/whos-there", methods=["POST"])
def whos_there():
    return """
        <p>Boo.</p>
        <form action="/boo-who" method="post">
            <button type="submit">Boo who?</button>
        </form>
    """


@app.route("/boo-who", methods=["POST"])
def boo_who():
    return """
        <p>Don't cry, it's just a joke! 😂</p>
        <a href="/">Start again</a>
    """


if __name__ == "__main__":
    app.run(debug=True)
