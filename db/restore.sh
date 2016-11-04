rm /home/ubuntu/db/dump/*

#shutdown server
#sudo killall python
sudo sh -c 'ps ax|grep manage.py|grep runserver|grep -v grep|cut -d" " -f 2|xargs kill -9'

ssh -i /home/ubuntu/db/backup.pem ubuntu@35.162.173.174 'sh /home/ubuntu/scripts/send.sh'

psql -U ubuntu -d postgres -c "DROP DATABASE groupb_aws;"

psql -U ubuntu -d postgres -c "CREATE DATABASE groupb_aws;"

backup_file=$(ls /home/ubuntu/db/dump/ -t | head -1)

psql groupb_aws< /home/ubuntu/db/dump/$backup_file

#restart server
cd /home/ubuntu/GROUPB-AWS
python manage.py runserver 0.0.0.0:8000&

rm /home/ubuntu/db/dump/*

