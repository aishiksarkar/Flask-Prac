# importing the required libraries
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

# initialising the flask app
app = Flask(__name__)

# Creating the upload folder
upload_folder = "uploads/"
if not os.path.exists(upload_folder):
   os.mkdir(upload_folder)

# Configuring the upload folder
app.config['UPLOAD_FOLDER'] = upload_folder

# configuring the allowed extensions
allowed_extensions = ['jpg', 'png', 'pdf']

def check_file_extension(filename):
    return filename.split('.')[-1] in allowed_extensions

# The path for uploading the file
@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/upload', methods = ['GET', 'POST'])
def uploadfile():
   if request.method == 'POST': # check if the method is post
      files = request.files.getlist('files') # get the file from the files object
      print(files)
      for f in files:
         print(f.filename)
         # Saving the file in the required destination
         if check_file_extension(f.filename):
            f.save(os.path.join(app.config['UPLOAD_FOLDER'] ,secure_filename(f.filename))) # this will secure the file

      return 'file uploaded successfully' # Display thsi message after uploading
		
if __name__ == '__main__':
   app.run() # running the flask app