from matplotlib import pyplot as plt
import librosa
import numpy as np



y, sr = librosa.load("song.wav")
print(y[500000:500200])
xs = np.linspace(0,len(y)/sr,len(y))
plt.plot(xs[500000:500500],y[500000:500500])
plt.show()