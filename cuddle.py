import requests
from flask import Flask, request

app = Flask(__name__)
curl_response = "Your cuddle partner curls back."
browser_response = "Cuddles!"
browser_url_script = "<script>history.replaceState({}, '', '/');</script>"

@app.route("/")
def main():
    """Return cuddles."""
    if request.headers.get("User-Agent").startswith("curl"):
        return curl_response
    
    return browser_response

@app.route("/<string:sub>")
def handle_sub(sub):
    """Return cuddles from sub."""
    curl = False

    if request.headers.get("User-Agent").startswith("curl"):
        curl = True

    if sub == "www":
        return cuddle(None, curl) + browser_url_script
    return cuddle(sub, curl)

def cuddle(sub, curl):
    """Given string and boolean, return cuddle string."""
    if not sub:
        if not curl:
            return browser_response
        return curl_response
    
    if not curl:
        return "{} cuddles back.".format(sub)
    return "{} curls up in your cuddles.".format(sub)

if __name__ == "__main__":
    app.run()

