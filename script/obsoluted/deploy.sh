#!/bin/bash

if [ $# -ne 1 ]; then
    echo "usage:deply.sh  <target(staging or prod)>"
    exit 1
fi

TARGET=$1
WORKDIR=~/work/${TARGET}
REGION="eu-west-1"
PLATFORM="Python 3.4"

# change these
REPO=https://github.com/ZacVND/GROUPB-AWS.git
PROJECT=GROUPB-AWS
PROFILE=test
ENVNAME=GROUPB-AWS-${TARGET}
CNAME=GROUPB-AWS-${TARGET}

# 1. cd to workdir
# 2. checkout from github
# 3. deploy
#
# this script is run by cron
#

#rm -rf WORKDIR
echo 'create work directory'
mkdir -p $WORKDIR
cd $WORKDIR

echo 'checkout source code'
git clone $REPO
cd $PROJECT
git pull


echo 'create environment it takes a long time'
eb init --profile $PROFILE -r "${REGION}" -p "${PLATFORM}"
eb deploy $ENVNAME

