#!pip install pydub
#!apt-get install ffmpeg -y

from pydub import AudioSegment
audio = AudioSegment.from_file("/content/07.wav")  # فایل صوتی ورودی

start_time = 10  * 1000  # شروع حذف
end_time = 32 * 1000      # پایان حذف
edited_audio = audio[:start_time] + audio[end_time:]

# ذخیره فایل ویرایش‌شده
edited_audio.export("edited_Audio_New_.wav", format="wav")

print("تکه انتخابی با موفقیت حذف شد!")
