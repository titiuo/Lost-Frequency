import numpy as np
from numpy.fft import *
from numpy.random import *
import matplotlib.pyplot as plt
import IPython.display as ipd
import soundfile as sf
import sys

offset=0

Alphabet = {num: chr(num - 501 + ord('A')-offset) for num in range(501+offset, 527+offset)}


def decode(x,Fe):
    T=[i*1/Fe for i in range(len(x))]
    Tec=T[1999]
    x_fft=np.fft.fft(x)
    x_fft_max=np.max(np.abs(x_fft))
    freq= np.argmax(np.abs(x_fft))/Tec
    freq_entier=round(freq)
    #print(freq_entier)
    if freq_entier in Alphabet:
        print(Alphabet[freq_entier])
    #x_fft_b=[num if num > x_fft_max/2 else 0 for num in np.abs(x_fft)]
    #show_signal_F(x_fft,Fe)
    #for i in range(len(x_fft_b[:len(x_fft_b)//2])):
        #if x_fft_b[i]!=0:
            #a=np.floor(i/Tec)
            #if a in Alphabet :
                #print(Alphabet[a])
            #j=0
            #while x_fft_b[i+j]!=0:
                #x_fft_b[i+j]=0
                #j+=1
    #show_signal_F(x_fft_b,Fe)

def decodes(file:str):
    x, Fe = sf.read(file)  
    i=0
    while i < len(x):
        decode(x[i:i+2000],Fe)
        i+=2500


    #show_signal_T(x,Fe)
    #show_signal_F(x_fft,Fe)



def show_signal_T(x,Fe):
    T=[i*1/Fe for i in range(len(x))]
    plt.figure(figsize=(10,4))
    plt.plot(T,x,color='b')
    plt.xlabel('Temps en seconde')
    plt.ylabel('Amplitude')
    plt.title('Signal audio')
    plt.grid()
    plt.show()

def show_signal_F(x,Fe):
    T=[i*1/Fe for i in range(len(x))]
    Tec=T[-1]
    F=[i/Tec for i in range(len(x))]
    plt.figure(figsize=(10,4))
    plt.plot(F,x,color='b')
    plt.xlabel('Fréquence en Hz')
    plt.ylabel('Amplitude')
    plt.title('TF du Signal audio')
    plt.grid()
    plt.show()




if __name__ == '__main__':
    decodes(f'{sys.argv[1]}.wav')
    #decode('symboleU.wav')


