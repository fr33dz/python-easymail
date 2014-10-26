# python-easymail

## Overview

Wrapper around smtplib and email.mime libs

## Installation

Clone the project from github

    $ git clone git@github.com:iocio005/python-easymail.git
    $ cd python-easymail

## How to use it?

Login:

```python
from easymail import EasyMail

m = EasyMail.login('yourname@yourdomain.es', 'yourpassword')

to = 'xxx@xxxxx.com'    #user that you want send an email
subject = 'yoursubject'
body = 'body text'

m.send(to, subject, body)
```

## Changelog
## 0.1

**26th Oct 2014**

* First release
* Gmail, Outlook, Hotmail and Yahoo support
