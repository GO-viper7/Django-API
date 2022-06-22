call the endpoint "http://localhost:8000/mail_details/" and is GET request <br />
which returns a json <br />
For Example :  <br />
{ <br />
    "res": [ <br />
        { <br />
            "from": "Mannoj Tewari <hello@billok.co>", <br />
            "to": "kush@billok.email", <br />
            "subject": "test", <br />
            "date": "Tue, 31 May 2022 22:34:46 +0530", <br />
            "messageId": "<CANEUi8jGMKOyHeU7yvsDgg+dnhjNuedqzGDBZ=sB_mOFx55+3A@mail.gmail.com>", <br />
            "text": "test\n\n-- \n*Mannoj Tewari*\n*Founder,* billok.co\n*E: hello@billok.co <hello@billok.co>*\n*M: +91 7400062746*\n\n\n*one place for all your invoices..*\n\n    <https://www.instagram.com/billok.co/>\n<https://twitter.com/billokindia>     <https://www.facebook.com/billokpage>\n    <https://www.linkedin.com/company/billok>\n", <br />
            "attachments": [] <br />
        }, <br />
    ] <br />
} <br />
 <br />
Attachments are "ISO-8859-1 decoded" to strings  <br />
So as to access attachemnts u need to "ISO-8859-1 encode" to bytes and then upload into a file <br />
For example in pythyon:  <br />
with open(f'{fileName}', 'wb') as fp: <br />
    fp.write(coded.encode("ISO-8859-1")) <br />
 <br />
where fileName and coded are the attributes which api offers  <br />
when it encounters an attachment in mail <br />