#!/bin/bash

TARGET=prod
WORKDIR=~/work/${TARGET}

# change these
REPO=https://github.com/ZacVND/GROUPB-AWS.git
PROJECT=GROUPB-AWS

# 1. cd to workdir
# 2. checkout from github
# 3. deploy
#
# this script is run by cron
#
cd /home/ubuntu/

#sudo killall python
sudo sh -c 'ps ax|grep manage.py|grep runserver|grep -v grep|cut -d" " -f 2|xargs kill -9'

echo 'checkout source code'
if [ ! -e $PROJECT ]; then
    git clone $REPO
fi
cd $PROJECT
git pull
python manage.py migrate
cd ..

#restart server
cd /home/ubuntu/GROUPB-AWS
python manage.py runserver 0.0.0.0:8000&

date >> /home/ubuntu/log/deploy_prod.log

