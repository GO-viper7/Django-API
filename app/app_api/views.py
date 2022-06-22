from .. import models
from . import serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import boto3
import base64
from email import policy
import os
from email.parser import BytesParser
s3_client = boto3.client("s3", 
                  region_name='us-east-1', 
                  aws_access_key_id='AKIA4SWO2AOMZ2ORRSVJ', 
                  aws_secret_access_key='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')
response = s3_client.list_objects_v2(Bucket='newbillokbucketfora2')
files = response.get("Contents")
from collections import defaultdict
from email.parser import Parser




def find_attachments(message):
    found = []
    for part in message.walk():
        if 'content-disposition' not in part:
            continue
        cdisp = part['content-disposition'].split(';')
        cdisp = [x.strip() for x in cdisp]
        if cdisp[0].lower() != 'attachment':
            continue
        parsed = {}
        for kv in cdisp[1:]:
            key, val = kv.split('=')
            if val.startswith('"'):
                val = val.strip('"')
            elif val.startswith("'"):
                val = val.strip("'")
            parsed[key] = val
        found.append((parsed, part))
    return found

         




@api_view()
def api(request):
  mails = []
  for file in files:
    res = s3_client.get_object(Bucket='newbillokbucketfora2', Key= file['Key'])
    body = res['Body'].read()
    try:
        with open(f"encodedFiles/{file['Key']}.eml", 'wb') as f:
         f.write(body)
    except FileNotFoundError:
      print("error")
    
    eml_filename = f"encodedFiles/{file['Key']}.eml"
    with open(eml_filename) as f:
        msg = Parser().parse(f)
    attachments = find_attachments(msg)
    attaches = []
    for cdisp, part in attachments:    
        attach = {"fileName" : '', "coded" : ''}
        with open(f'decodedFiles/{cdisp["filename"]}', 'wb') as fp:
            attach['fileName'] = cdisp["filename"]
            data = part.get_payload(decode=True)
            fp.write(data)
            attach['coded'] = data.decode("ISO-8859-1")
            attaches.append(attach)
            
    with open(f"encodedFiles/{file['Key']}.eml", 'rb') as fp:     
      msg = BytesParser(policy=policy.default).parse(fp)
      mails.append({
        "from" : msg['from'],
        "to" :  msg['to'],
        "subject" : msg['subject'],
        "date" : msg['date'],
        "messageId" :  msg['Message-ID'],
        "text" : msg.get_body(preferencelist=('plain')).get_content(),
        "attachments" : attaches
        }) 
  return Response({"res" : mails})