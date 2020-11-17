from mqtt_tet.mqtt_client import MQTT
from cbk_process import CBK_Process as cbk_funcs

if __name__ == '__main__':
    mqtt_info = {
        "Server":"www.entertang.icu",
        "Port":1883,
        "username":"admin",
        "pwd": "admin"
    }
    mqtt = MQTT()
    mqtt.mqtt_config(mqtt_info)
    mqtt.mqtt_set_cbk(cbk_funcs.mqtt_cbk_conn, cbk_funcs.mqtt_cbk_msg_recv)
    mqtt.mqtt_create_conn()
    mqtt.mqtt_create_process()
    mqtt.mqtt_sub_topic("/python/test/aaa")
    mqtt.mqtt_pub_topic("/python/test/helloworld", "helloworld!!!")
    while True:
        if input("请输入q退出。。。") == 'q':
            break

