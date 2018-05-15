import requests
from flask import Flask, request

app = Flask(__name__)
curl_response = "Your cuddle partner curls back."
browser_response = "Cuddles!"

@app.route("/")
def main():
    """Return cuddles."""
    if request.headers.get('User-Agent').startswith("curl"):
        return curl_response
    
    return browser_response

@app.route("/<str:sub>")
def cuddle(sub):
    """Return cuddles from sub."""
    if request.headers.get('User-Agent').startswith("curl"):
        return "{} curls up in your cuddles.".format(sub)
    
    return "{} cuddles you.".format(sub)


if __name__ == "__main__":
    app.run()

