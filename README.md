# python-easymail

## Overview

Wrapper around smtplib and email.mime libs

## Installation

Clone the project from github

    $ git clone git@github.com:fr33dz/python-easymail.git
    $ cd python-easymail

## How to use it?


```python
def main():
    m = EasyMail('yacine.bs1@gmail.com', 'yourpassword', 'smtp.gmail.com')

    to = 'yacine.bs2@gmail.com'    #user that you want send an email
    subject = 'test smtp'
    body = '<h2> Hello world :p </h2>'      #you can send HTML text

    m.send(to, subject, body)

if __name__ == "__main__":
    main()

```
