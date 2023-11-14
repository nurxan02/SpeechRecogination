import speech_recognition as sr
from gtts import gTTS
import playsound
import tkinter as tk

recognized_text = ""  

def start_listening():
    global recognized_text
    status_label.config(text="Listening...")
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio, language='tr-TR')
        status_label.config(text="")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, recognized_text)
    except sr.UnknownValueError:
        status_label.config(text="Could not understand audio")

def play_audio():
    text = result_text.get(1.0, tk.END).strip()
    if text:
        tts = gTTS(text=text, lang='tr')
        tts.save("output.mp3")
        playsound.playsound("output.mp3")

app = tk.Tk()
app.title("Səsi mətinə çevirmək (Türkcə)")

status_label = tk.Label(app, text="", font=("Arial", 12))
status_label.pack()

listen_button = tk.Button(app, text="Dinləməyə başla", command=start_listening, width=20, height=2)
listen_button.pack(side=tk.TOP, padx=10, pady=5)

result_text = tk.Text(app, height=10, width=50)
result_text.pack(padx=10, pady=5)

play_button = tk.Button(app, text="Səsləndir", command=play_audio, width=20, height=2)
play_button.pack(side=tk.TOP, padx=10, pady=5)

app.mainloop()
