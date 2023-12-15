from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from core.autocorrectTBFO import turing

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
   if request.method == 'POST':
        result = []
        input_string = request.form['input_text']
        print(input_string)
        input_string = input_string.split(" ")
        kata_terkoreksi = ""
        res = []
        for kata in input_string :
            if kata != "," and kata!= " " and kata!="":
                res =  turing(kata.lower())
                kata_terkoreksi += res[0] + " "
                result.append(res[1])
        return jsonify({'hasil': kata_terkoreksi, 'proses':result})
     
@app.route('/gambar/<path:filename>')
def serve_image(filename):
    return send_from_directory(os.path.join('gambar'), filename)

if __name__ == '__main__':
   app.run(debug=True)