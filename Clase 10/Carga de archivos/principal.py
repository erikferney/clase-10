from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/upload')
def upload_file():
	return render_template('upload_file.html')

@app.route('/uploader', methods=['POST', 'GET'])
def uploader_file():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		data = [x.split(',') for x in open(f.filename).readlines()]
		return render_template('showall.html', rows=data)

if __name__ == '__main__':
	app.run(debug=True)