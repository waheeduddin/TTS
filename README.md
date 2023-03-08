# TTS
A python-flask app that uses [coqui-ai](https://github.com/coqui-ai/TTS) [YourTTS](https://arxiv.org/abs/2112.02418) model to clone voice and convert any english text into speech in that voice. <br /> For now a default voice is added in the `app/temp` folder. Just remove the `mySampleSpeaker.wav` and add your own voice samples as `mySampleSpeaker.wav` file. 

## RUN
- install dependencies `pip install -r requirements.txt`
- run the main.py file `python main.py`
The application should run on port 5005.
