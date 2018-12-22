from flask import Flask
import new

app = Flask(__name__)

@app.route("/")
def home():
    return new
if __name__ == "__main__":
    app.run(debug=True)