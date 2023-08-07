import flask
import uuid
import mac_say
from flask import Flask, request
from pydub import AudioSegment

app = Flask(__name__)


@app.route("/tts")
def receiveText():
    text = request.args.get('text')
    mac_say.say(["-o", "voice.wav", text, "--data-format=LEF32@48000"])
    convertToMp3()
    return flask.send_file("voice_converted.mp3", download_name=str(uuid.uuid1()) + ".mp3")


def convertToMp3():
    source_audio = AudioSegment.from_file("voice.wav")
    source_audio.export("voice_converted.mp3", format="mp3")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)