#!/usr/bin/python
# -*- coding: utf-8 -*-
from threading import Thread

__author__ = 'Nathaniel'

import json
import copy
import sys
from terminalColor import bcolors
import class_AnimalFS_MQTTManager


# 上層目錄
sys.path.append("..")
import config_ServerIPList

_g_cst_MQTTRegTopicName = "IOTSV/REG"  # 一開始要和IoT_Server註冊，故需要傳送信息至指定的MQTT Channel
_g_cst_FSUUID = "FSZOOGUIDE@FS-a119ec6e-3df6-11e6-ac61-9e71128cae77"


# _globalGWList = []


print(bcolors.HEADER + ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::" + bcolors.ENDC)
print(bcolors.HEADER + ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::" + bcolors.ENDC)
print(bcolors.HEADER + "':::'###::::'##::: ##:'####:'##::::'##::::'###::::'##:::::::::::'######:::'##::::'##:'####:'########::'########:" + bcolors.ENDC)
print(bcolors.HEADER + " ::'## ##::: ###:: ##:. ##:: ###::'###:::'## ##::: ##::::::::::'##... ##:: ##:::: ##:. ##:: ##.... ##: ##.....::" + bcolors.ENDC)
print(bcolors.HEADER + " :'##:. ##:: ####: ##:: ##:: ####'####::'##:. ##:: ##:::::::::: ##:::..::: ##:::: ##:: ##:: ##:::: ##: ##:::::::" + bcolors.ENDC)
print(bcolors.HEADER + " '##:::. ##: ## ## ##:: ##:: ## ### ##:'##:::. ##: ##:::::::::: ##::'####: ##:::: ##:: ##:: ##:::: ##: ######:::" + bcolors.ENDC)
print(bcolors.HEADER + " #########: ##. ####:: ##:: ##. #: ##: #########: ##:::::::::: ##::: ##:: ##:::: ##:: ##:: ##:::: ##: ##...::::" + bcolors.ENDC)
print(bcolors.HEADER + " ##.... ##: ##:. ###:: ##:: ##:.:: ##: ##.... ##: ##:::::::::: ##::: ##:: ##:::: ##:: ##:: ##:::: ##: ##:::::::" + bcolors.ENDC)
print(bcolors.HEADER + " ##:::: ##: ##::. ##:'####: ##:::: ##: ##:::: ##: ########::::. ######:::. #######::'####: ########:: ########:" + bcolors.ENDC)
print(bcolors.HEADER + ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n" + bcolors.ENDC)
print(bcolors.HEADER + ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n" + bcolors.ENDC)


def main():
    REGMSG = '{"FunctionServer":"%s", "Control":"FS_REG",' \
             '"Function":"Guide","FSIP":"10.0.0.2" ,"MappingNodes":"TOUR", "Source":"%s"}' % \
             (_g_cst_FSUUID, _g_cst_FSUUID)

    publisherManger = class_AnimalFS_MQTTManager.PublisherManager()
    publisherManger.MQTT_PublishMessage(_g_cst_MQTTRegTopicName, REGMSG)

    # 訂閱自身名稱topic
    class_AnimalFS_MQTTManager.SubscriberThreading(_g_cst_FSUUID).start()


if __name__ == '__main__':
    main()
