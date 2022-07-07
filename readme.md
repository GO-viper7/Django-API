# API DJANGO
```
 Run the command: python manage.py runserver 
 Call the endpoint http://localhost:8000/mail_details/ and is GET request 
```
#### **`Returns a json list `**
### For Example :  <br />
```Javascript
{ 
    "res": [ 
        { 
           "from": "", 
            "to": "", 
            "subject": "", 
            "date": "", 
            "messageId": "", 
            "text": "", 
            "attachments": [ 
              "fileName": "", 
              "coded": "" 
            ] 
        }, 
    ] 
} 
 ```
**Attachments are "ISO-8859-1 decoded" to strings**  <br />
#### So as to access attachemnts u need to "ISO-8859-1 encode" to bytes and then upload into a file <br />
## For example in python:  <br /><br />
```python
with open(f'{fileName}', 'wb') as fp: 
    fp.write(coded.encode("ISO-8859-1"))
```
#### where fileName and coded are the attributes which api offers  <br />
#### when it encounters an attachment in mail <br />
---
