import streamlit as st
import requests
import io

st.title('多功能音频处理应用')

# 页面导航
option = st.sidebar.selectbox('选择功能', ('语音转译', '音频合并'))

# 语音转译功能
if option == '语音转译':
    st.header('语音转译')
    uploaded_file = st.file_uploader("选择一个音频文件", type=["wav", "mp3"])
    
    if uploaded_file is not None:
        audio_bytes = uploaded_file.read()
        st.audio(audio_bytes, format=uploaded_file.type)
        
        if st.button('转译音频'):
            files = {'file': (uploaded_file.name, io.BytesIO(audio_bytes), uploaded_file.type)}
            response = requests.post('http://localhost:5001/translate', files=files)
            if response.status_code == 200:
                with open("translated_audio.mp3", "wb") as f:
                    f.write(response.content)
                st.audio("translated_audio.mp3", format="audio/mp3")
            else:
                st.error('请求失败，请检查后端服务。')

# 音频合并功能
if option == '音频合并':
    st.header('音频合并')
    uploaded_file1 = st.file_uploader("选择第一段音频文件", type=["wav", "mp3"], key="file1")
    uploaded_file2 = st.file_uploader("选择第二段音频文件", type=["wav", "mp3"], key="file2")

    if uploaded_file1 is not None and uploaded_file2 is not None:
        audio_bytes1 = uploaded_file1.read()
        audio_bytes2 = uploaded_file2.read()
        st.audio(audio_bytes1, format=uploaded_file1.type)
        st.audio(audio_bytes2, format=uploaded_file2.type)
        
        if st.button('合并音频'):
            files = {
                'file1': (uploaded_file1.name, io.BytesIO(audio_bytes1), uploaded_file1.type),
                'file2': (uploaded_file2.name, io.BytesIO(audio_bytes2), uploaded_file2.type)
            }
            response = requests.post('http://localhost:5003/combine', files=files)
            if response.status_code == 200:
                with open("combined_audio.wav", "wb") as f:
                    f.write(response.content)
                st.audio("combined_audio.wav", format="audio/wav")
            else:
                st.error('请求失败，请检查后端服务。')
