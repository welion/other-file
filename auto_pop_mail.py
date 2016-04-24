# -*- coding: utf-8 -*-
#!/usr/bin/env python
import smtplib
import string
HOST = "smtp.163.com"
SUBJECT = "测试邮件，来自python"
TO = "353566165@qq.com"
FROM = "welion_zhong@163.com"
TEXT = "哈哈哈啊哈哈哈哈"
BODY = string.join((
    "FROM: %s" % FROM,
    "TO: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",TEXT),"\r\n")
server = smtplib.SMTP()
server.connect(HOST,"25")
server.login("welion_zhong@163.com","zwh123@163")
server.sendmail(FROM, [TO], BODY)
server.quit
