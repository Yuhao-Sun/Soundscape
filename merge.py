# app2.py
from flask import Flask, request, jsonify, send_file
import librosa
import soundfile as sf
import numpy as np

app = Flask(__name__)

def apply_timbre(content_audio_path, style_audio_path, output_path):
    # 使用librosa加载两段音频
    content_audio, content_sr = librosa.load(content_audio_path, sr=None)
    style_audio, style_sr = librosa.load(style_audio_path, sr=None)

    # 确保采样率一致
    if content_sr != style_sr:
        style_audio = librosa.resample(style_audio, orig_sr=style_sr, target_sr=content_sr)

    # 如果音频长度不同，对齐它们
    min_length = min(len(content_audio), len(style_audio))
    content_audio = content_audio[:min_length]
    style_audio = style_audio[:min_length]

    # 计算STFT
    content_stft = librosa.stft(content_audio)
    style_stft = librosa.stft(style_audio)

    # 获取幅度和相位信息
    content_mag, content_phase = librosa.magphase(content_stft)
    style_mag, _ = librosa.magphase(style_stft)

    # 使用style的幅度和content的相位重建音频
    combined_stft = style_mag * content_phase

    # 反向STFT得到时域信号
    combined_audio = librosa.istft(combined_stft)

    # 保存结果
    sf.write(output_path, combined_audio, content_sr)

@app.route('/combine', methods=['POST'])
def combine_audio():
    if 'file1' not in request.files or 'file2' not in request.files:
        return jsonify({'error': 'Both audio files are required'}), 400
    file1 = request.files['file1']
    file2 = request.files['file2']
    if file1.filename == '' or file2.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 保存音频文件到临时路径
    temp_audio_path1 = "temp_audio1.wav"
    temp_audio_path2 = "temp_audio2.wav"
    file1.save(temp_audio_path1)
    file2.save(temp_audio_path2)

    # 应用音色迁移
    combined_audio_path = "combined_audio.wav"
    apply_timbre(temp_audio_path1, temp_audio_path2, combined_audio_path)

    return send_file(combined_audio_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
