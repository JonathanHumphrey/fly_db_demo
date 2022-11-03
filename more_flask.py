import flask

app = flask.Flask(__name__)
app.secret_key = "da2708a62d9fc4426cb6bff744f8af3bca85d9862dadf3c70cfb79aceeb7b02b"


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/handle_form", methods=["POST"])
def handle_txst_id_submission():
    form_data = flask.request.form
    print(f"FORM DATA: {form_data}")
    txst_id = form_data["txst_id"]
    if txst_id == "laithh":
        return flask.redirect(flask.url_for("welcome_to_the_matrix"))
    else:
        flask.flash("Invalid TXST ID. Please try again.")
        return flask.redirect(flask.url_for("index"))


@app.route("/welcome")
def welcome_to_the_matrix():
    return flask.render_template("welcome.html")


app.run(debug=True)
