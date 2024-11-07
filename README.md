# StremingNao_rsync-
# Progetto di Cattura Video con il Robot NAO

Questo progetto utilizza il robot **NAO** di **SoftBank Robotics** per catturare video tramite il modulo `ALVideoCapture`. NAO è un robot umanoide versatile, progettato per l'educazione, la ricerca e l'intrattenimento. Utilizzando le API di NAO, possiamo catturare immagini e video direttamente dalla sua telecamera e utilizzarli in applicazioni come la visione artificiale e il machine learning.

## Requisiti

- Robot NAO di SoftBank Robotics con l'accesso alla rete
- Python e OpenCV installati nel sistema locale per ricevere e analizzare i video

## Modulo ALVideoCapture

Il modulo `ALVideoCapture` è un proxy API fornito dal sistema operativo del robot NAO che permette di accedere alle sue telecamere. Questo modulo consente di catturare immagini e video dal robot, che possono essere trasmessi a un computer remoto per ulteriori elaborazioni.

## Setup

1. **Installazione di OpenCV**

   Per eseguire script di cattura e visualizzazione video sul tuo sistema, installa il pacchetto `opencv-python`:

   ```bash
   pip install opencv-python

2. **Trasferimento di file da eseguire sul nao**

    Per trasferire il passaggio del file videoCap.py dalla macchina locale al nao è consigliato l'uso di scp.lanciare questo comando per trasferire il suddetto file :

    ```bash
    scp videoCap.py nao@<indirizzo_ip_nao>:/home/nao/

3. **Connettersi al nao**
    la connessione al nao avviene tramite ssh lanciando il comando :

    ```bash
    ssh nao@<indirizzo_ip_del_nao> 

4. una volta stabilita la conessione eseguire con python lo script videoCap.py,lasciandolo iun ascolto su di esso. 
   
5. Aprire sulla tua macchina locale un nuovo terminale e eseguire il file rsync.sh per avviare cosi una comunicazione attraverso ssh che all'occorrenza prelevera i file .avi.
   
6. con quest'ultimo script python la catena sara completa,eseguire visualize.py per renderizzare le immagini prelevate dal nao.

    
