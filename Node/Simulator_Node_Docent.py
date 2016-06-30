#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import threading
import time
import json

import NIT_Node_Module
from terminalColor import bcolors

NodeUUID = "NODEDOCENT@NODE-5ac42c3c-3df3-11e6-ac61-9e71128cae77"
# NodeUUID ="NODE-" +uuid.uuid1()

Functions = []
NodeFunctions = ['TOUR']

print("::::::::::::::::::::::::::::::::::::::::::\n")
print("::::::::::::::::::::::::::::::::::::::::::\n")
print("'##::: ##::'#######::'########::'########:")
print(" ###:: ##:'##.... ##: ##.... ##: ##.....::")
print(" ####: ##: ##:::: ##: ##:::: ##: ##:::::::")
print(" ## ## ##: ##:::: ##: ##:::: ##: ######:::")
print(" ##. ####: ##:::: ##: ##:::: ##: ##...::::")
print(" ##:. ###: ##:::: ##: ##:::: ##: ##:::::::")
print(" ##::. ##:. #######:: ########:: ########:")
print("..::::..:::.......:::........:::........::")
print("::::::::::::::::::::::::::::::::::::::::::\n")

nit = NIT_Node_Module.NIT_Node(NodeUUID, Functions, NodeFunctions) #設定自己的值與需求功能


# Connect to MQTT Server for communication
def NodeToServerMQTTThread():
    # print("thread name：　" + threading.current_thread().getName())

    # callback
    nit.CallBackRxRouting = RxRouting
    print(bcolors.HEADER + '===============================================\n' + bcolors.ENDC)
    print(bcolors.HEADER + '---------------Node(%s)--->>>Server in MQTT-\n' % NodeUUID + bcolors.ENDC)
    print(bcolors.HEADER + '>>>Start connect Server %s<<<' % (
        time.asctime(time.localtime(time.time()))) + bcolors.ENDC)
    print(bcolors.HEADER + '===============================================\n' + bcolors.ENDC)
    print(bcolors.HEADER + 'Register to IoT Server successful! \n' + bcolors.ENDC)#之後開始跑出info

    try:
        nit.RegisterNoode();



    except (RuntimeError, TypeError, NameError) as e:
        print(bcolors.FAIL + "[INFO]Register error." + str(e) + bcolors.ENDC)
        raise
        sys.exit(1)
0.0

########### Keyboard interactive ##############
def RxRouting(self, _obj_json_msg):
    nit.M2M_RxRouting(_obj_json_msg)

global msg



global flip
def loop():
    global flip
    decide = "g"
    decide = input("enter 'TALK' to trigger")
    print(decide)
    if(decide=='TALK'):
        msg=input()

    initMSGObj = {'TopicName': "NODEDOCENT@NODE-5ac42c3c-3df3-11e6-ac61-9e71128cae77", 'Control': "CALL", 'Source': "NODEDOCENT@NODE-5ac42c3c-3df3-11e6-ac61-9e71128cae77", 'M2M_Value': flip, 'MSG': msg}
    initMSGSTR = json.dumps(initMSGObj)

    if (decide == "TALK"):
        nit.DirectMSG("NODEDOCENT@NODE-5ac42c3c-3df3-11e6-ac61-9e71128cae77", initMSGSTR)
        print("CALL PEOPLE")
        flip = (~flip)



if __name__ == "__main__":
    MQTT_Thread = threading.Thread(target=NodeToServerMQTTThread, name="main_thread")
    MQTT_Thread.start()
    global flip
    flip = 0
    while True:
        loop()
