# pip install ffmpeg
# pip install pydub
from pydub import AudioSegment

audio = AudioSegment.from_wav("output.wav")

# boost volume by 6dB
audio = audio + 12

# repeat the clip twice
audio = audio * 2

# 2 sec fade in
audio = audio.fade_in(2000)

audio.export("mashup.mp3", format="mp3")

audio = AudioSegment.from_mp3("mashup.mp3")

print('all set, we are done!')