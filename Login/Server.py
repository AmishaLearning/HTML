from flask import Flask

app = Flask(__name__)

# Disable debug mode
app.debug = False

@app.route('/Portfolio')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)
