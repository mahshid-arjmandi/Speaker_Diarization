import torchaudio
from speechbrain.pretrained import SepformerSeparation as separator
model = separator.from_hparams(source="speechbrain/sepformer-wsj02mix", savedir="pretrained_models/sepformer")
input_file = "/content/audio__.wav"
estimated_sources = model.separate_file(path=input_file)
torchaudio.save("speaker1.wav", estimated_sources[:, :, 0].detach().cpu(), 8000)
torchaudio.save("speaker2.wav", estimated_sources[:, :, 1].detach().cpu(), 8000)
print("صدای گویندگان جدا شد و ذخیره گردید.")
