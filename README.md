# python-easymail

## Overview

Wrapper around smtplib and email.mime libs

## Installation

Clone the project from github

    $ git clone git@github.com:fr33dz/python-easymail.git
    $ cd python-easymail

## How to use it?

Login:

```python
from easymail import EasyMail

m = EasyMail.login('smtp.gmail.com', 'yourname@yourdomain.es', 'yourpassword')

to = 'xxx@xxxxx.com'    #user that you want send an email
subject = 'yoursubject'
body = 'body text'      #you can send HTML text

m.send(to, subject, body)

```
