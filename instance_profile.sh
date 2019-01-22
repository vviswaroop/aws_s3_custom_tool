#!/bin/bash
instance_profile=`curl http://169.254.169.254/latest/meta-data/iam/security-credentials/`
echo $instance_profile

aws_access_key_id=`curl http://169.254.169.254/latest/meta-data/iam/security-credentials/${instance_profile} | grep AccessKeyId | cut -d':' -f2 | sed 's/[^0-9A-Z]*//g'`


aws_secret_access_key=`curl http://169.254.169.254/latest/meta-data/iam/security-credentials/${instance_profile} | grep SecretAccessKey | cut -d':' -f2 | sed 's/[^0-9A-Za-z/+=]*//g'`


aws_session_token=`curl http://169.254.169.254/latest/meta-data/iam/security-credentials/${instance_profile} | grep Token | cut -d':' -f2 | sed 's/[^0-9A-Za-z/+=]*//g'`


echo "Exporting environment variables"
export AWS_ACCESS_KEY_ID=${aws_access_key_id}
export AWS_SECRET_ACCESS_KEY=${aws_secret_access_key}
export AWS_SESSION_TOKEN=${aws_session_token}


echo "Exporting Default region"
export AWS_DEFAULT_REGION=us-east-1

echo "Done"
