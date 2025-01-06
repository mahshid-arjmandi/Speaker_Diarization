#!pip install pydub
#!apt-get install ffmpeg -y
from pydub import AudioSegment
audio1 = AudioSegment.from_file("/content/edited_audio_new_.wav")  # فایل اول
audio2 = AudioSegment.from_file("/content/007.wav")  # فایل دوم
#combined = audio1 + audio2
combined = audio1.overlay(audio2)
# ذخیره فایل ترکیبی
combined.export("combined__audio__.wav", format="wav")
print("فایل ترکیبی با موفقیت ساخته شد!")
