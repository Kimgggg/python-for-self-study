# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import sys
import SetDef
import SetClass
import Image
import types
import itertools
import hashlib
import urllib2
import HTMLParser
import re
import socket

# key = raw_input('是否要查询斐波那契数列？按y/n查询，其他键退出\n')
# if ord(key) == 121:
# 	SetDef.Fib(key)
# else:
# 	raw_input("Press any key to Exit: ")
# 未调通


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('To: ')
smtp_server = raw_input('SMTP server: ')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

      
