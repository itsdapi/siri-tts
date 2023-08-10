import flask
import uuid
import mac_say
import baiduTranslator as bd
from flask import Flask, request
from pydub import AudioSegment

app = Flask(__name__)


@app.route("/tts")
def receiveText():
    text = processText(request.args.get('text'))
    mac_say.say(["-o", "voice.wav", text, "--data-format=LEF32@48000"])
    convertToMp3()
    return flask.send_file("voice_converted.mp3", download_name=str(uuid.uuid1()) + ".mp3", as_attachment=True)


def convertToMp3():
    source_audio = AudioSegment.from_file("voice.wav")
    source_audio.export("voice_converted.mp3", format="mp3")


def translateToCantonese(source):
    return bd.whatis(source, "zh", "yue")


def processText(text):
    print(f"Source text is {text}")
    content = text.split(' ')
    name = content.pop(0)
    words = ''.join(content)
    translated = translateToCantonese(words)
    return name+translated


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
