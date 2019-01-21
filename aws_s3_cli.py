#importing the required python modules for fully funcitonal s3 custom tool
#####################################
import boto3
import string
from datetime import datetime
import datetime
import sys
####################################

#To get the details of the specific bucket by specifying the name
def list_buckets2(arguments):
        s3 = boto3.resource('s3')
        bucket_list = [bucket.name for bucket in s3.buckets.all()]
        for bucket in s3.buckets.all():
                region_name = s3.meta.client.get_bucket_location(Bucket=bucket.name)["LocationConstraint"] #initial step to identify the region name of the bucket
                name = bucket.name
                if arguments == name:
                        print
                        print
                        print("Printing Details of The Bucket \"%s\"  " % bucket.name)
                        print
                        my_bucket = s3.Bucket(bucket.name)
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print
                        print ("Files that are present in the bucket requested: ")
                        print
                        print ("File Name \t \t Storage class")
                        print
                        a = 0
                        fs = 0
                        fdate2 = datetime.datetime(1999, 5, 17) #sample date for comparision
                        fdate3 = fdate2.date()
                        for object in my_bucket.objects.all(): #to get the list of objects present in the bucket requested
                            fname = object.key

                            fsize = object.size
                            fs = fs + fsize
                            if fname.endswith('/'):
                                continue
                            else:#lsit only files and exclude the folders
                                fdate1 = object.last_modified
                                fdate4 = fdate1.date()
                                obclass = object.storage_class
                                print (" %s\t \t \t \t %s" % (fname , obclass))
                                a = a+1
                        b = 0
                        while fs > 1024: #object file size conversion bytes to kilobytes to megabytes to gigabytes (bytes to kb to mb to gb)
                            fs = fs/1024
                            b = b + 1
                        print
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print
                        print ("Number of Files in Bucket: %s" %a)
                        print
                        print
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print
                        if b == 1:
                            print ("Bucket Size: %s Kb " % fs)
                            print ("Storage Price: %s $" % (((fs/1024)/1024)*.039))
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print
                        elif b == 2:
                            print ("Bucket Size: %s Mb " % fs)
                            print ("Storage Price: %s $" % ((fs/1024)*.039))
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print
                        elif b == 3:
                            print ("Bucket Size: %s Gb " % fs)
                            print ("Storage Price : %s $" % (fs*.039))
                            print
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print




def list_buckets1(arguments):
        s3 = boto3.resource('s3')
        bucket_list = [bucket.name for bucket in s3.buckets.all()]
        for bucket in s3.buckets.all():
                region_name = s3.meta.client.get_bucket_location(Bucket=bucket.name)["LocationConstraint"] #initial step to identify the region name of the bucket
                name = bucket.name
                if arguments == name:
                        print
                        print
                        print("Printing Details of The Bucket \"%s\"  " % bucket.name)
                        print
                        my_bucket = s3.Bucket(bucket.name)
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print
                        print ("List of Files Modified today: ")
                        print
                        a = 0
                        fs = 0
                        fdate2 = datetime.datetime.today() #defining a sample date for the comparisson
                        fdate3 = fdate2.date()
                        for object in my_bucket.objects.all(): #get the bucket objects
                            fname = object.key

                            fsize = object.size
                            fs = fs + fsize
                            if fname.endswith('/'):
                                continue
                            else:#lsit only files and exclude the folders
                                fdate1 = object.last_modified
                                fdate4 = fdate1.date()
                                obclass = object.storage_class
                                a = a+1
                                if fdate4 >= fdate3:
                                    print fname,fdate1
                                    print
                                    fdate3 = fdate4
                        b = 0
                        while fs > 1024: #convert the size from bytes to kb to mb to gb
                            fs = fs/1024
                            b = b + 1
                        print
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print
                        print ("Number of Files in Bucket: %s" %a)
                        print
                        print
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print
                        if b == 1:
                            print ("Bucket Size: %s Kb " % fs)
                            print ("Storage Price: %s $" % (((fs/1024)/1024)*.039))
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print
                        elif b == 2:
                            print ("Bucket Size: %s Mb " % fs)
                            print ("Storage Price: %s $" % ((fs/1024)*.039))
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print
                        elif b == 3:
                            print ("Bucket Size: %s Gb " % fs)
                            print ("Storage Price : %s $" % (fs*.039))
                            print
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print







def list_buckets(): #function to list the buckets available and bucket's details (region,creation date & bucket name)
        s3 = boto3.resource('s3')
        bucket_list = [bucket.name for bucket in s3.buckets.all()]
        print("Bucket Name--------------------------------------Created on---------------------------------------Region")
        for bucket in s3.buckets.all():
                region_name = s3.meta.client.get_bucket_location(Bucket=bucket.name)['LocationConstraint']
                if region_name : #print the result if the region is NOT s-east-1
                    print("{name}\t\t====>>\t\t{created}\t\t====>>\t\t{region}".format(name=bucket.name, created=bucket.creation_date,region=region_name))
                else : #print the result if the region is us-east-1 (us-east-1 is stored as None)
                    print("{name}\t\t====>>\t\t{created}\t\t====>>\t\tus-east-1".format(name=bucket.name, created=bucket.creation_date))


def main():
    if len(sys.argv) == 3:
        arguments = sys.argv[1]
        list_buckets2(arguments)
    elif len(sys.argv) == 2:
        arguments = sys.argv[1]
        list_buckets1(arguments)
    elif len(sys.argv) == 1:
        list_buckets()
if __name__ == "__main__":
    main()
