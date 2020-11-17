from mqtt_tet.mqtt_client import MQTT
from cbk_process import CBK_Process
from sys_tools.sys_tools import SysTools
from database import *
import os, json

def mqtt_get_conf(filename):
    jsFile = sys_tools.get_conf_from_files('config.json')
    if jsFile != -1:
        if "basedata" in jsFile:
            if "Server" in jsFile["basedata"]:
                mqtt_info["Server"] = jsFile["basedata"]["Server"]
            if "Port" in jsFile["basedata"]:
                mqtt_info["Port"] = jsFile["basedata"]["Port"]
            if "username" in jsFile["basedata"]:
                mqtt_info["username"] = jsFile["basedata"]["username"]
            if "pwd" in jsFile["basedata"]:
                mqtt_info["pwd"] = jsFile["basedata"]["pwd"]
        if "device_sn" in jsFile:
            device_info["sn"] = jsFile["device_sn"]

        if "sub_sn" in jsFile:
            sub_sn_lst = []
            for i in jsFile["sub_sn"]:
                sub_sn_lst.append(i)
            sub_topic["sub_sn"] = sub_sn_lst
        if "sub_no_sn" in jsFile:
            # sub_no_sn_lst = {}
            # for i in jsFile["sub_no_sn"].items():
            sub_topic["sub_no_sn"] = jsFile["sub_no_sn"]

def auto_sub(mqtt):
    if "sub_sn" in sub_topic:
        if "sn" in device_info:
            for i in sub_topic["sub_sn"]:
                mix_topic = i + device_info["sn"]
                print(mix_topic)
                mqtt.mqtt_sub_topic(mix_topic)
    if "sub_no_sn" in sub_topic:
        for j in sub_topic["sub_no_sn"]:
            mqtt.mqtt_sub_topic(j)

if __name__ == '__main__':
    sys_tools = SysTools()
    cbk_funcs = CBK_Process()
    mqtt = MQTT()

    mqtt_get_conf('config.json')

    mqtt.mqtt_config(mqtt_info)
    mqtt.mqtt_set_cbk(cbk_funcs.mqtt_cbk_conn, cbk_funcs.mqtt_cbk_msg_recv)
    mqtt.mqtt_create_conn()
    mqtt.mqtt_create_process()
    '''
    sub topic here
    '''
    auto_sub(mqtt)
    # mqtt.mqtt_sub_topic("/python/test/aaa")
    # mqtt.mqtt_pub_topic("/python/test/helloworld", "helloworld!!!")
    while True:
        if input("请输入q退出...") == 'q':
            break

