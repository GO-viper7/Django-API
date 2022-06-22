call the endpoint "http://localhost:8000/mail_details/" and is GET request
which returns a json
For Example : 
{
    "res": [
        {
            "from": "Mannoj Tewari <hello@billok.co>",
            "to": "kush@billok.email",
            "subject": "test",
            "date": "Tue, 31 May 2022 22:34:46 +0530",
            "messageId": "<CANEUi8jGMKOyHeU7yvsDgg+dnhjNuedqzGDBZ=sB_mOFx55+3A@mail.gmail.com>",
            "text": "test\n\n-- \n*Mannoj Tewari*\n*Founder,* billok.co\n*E: hello@billok.co <hello@billok.co>*\n*M: +91 7400062746*\n\n\n*one place for all your invoices..*\n\n    <https://www.instagram.com/billok.co/>\n<https://twitter.com/billokindia>     <https://www.facebook.com/billokpage>\n    <https://www.linkedin.com/company/billok>\n",
            "attachments": []
        },
    ]
}

Attachments are "ISO-8859-1 decoded" to strings 
So as to access attachemnts u need to "ISO-8859-1 encode" to bytes and then upload into a file
For example in pythyon: 
with open(f'{fileName}', 'wb') as fp:
    fp.write(coded.encode("ISO-8859-1"))

where fileName and coded are the attributes which api offers 
when it encounters an attachment in mail