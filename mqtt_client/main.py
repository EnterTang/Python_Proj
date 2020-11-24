from mqtt_tet.mqtt_client import MQTT
from cbk_process import CBK_Process
from sys_tools.sys_tools import SysTools
from database import *
import os, json
import sys
from QT_GUI.PyQT5 import GUI_Qwidget, GUI_Qapp, GUI_QMainWindow

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
            sub_topic["sub_sn"] = jsFile["sub_sn"]
        if "sub_no_sn" in jsFile:
            # sub_no_sn_lst = {}
            # for i in jsFile["sub_no_sn"].items():
            sub_topic["sub_no_sn"] = jsFile["sub_no_sn"]

def auto_sub(mqtt):
    jsData = {
        "type": "subTopics",
        "topics":[]
    }
    if "sub_sn" in sub_topic:
        if "sn" in device_info:
            for i in sub_topic["sub_sn"]:
                mix_topic = i + device_info["sn"]
                mqtt.mqtt_sub_topic(mix_topic)
                jsData["topics"].append(mix_topic)
    if "sub_no_sn" in sub_topic:
        for j in sub_topic["sub_no_sn"]:
            mqtt.mqtt_sub_topic(j)
            jsData["topics"].append(j)
    print(jsData)
    return jsData


if __name__ == '__main__':
    # 注册观察者
    observer = Observer()

    sys_tools = SysTools()
    cbk_funcs = CBK_Process(observer)
    mqtt = MQTT()

    app = GUI_Qapp()
    gui_main = GUI_QMainWindow()
    gui_main.show()

    observer.attach(gui_main)

    mqtt_get_conf('config.json')

    mqtt.mqtt_config(mqtt_info)
    mqtt.mqtt_set_cbk(cbk_funcs.mqtt_cbk_conn, cbk_funcs.mqtt_cbk_msg_recv)
    mqtt.mqtt_create_conn()
    mqtt.mqtt_create_process()
    '''
    sub topic here
    '''
    jsData = auto_sub(mqtt)
    observer.data = jsData
    sys.exit(app.exec_())

