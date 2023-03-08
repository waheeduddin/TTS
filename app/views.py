from distutils.log import error
from app import app
import io
from flask import render_template, request, send_file, Response
from app.tts import model

from pathlib import Path
BASE_DIR = str(Path(__file__).resolve().parent)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tts", methods = ["POST"])
def streamwav():
    def generate():
        with open(BASE_DIR+"/temp/output.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    
    if(request.form["text"]):
        text = request.form["text"]
        model.tts_to_file(text, speaker_wav=BASE_DIR+"/temp/mySampleSpeaker.wav", 
                          language="en", file_path=BASE_DIR+"/temp/output.wav")
        return Response(generate(), mimetype="audio/x-wav")
    else:
        return {"error": "Please provide the text"}, 400 