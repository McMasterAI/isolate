import sys
import wave


'''
The sound file should have the .wav format and placed in the same folder as main.py
'''

AUDIO_FORMAT = ['wav']

if __name__ == '__main__':
    assert len(sys.argv)==2
    assert sys.argv[1].split('.')[-1] in AUDIO_FORMAT
    try:
        wavefile = wave.open(sys.argv[1], 'r')
        print("The audio file is successfully read into memory")
    except Exception as e:
        print(e)

