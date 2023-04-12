from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reverse_string', methods=['POST'])
def reverse_string():
    input_string = request.json['string']
    return {'reversed_string': input_string[::-1]}

if __name__ == '__main__':
    app.run()
