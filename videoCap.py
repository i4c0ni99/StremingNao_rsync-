from naoqi import ALProxy
import time
import os

IP = "192.168.0.106"  # Inserisci l'indirizzo IP di NAO
PORT = 9559

# Connessione al servizio ALVideoRecorder
video_recorder = ALProxy("ALVideoRecorder", IP, PORT)
video_recorder.stopRecording()

video_recorder.setResolution(2)        # Risoluzione VGA (640x480)
video_recorder.setFrameRate(30)        # Frame rate di 10 fps
video_recorder.setVideoFormat("MJPG")  # Formato MJPG (salvato come .avi)


while True :
    i=0
    while i <= 1:
        video_name = "video_from_nao" + str(i).zfill(2)
        video_recorder.startRecording("/dev/shm/recordings/", video_name )
        print("Registrazione avviata...",i)

        # Tempo di registrazione
        time.sleep(1) 

        # Ferma la registrazione
        video_info = video_recorder.stopRecording()
        
      
        i+=1

   