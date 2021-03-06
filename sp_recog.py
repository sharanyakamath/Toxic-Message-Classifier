import speech_recognition as sr 
def get_speech(filename):
    r = sr.Recognizer() 
    
    AUDIO_FILE = "./uploads/" + filename
    with sr.AudioFile(AUDIO_FILE) as source: 
        audio = r.record(source)   
    
    try: 
        return r.recognize_google(audio)
    
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
    
    except sr.RequestError as e: 
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['wav'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS