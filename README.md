# s3-scanner
This is a lightweight tool that scans the bucket to check whether it has public read and write permission.

## Requirment:

### packages 

- requests
- xmltodict
- bcolors
- sys
- argparse

### python > 3.x 

## usage: 

bucket.py  -n < name of the bucket >

OPTIONS: 

```
-h             --help    
             	 < show the available options >
-n            valid bucket name (eg. testing)
  		< bucket name want to check >
```

