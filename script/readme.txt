setup:
1. get aws access key id and secret ke
2. write them to .aws/config
  [profile test]
  aws_access_key_id = XXX
  aws_secret_access_key = XXX
3. (setup security group)


you can run script manually

launch_server.sh
 usage:launch_server.sh <target(staging or prod)>

deploy.sh
 usage:deploy.sh <target(staging or prod)>

if you want to run periodically, set deploy.sh to crontab

finally you cann access via http://groupb-aws-{prod, staging}.eu-west-1.elasticbeanstalk.com/
