import requests
from flask import Flask

app = Flask(__name__)
curl_response = "Your cuddle partner curls back."


@app.route("/")
def main():
    """Return cuddles."""
    return curl_response


if __name__ == "__main__":
    app.run()

