import baidu_translator as bd


def processText(text):
    print(f"Source text is {text}")
    # content = text.split(' ')
    # name = content.pop(0)
    # words = ''.join(content)
    translated = translate(text, "zh", "yue")
    return translated


def translate(source, source_la: str, target_la: str):
    return bd.whatis(source, source_la, target_la)
