from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    product_class = request.form.get('productClass')
    alcohol_percent = request.form.get('alcoholPercent')
    net_volume = request.form.get('netVolume')
    bottled_by = request.form.get('bottledBy')
    file = request.files.get('fileUpload')

    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

    return f"Received {product_class}, {alcohol_percent}%, {net_volume}, {bottled_by}, file: {file.filename if file else 'None'}"

if __name__ == "__main__":
    app.run(debug=True)
