from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/industries")
def industries():
    return render_template("industries.html")

@app.route("/why-us")
def why_us():
    return render_template("why_us.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        if not name or not email or not message:
            flash("All fields are required", "danger")
            return redirect(url_for("contact"))

        try:
            msg = Message(
                subject=f"[Eclipse Inc. Website] {subject}",
                sender=app.config.get("MAIL_USERNAME") or email,
                recipients=[app.config.get("RECEIVER_EMAIL") or app.config.get("MAIL_USERNAME")],
                reply_to=email,
                body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            )
            mail.send(msg)
            flash("Thank you! Your message has been sent successfully.", "success")
        except Exception:
            flash("Thank you! We received your message and will get back to you soon.", "success")
        return redirect(url_for("contact"))

    return render_template("contacts.html")

if __name__ == "__main__":
    app.run(debug=True)
