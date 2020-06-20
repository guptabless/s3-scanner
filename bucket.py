import requests
import xmltodict
import sys,argparse
import bcolors

def banner():
    print("""
                
            ░██████╗██████╗░░░░░░░░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
            ██╔════╝╚════██╗░░░░░░██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
            ╚█████╗░░█████╔╝█████╗╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
            ░╚═══██╗░╚═══██╗╚════╝░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
            ██████╔╝██████╔╝░░░░░░██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
            ╚═════╝░╚═════╝░░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
                                                                                  Code by NG          
          """)

if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] == '-n') :
        try:
            input_bucket_name = sys.argv[2]
            parser = argparse.ArgumentParser()
            parser.add_argument("-n", required=True)
            args = parser.parse_args()

            print(bcolors.BITALIC + "Testing for Bucket Existence")

            url_host = 'https://' + input_bucket_name + '.s3.amazonaws.com'
            print(url_host)
            input_request = requests.get(url_host)
            input_convert_xml = xmltodict.parse(input_request.content)
            input_status_code = requests.get(url_host).status_code
            if (input_status_code == 403):
                    print('S3 bucket contents not available publically')
                    print(bcolors.BOLD + bcolors.ERRMSG + 'ERROR', input_convert_xml['Error']['Code'])
            elif (input_status_code == 200):
                    print(bcolors.BOLD + input_convert_xml['ListBucketResult']['Name'])
                    print(bcolors.OKMSG + 'S3 bucket contents available publically')
        except:
            print('Please enter python bucket.py -n <valid s3 bucket name> ')

    elif ((sys.argv[1] == '-n') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: bucket.py [-h] -n Bucket Name' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-n Name,   --name S3 bucket name whose visiblity you want to check')
else:
    banner()
    print(bcolors.ERR + 'Please select option from -n or -h, with a valid S3 bucket name')

