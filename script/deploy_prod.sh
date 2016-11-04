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

echo 'checkout source code'
if [ ! -e $PROJECT ]; then
    git clone $REPO
fi
cd $PROJECT
git pull
python manage.py migrate
cd ..

date >> /home/ubuntu/log/deploy_prod.log
