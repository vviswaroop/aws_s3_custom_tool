# aws_s3_custom_tool
aws s3 tool to get the list of buckets, details of the bucket such as number of objects, size, cost etc;

The following code was dveloped & intended to perform operations on AWS S3 service.

This script can be run in three ways in order to get the appropriate results.

NOTE: there are many ways to get the results, it is just the matter of fact that i choosed this way.

1. To list the AWS S3 buckets in your account i.e; python aws_s3_cli.py
2. To get the detials of the specific bucket
	a. Last modified files along with modification date
        b. Total number of files in the bucket
        c. Bucket Size
        d. Cost
3. To get the list of objects present in a bucket
	a. list of all files and storage class of the file
	b. Total number of files in the bucket
	c. Bucket Size
	d. Cost of the bucket


System Requirements:
Python27
boto3
sys
datetime
IAM User
AWS CLI



Steps:
1. To install AWS CLI
 $ pip install awscli / yum install awscli
2. aws configure
	pass the credentials and config
3.Below are the 3 ways to execute the script

	a. List buckets:
		python aws_s3_cli.py
			Viswaroops-MacBook-Pro:aws_s3_custom_tool vadlamudi$ python aws_s3_cli.py \n 
			Bucket Name--------------------------------------Created on---------------------------------------Region \n
			aws-logs-328427342299-us-east-1		====>>		2018-01-11 05:10:17+00:00		====>>		us-east-1 \n
			cf-templates-ckj5u60m36f9-us-east-1		====>>		2018-01-11 05:04:29+00:00		====>>		us-east-1 \n
			cf-templates-ckj5u60m36f9-us-west-2		====>>		2018-01-11 06:10:05+00:00		====>>		us-west-2 \n
			elasticbeanstalk-us-east-1-328427342299		====>>		2019-01-03 00:46:05+00:00		====>>		us-east-1 \n
			myawscloudtrailbucket20180111		====>>		2018-01-11 06:24:49+00:00		====>>		us-west-2 \n
			mycloudformationscript		====>>		2018-02-02 17:09:11+00:00		====>>		us-east-1 \n
			myemrbucket20180111		====>>		2018-01-11 06:12:00+00:00		====>>		us-west-2 \n
			viswatestemr		====>>		2018-01-11 05:06:42+00:00		====>>		us-east-1 \n
 
	b. details of specific bucket:
		python aws_s3_cli.py viswatestemr
			Viswaroops-MacBook-Pro:aws_s3_custom_tool vadlamudi$ python aws_s3_cli.py viswatestemr


				Printing Details of The Bucket "viswatestemr"  

				~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

				List of Files Modified today: 


				~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

				Number of Files in Bucket: 13


				~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

				Bucket Size: 126 Kb 
				Storage Price: 0.0 $
				~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	c. Output while passing the list argument
		python aws_s3_cli.py viswatestemr list
			Viswaroops-MacBook-Pro:aws_s3_custom_tool vadlamudi$ python aws_s3_cli.py viswatestemr list


Printing Details of The Bucket "viswatestemr"  

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Files that are present in the bucket requested: 

File Name 	 	 Storage class

 AWSLogs/328427342299/CloudTrail/us-east-1/2018/01/11/328427342299_CloudTrail_us-east-1_20180111T0505Z_31vsaZo94jBOorSI.json.gz	 	 	 	 STANDARD
 AWSLogs/328427342299/CloudTrail/us-east-1/2018/01/11/328427342299_CloudTrail_us-east-1_20180111T0510Z_6EYjss8cTf27KCwX.json.gz	 	 	 	 STANDARD
 AWSLogs/328427342299/CloudTrail/us-east-1/2018/01/11/328427342299_CloudTrail_us-east-1_20180111T0510Z_73Zi2csTKu7ot9mq.json.gz	 	 	 	 STANDARD
 AWSLogs/328427342299/CloudTrail/us-east-1/2018/01/11/328427342299_CloudTrail_us-east-1_20180111T0510Z_uPag4hPYb5u0K19O.json.gz	 	 	 	 STANDARD
 AWSLogs/328427342299/CloudTrail/us-east-1/2018/01/11/328427342299_CloudTrail_us-east-1_20180111T0515Z_c8ocCzpgLR5BsIfM.json.gz	 	 	 	 STANDARD
 AWSLogs/328427342299/CloudTrail/us-east-1/2018/01/11/328427342299_CloudTrail_us-east-1_20180111T0515Z_ndQXeP26cWyUCG67.json.gz	 	 	 	 STANDARD
 AWSLogs/328427342299/CloudTrail/us-east-1/2018/01/11/328427342299_CloudTrail_us-east-1_20180111T0515Z_nvdHr3tYDp2ViOyj.json.gz	 	 	 	 STANDARD
 AWSLogs/328427342299/CloudTrail/us-east-1/2018/01/11/328427342299_CloudTrail_us-east-1_20180111T0520Z_1ro8qO8v39zCAc5c.json.gz	 	 	 	 STANDARD
 AWSLogs/328427342299/CloudTrail/us-east-1/2018/01/11/328427342299_CloudTrail_us-east-1_20180111T0520Z_cC6W3ui0YN06o1t2.json.gz	 	 	 	 STANDARD
 cf-1.json	 	 	 	 STANDARD
 cf.json	 	 	 	 STANDARD
 param (2).json	 	 	 	 STANDARD
 test.bash	 	 	 	 STANDARD

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Number of Files in Bucket: 13


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bucket Size: 126 Kb 
Storage Price: 0.0 $
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


NOTE:
Cost is an approximate value based on storage type****




