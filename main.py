import flask
import uuid
import mac_say
import text_process
import sys
from flask import Flask, request
from pydub import AudioSegment

app = Flask(__name__)
process = sys.argv[1]


@app.route("/tts")
def receiveText():
    global process
    text = request.args.get('text')
    if process == '-p':
        text = text_process.processText(text)
    mac_say.say(["-o", "voice.wav", text, "--data-format=LEF32@48000"])
    convertToMp3()
    return flask.send_file("voice_converted.mp3", download_name=str(uuid.uuid1()) + ".mp3", as_attachment=True)


def convertToMp3():
    source_audio = AudioSegment.from_file("voice.wav")
    source_audio.export("voice_converted.mp3", format="mp3")


if __name__ == '__main__':
    if process == '-p':
        print("--Text process enabled--")
    app.run(host="0.0.0.0", port=5001)
