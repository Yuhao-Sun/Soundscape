# app1.py
from flask import Flask, request, jsonify, send_file
from transformers import WhisperForConditionalGeneration, WhisperProcessor
import torch
import librosa
from gtts import gTTS

app = Flask(__name__)

# 本地模型路径
model_path = "your model path"

# 加载本地模型和处理器
model = WhisperForConditionalGeneration.from_pretrained(model_path)
processor = WhisperProcessor.from_pretrained(model_path)

@app.route('/translate', methods=['POST'])
def translate_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 保存音频文件到临时路径
    temp_audio_path = "temp_audio.wav"
    file.save(temp_audio_path)
    
    # 加载音频文件并进行转译
    audio, _ = librosa.load(temp_audio_path, sr=16000)
    inputs = processor(audio, sampling_rate=16000, return_tensors="pt")
    with torch.no_grad():
        generated_ids = model.generate(inputs["input_features"])
    translated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)
    transcript = translated_text[0]

    # 将转译后的文本转换为语音
    tts = gTTS(transcript, lang='zh')
    tts.save("translated_audio.mp3")

    return send_file("translated_audio.mp3", as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
