from flask import Flask
import json
import os

app = Flask(__name__)


@app.route("/")
def home():
    return {"available_routes": "/act/:act"}


@app.route("/act/<string:act>")
def act(act: str):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "../static", "prompts.json")
    data = json.load(open(json_url))
    for i in range(len(data)):
        if data[i]["act"].lower().replace(" ", "") == act.lower().replace(" ", ""):
            resp = data[i]["prompt"]
            ret = {"act": act.lower(), "prompt": resp}
            return ret
    return {"error": "Prompt doesn't exist."}
