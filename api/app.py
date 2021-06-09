from flask import Flask, json, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv, find_dotenv
from os import getenv
import requests

load_dotenv(find_dotenv())

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
CORS(app)
# Throttle
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10/second"]
)

def strip_down(item):
    return { 
        "id": item["id"]["videoId"],
        "title": item["snippet"]["title"],
        "description": item["snippet"]["description"][:100] + ('...' if len(item["snippet"]["description"]) > 100 else ''),
        "url": "https://www.youtube.com/watch?v=" + item["id"]["videoId"],
        "thumbnail": {
            "url": item["snippet"]["thumbnails"]["medium"]["url"],
            "width": item["snippet"]["thumbnails"]["medium"]["width"],
            "height": item["snippet"]["thumbnails"]["medium"]["height"],
        }
    }

def search_by_terms(terms):
    req = requests.get("https://youtube.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults={}&key={}&q={}".format(
        getenv("ITEMS_PER_PAGE"),
        getenv("YOUTUBE_API_KEY"),
        terms
    ))

    result = req.json()

    if 'error' in result:
        raise Exception(result['error']['message'])

    if 'items' in result:
        return list(map(strip_down, result["items"]))

    return []

# Routes

@app.route("/")
def index():
    return jsonify({ "message": "Por favor utiliza el endpoint /api/search para iniciar una búsqueda." }), 200

@app.route("/ping")
def ping():
    return jsonify({ "message": "pong!" }), 200

@app.route("/api/search")
def getSearch():
    if not 'q' in request.args:
        return jsonify({ "message": "No se especificaron términos de búsqueda." }), 400

    try:
        result = search_by_terms(request.args['q'])
        return jsonify(result), 200
    except Exception as e:
        app.logger.error(request.args['q'])
        app.logger.error(e)
        return jsonify({ "message": f"Error: {e}" }), 500

# Start the app

if __name__ == "__main__":
    app.run(debug=getenv('DEBUG'), port=getenv('PORT'))