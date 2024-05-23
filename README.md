多功能音频处理应用
这是一个使用Flask和Streamlit构建的多功能音频处理应用，包括语音转译和音频合并功能。

目录
多功能音频处理应用
目录
功能
安装
运行应用
使用说明
文件结构
依赖项
功能
语音转译：将上传的音频文件转换为文本并输出为语音文件。
音频合并：将两段音频文件合并，使用第一段音频的内容和第二段音频的音色。
安装
克隆本仓库到本地：

bash
复制代码
git clone <your-repo-url>
cd soundscape
创建并激活Python虚拟环境（可选）：

bash
复制代码
python3 -m venv venv
source venv/bin/activate  # 对于Windows用户，使用 `venv\Scripts\activate`
安装所需依赖：

bash
复制代码
pip install -r requirements.txt
安装FFmpeg（用于音频处理）：

bash
复制代码
brew install ffmpeg  # macOS
sudo apt-get install ffmpeg  # Ubuntu
choco install ffmpeg  # Windows
运行应用
启动Flask后端1（用于语音转译）：

bash
复制代码
python translation.py
启动Flask后端2（用于音频合并）：

bash
复制代码
python merge.py
启动Streamlit前端：

bash
复制代码
streamlit run soundscape.py
使用说明
打开浏览器，访问 http://localhost:8501 以打开Streamlit应用。
在左侧栏中选择需要的功能：
语音转译：上传一个音频文件，点击“转译音频”按钮。
音频合并：上传两段音频文件，点击“合并音频”按钮。
查看和播放处理后的音频文件。
文件结构
bash
复制代码
project-directory/
├── translation.py                 # Flask后端1（语音转译）
├── merge.py                 # Flask后端2（音频合并）
├── soundscape.py             # Streamlit前端
├── requirements.txt        # Python依赖项
└── README.md               # 项目说明文件
依赖项
Flask
Streamlit
Transformers
Torch
Librosa
Soundfile
gTTS
pydub
ffmpeg
要安装所有依赖项，请运行：

bash
复制代码
pip install -r requirements.txt
# Soundscrape
