from flask import (
    Flask,
    send_file,
    request,
    render_template,
    redirect,
    url_for,
    session,
    flash,
)
import logging
import mysql.connector
from datetime import datetime
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
logging.basicConfig(level=logging.INFO)


USERNAME = ""
PASSWORD = ""

db_config = {
    "host": "",
    "user": "",
    "password": "",
    "database": "",
    "port": ,
}



@app.route("/track_open", methods=["GET"])
def track_open():
    email = request.args.get("email")
    logging.info(f"Email opened by: {email}")

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO email_opens (email, timestamp) VALUES (%s, %s)", (email, timestamp)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return send_file("static/pixel.png", mimetype="image/png")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            session["logged_in"] = True
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password", "danger")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT email, MAX(timestamp) AS last_viewed, COUNT(*) AS view_count
        FROM email_opens
        GROUP BY email
        ORDER BY last_viewed DESC
    """
    )
    opens = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("dashboard.html", opens=opens)



@app.route("/")
def index():
    return "Email Tracking Service is Running!"



@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
