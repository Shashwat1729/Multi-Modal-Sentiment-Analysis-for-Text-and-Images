from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from model import analyze_text_sentiment, analyze_image_sentiment
from utils.file_parser import extract_text_from_file

app = Flask(__name__)

# Upload folder for images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or 'text' not in request.form:
        return redirect(request.url)
    
    file = request.files['file']
    user_text = request.form['text']
    
    if file.filename == '':
        return redirect(request.url)

    # Save the uploaded image file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    
    # Analyze sentiment for both text and image
    text_sentiment = analyze_text_sentiment(user_text)
    image_sentiment = analyze_image_sentiment(file_path)
    
    return render_template('index.html', text_sentiment=text_sentiment, image_sentiment=image_sentiment, filename=filename, user_text=user_text)

if __name__ == '__main__':
    app.run(debug=True)
