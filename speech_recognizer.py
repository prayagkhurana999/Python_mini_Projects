#speech recognition it will recognise our voice and converted to text

import speech_recognition os sp
x=sp.Recogniser()  #instance
with sp.Microphone() as source:  #it us equalent to sp.Microphone bt after its use it will continue to work
    audio=x.listen(source)  #here recogniser is saying listen from source
    text=x.recognize_google(audio)
    print(text)
    
#also have to install PyAudio  otherwise it will thorugh error
