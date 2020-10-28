#speech to text
import win32com.client as winc
speak=winc.Dispatch("SAPI.spVoice")
speaker.speak()  #speaker is bject basicaly calling speak