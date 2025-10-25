from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    files = request.files.getlist("files")
    for file in files:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return "Files uploaded successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
