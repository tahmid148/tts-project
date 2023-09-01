# Import Modules
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

# Provide path for model manager JSON file
path = "/home/tahmid/.local/lib/python3.10/site-packages/TTS/.models.json"

# Initialise Model Manager
model_manager = ModelManager(path)

# Download TTS model and its associated vocoder
model_name = "tts_models/en/ljspeech/glow-tts"
model_path, config_path, model_item = model_manager.download_model(model_name)
vocoder_name = model_item["default_vocoder"]
voc_path, voc_config_path, _ = model_manager.download_model(vocoder_name)


# Create a Synthesizer instance
syn = Synthesizer(
    tts_checkpoint=model_path,
    tts_config_path=config_path,
    vocoder_checkpoint=voc_path,
    vocoder_config=voc_config_path
)

# Text to be converted into speech
text = "I am a text readed by a computer"

# Synthesize speech from text
outputs = syn.tts(text)

# Save the generated speech as an audio file
syn.save_wav(outputs, "output/audio.wav")