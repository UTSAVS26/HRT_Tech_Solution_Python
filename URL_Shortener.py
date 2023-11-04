import string
import random
from flask import Flask, request, redirect

app = Flask(__name)
url_store = {}  # Store long and short URL mappings

def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/')
def home():
    return "Welcome to the URL Shortener Service!"

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form.get('long_url')
    if long_url:
        if long_url in url_store:
            short_url = url_store[long_url]
        else:
            short_url = generate_short_url()
            url_store[long_url] = short_url
        return f'Short URL: http://yourdomain/{short_url}'
    else:
        return 'Invalid URL input.'

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    if short_url in url_store.values():
        long_url = [url for url, short in url_store.items() if short == short_url][0]
        return redirect(long_url)
    else:
        return 'Short URL not found.'

if __name__ == '__main__':
    app.run(debug=True)
