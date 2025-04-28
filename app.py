from flask import Flask, render_template, request, redirect, send_from_directory, flash
from flask_mail import Mail, Message
import os

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
            recipients=["kabilansiva609@gmail.com"],  # Where the email will be sent
            body=f"From: {name} <{email}>\n\nMessage:\n{message}"
        )
        mail.send(msg)
        flash("✅ Your message was sent successfully!", "success")
    except Exception as e:
        print(f"Error: {e}")
        flash("❌ Failed to send message. Please try again later.", "error")
    return redirect("/")

# Ensure the static directory path
static_folder = os.path.join(os.getcwd(), 'static')

# Resume download route
@app.route("/Resume.pdf")
def resume():
    try:
        return send_from_directory(
            static_folder,
            "Resume.pdf",
            as_attachment=True,
            mimetype="application/pdf"
        )
    except Exception as e:
        flash("❌ Failed to download Resume. Please try again later.", "error")
        print(f"Error: {e}")
        return redirect("/")
        
if __name__ == "__main__":
    app.run(debug=True)
