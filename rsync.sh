#!/bin/bash
while true; do
    sshpass -p nao rsync -auv --log-file ="./rsync.log" -e ssh nao@192.168.0.106:/dev/shm/recordings ~/UNIVAQ/LavoriRobotica/NaoAI/recordings/
    sleep 0.5
done


