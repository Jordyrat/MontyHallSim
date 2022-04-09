import flask
import main

app = flask.Flask(__name__)

app.config["DEBUG"] = True


@app.route("/")
def home():
    values = main.getsuccessdata()
    return flask.render_template("graph.html", values=values)

if __name__ == "__main__":
    flask.app.run(debug=True)
