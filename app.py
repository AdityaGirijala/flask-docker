from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<center><h1>Hello Flask Application CI CD Pipeline</h1></center>"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=7000, debug=True)
