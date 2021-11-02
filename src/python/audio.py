import wave
# from __future__ import division
import bokeh.plotting as bk
from matplotlib import pyplot
import numpy
import pyaudio
import scipy.signal as signal
from matplotlib.pyplot import *
from numpy import *
from numpy.fft import *

# https://inst.eecs.berkeley.edu/~ee123/sp15/lab/lab3/s1.wav
FILE_PATH = "/Users/j0z07b8/pyLime-workspace/s1.wav"
BIT_DEPTH = "int16"


def read_wav(file_path: str):
    try:
        wf = wave.open(file_path, 'rb')
    except FileNotFoundError:
        return None

    CHUNK = 1024
    frames = []
    data_str = wf.readframes(CHUNK)  # read a chunk

    while data_str != '' and data_str != b'':
        print("CHUNK_DATA: ", data_str)
        data_int = numpy.frombuffer(data_str, BIT_DEPTH)  # convert from string to int
        data_flt = data_int.astype(numpy.float32) / 32767.0  # convert from int to float32
        frames.append(data_flt)  # append to list
        data_str = wf.readframes(CHUNK)  # read a chunk

    return numpy.concatenate(frames)


def play_audio(data: str, fs: float):
    py_audio = pyaudio.PyAudio()
    out_stream = py_audio.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
    out_stream.write(data.astype(numpy.float32).tobytes())
    py_audio.terminate()

    return out_stream


data = read_wav(FILE_PATH)
print(data)
play_audio(data, 48000)
