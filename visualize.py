import cv2
import os
import time

# Percorso della cartella contenente i video
video_folder = '/Users/i4c0ni99/UNIVAQ/LavoriRobotica/NaoAI/recordings/recordings'

# Ottieni tutti i file .avi nella cartella
video_files = [f for f in os.listdir(video_folder) if f.endswith('.avi')]

# Ordina i file (se necessario, ad esempio per nome o data di creazione)
video_files.sort()  # Se vuoi ordinarli per nome o in altro modo
print(video_files)
# Itera attraverso i file video

for x in range(100):
    for video_file in video_files:
        # Crea il percorso completo del file video
        video_path = os.path.join(video_folder, video_file)
        if os.path.exists(video_path):
            print(video_path)
            # Apri il video usando cv2.VideoCapture
            cap = cv2.VideoCapture(video_path)
            
            # Controlla se il video è stato aperto correttamente
            if not cap.isOpened():
                print("Errore nell'apertura del file video.")
            else:
                # Riproduce il video frame per frame
                while cap.isOpened():
                    ret, frame = cap.read()  # Legge il frame successivo
                    if ret:
                        cv2.imshow('Video', frame)  # Mostra il frame nella finestra 'Video'
                        time.sleep(0.035)
                        # Premere 'q' per uscire dal loop
                        if cv2.waitKey(25) & 0xFF == ord('q'):
                            break
                    else:
                        # Se non ci sono più frame, esce dal loop
                        print('esco', x ,video_path.split('/')[-1] )
                        break
            os.remove(video_path)
            print(f"File {video_path} è stato cancellato.")        
            # Rilascia il video e chiude tutte le finestre
            cap.release()
        time.sleep(0.5)
    time.sleep(1)        
cv2.destroyAllWindows()
                        
                        
                        

            

            
# Chiudi tutte le finestre di OpenC
    
