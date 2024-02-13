from flask import Flask

app = Flask(__name__)
@app.route('/api/v1/users', methods=['GET'])
def hello():
    return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(debug=True)