#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import threading
import time
import json

import NIT_Node_Module
from terminalColor import bcolors

NodeUUID = "NODE-SP"
# NodeUUID ="NODE-" +uuid.uuid1()

Functions = ["LED1", "LED2"]
NodeFunctions = ['IOs','Animal_Data']

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




#之後的Trigger設計
global flip
def loop():
    global flip
    decide = "g"
    decide = input("Enter 't' to call Docent.......")
    print(decide)

    initMSGObj = {'TopicName': "FS2", 'Control': 'CALL', 'Source': "NODE-SP", 'M2M_Value': flip}
    initMSGSTR = json.dumps(initMSGObj)

    if (decide == "t"):
        nit.DirectMSG("NODE-SP", initMSGSTR)
        print("SW01 SENT.")
        flip = (~flip)



if __name__ == "__main__":
    MQTT_Thread = threading.Thread(target=NodeToServerMQTTThread, name="main_thread")
    MQTT_Thread.start()
    global flip
    flip = 0
    while True:
        loop()
