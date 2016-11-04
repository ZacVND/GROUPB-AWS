bpath='/home/ubuntu/backups'

latest_backup=$(ls -t $bpath | head -1)

scp -i /home/ubuntu/pem/backup.pem $bpath/$latest_backup  ubuntu@35.162.183.154:/home/ubuntu/db/dump/
