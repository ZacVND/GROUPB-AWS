# Sends current database to the backup server

date=$(date +%Y-%m-%d-%H-%M)

cpath='/home/ubuntu/db'
echo $cpath
pg_dump groupb_aws> $cpath/$date

scp -i $cpath/backup.pem $cpath/$date ubuntu@35.162.173.174:/home/ubuntu/backups

rm $cpath/$date

echo $date >> $cpath/status.log

echo "\n----------\n" >> $cpath/status.log



