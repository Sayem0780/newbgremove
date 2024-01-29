from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Change the route decorator to accept a query parameter
@app.route('/bgremove', methods=['GET'])
def bgremove():
    # Get the image URL from the request.args dictionary
    image_url = request.args.get('image')
    # Download the image from the URL and convert it to bytes
    image_bytes = requests.get(image_url).content
    # Remove the background using rembg
    bgimg_bytes = remove(image_bytes)
    # Convert the bytes to a PIL image
    bgimg = Image.open(io.BytesIO(bgimg_bytes))
    # Save the image to a temporary file
    temp_file = io.BytesIO()
    bgimg.save(temp_file, format='PNG')
    # Return the file as a response
    temp_file.seek(0)
    return send_file(temp_file, mimetype='image/png')

