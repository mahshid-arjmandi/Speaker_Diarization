!pip install torchaudio
!pip install speechbrain
import torchaudio
from speechbrain.pretrained import SepformerSeparation as separator
model = separator.from_hparams(source="speechbrain/sepformer-wsj02mix", savedir="pretrained_models/sepformer")
from google.colab import files
files.upload()
# نمایش مسیر فعلی
print("Current Directory:", os.getcwd())

# نمایش فایل‌های موجود در مسیر جاری
print("Files in Current Directory:", os.listdir())
input_file = "/content/audio__.wav"
estimated_sources = model.separate_file(path=input_file) 

!pip install pydub
from pydub import AudioSegment

# مسیر فایل ورودی و خروجی
input__file = "VoiceClass.m4a"  # فایل MP4
output__file = "output_audio.wav"  # فایل WAV

try:
    # بارگذاری فایل MP4
    audio = AudioSegment.from_file(input__file, format="mp4")

    # تنظیم نرخ نمونه‌برداری و تک‌کاناله
    audio = audio.set_frame_rate(16000).set_channels(1)

    # ذخیره فایل خروجی به صورت WAV
    audio.export(output__file, format="wav")
    print(f"تبدیل با موفقیت انجام شد! فایل خروجی: {output__file}")

except Exception as e:
    print(f"خطا در تبدیل فایل: {e}")
estimated__sources = model.separate_file(path=output__file)

torchaudio.save("speaker1.wav", estimated_sources[:, :, 0].detach().cpu(), 8000)
torchaudio.save("speaker2.wav", estimated_sources[:, :, 1].detach().cpu(), 8000)

print("صدای گویندگان جدا شد و ذخیره گردید.")
