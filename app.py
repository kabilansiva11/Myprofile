from flask import Flask, render_template, request, redirect, send_from_directory, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Needed for flash messages

# Flask-Mail configuration
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "kabilansiva609@gmail.com"        # ✅ Replace with your Gmail
app.config["MAIL_PASSWORD"] = "rvpz xtht ggpz zmdb"           # ✅ Replace with your Gmail App Password
app.config["MAIL_DEFAULT_SENDER"] = "kabilansiva609@gmail.com" 

mail = Mail(app)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Contact form handler
@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    try:
        msg = Message(
            subject=f"New Contact Message from {name}",
            recipients=["kabilansiva609@gmail.com"],  # ✅ Where to receive the message
            body=f"From: {name} <{email}>\n\nMessage:\n{message}"
        )
        mail.send(msg)
        flash("✅ Your message was sent successfully!", "success")
    except Exception as e:
        print(f"Error: {e}")
        flash("❌ Failed to send message. Please try again later.", "error")
    return redirect("/")

# Resume download route
@app.route("/resume.pdf")
def resume():
    return send_from_directory(".", "resume.pdf")

if __name__ == "__main__":
    app.run(debug=True)
