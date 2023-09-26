from gtts import gTTS
import os

'''
#file = open("abc.txt", "r", encoding='utf-8').read()
#speech = gTTS(text=file, lang='ru', slow=False)
#speech.save("voice.mp3")
#os.system("voice.mp3")
'''


def voice_handler(text, prompt):
    with open('back/text_to_voice/file1.txt', 'w+', encoding='utf-8') as file1:
        file1.write(text)

    file2 = open('back/text_to_voice/file1.txt', "r", encoding='utf-8').read()
    speech1 = gTTS(text=file2, lang='ru', slow=False)
    speech1.save("voice.mp3")
    result = "voice.mp3"
    if prompt == 1:
        os.system("voice.mp3")
    elif prompt == 2:
        return result