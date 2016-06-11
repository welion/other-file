#!/bin/bash

INTERFACE=$1
IP_FILE="/tmp/IP.now.${INTERFACE}"
INTERFACE_IP="inet addr:"
MAIL_FILE="/tmp/mail.txt"

if [ -f $IP_FILE ]; then
        IP_OLD=`cat $IP_FILE`
else
        echo "0.0.0.0" > ${IP_FILE}
        IP_OLD=""
fi
IP_NEW=`ifconfig ${INTERFACE} |grep "${INTERFACE_IP}" |tr ":" " " |awk '{print $3}'`

while true
do
        IP_OLD=`cat ${IP_FILE}`
        IP_NEW=`ifconfig ${INTERFACE} |grep "${INTERFACE_IP}" |tr ":" " " |awk '{print $3}'`
        if [ ${IP_OLD} != ${IP_NEW} ]; then
#               echo "IP_OLD:${IP_OLD}---->IP_NEW:${IP_NEW}...."
                echo ${IP_NEW} > ${IP_FILE}
                echo "IP changed"
                echo "To:353566165@qq.com \n From:auto_pop_mail@sina.com \n Subject:IP-Changed \n \n ${IP_NEW} " > ${MAIL_FILE}

        fi
        sleep 10
done