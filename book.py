from flask import Flask
app = Flask(__name__)

@app.route('/book')
def home():
    books = ["Harry potter", "Feluda", "crime and punishment", "Tempest", "merchant of venice"]
    return books

if __name__ == '__main__':
    app.run(debug=True)