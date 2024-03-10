import numpy as np
from numpy.fft import *
from numpy.random import *
import matplotlib.pyplot as plt
import IPython.display as ipd
import soundfile as sf
import sys

offset=0

Alphabet = {num: chr(num - 501 + ord('A')-offset) for num in range(501+offset, 527+offset)}

def decode(file:str):
    mot=''
    x, Fe = sf.read(file)
    #show_signal_T(x,Fe)
    T=[i*1/Fe for i in range(len(x))]
    offset=0
    while offset<=len(x)-2000:
        N=Fe*8
        x_symbole=x[offset:offset+2000]

        x_fft=np.fft.fft(x_symbole,N)
        show_signal_F(np.abs(x_fft),Fe)
        Tec=T[1999]
        index=np.argmax(np.abs(x_fft[:len(x_fft)//2]))
        print(index/Tec*len(x_symbole)/N)
        a=np.round(index/Tec*len(x_symbole)/N)
        if a in Alphabet :
                mot+=Alphabet[a]
        else :
             mot+=' '
        offset=offset+2500
    print(mot)
    #x_fft_b=[num if num > x_fft_max/2 else 0 for num in np.abs(x_fft)]
    #show_signal_F(x_fft_b,Fe)
    #for i in range(len(x_fft_b[:len(x_fft_b)//2])):
    #    if x_fft_b[i]!=0:
    #        a=np.floor(i/Tec)
    #        if a in Alphabet :
    #            print(Alphabet[a])
    #        j=0
    #        while x_fft_b[i+j]!=0:
    #            x_fft_b[i+j]=0
    #            j+=1
    #show_signal_F(x_fft_b,Fe)

    
    
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
    decode(f'{sys.argv[1]}.wav')
    #decode('symboleU.wav')


