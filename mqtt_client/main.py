from mqtt_tet.mqtt_client import MQTT

if __name__ == '__main__':
    mqtt_info = {"Server":"www.entertang.icu", "Port":1883}
    mqtt = MQTT()
    mqtt.mqtt_config(mqtt_info)
    mqtt.mqtt_set_cbk()
    mqtt.mqtt_create_conn()
    mqtt.mqtt_create_process()
    print("xxxxxx 1")
    mqtt.mqtt_sub_topic("/python/test/aaa")
    mqtt.mqtt_pub_topic("/python/test/helloworld", "helloworld!!!")
    while True:
        if input("请输入q退出。。。") == 'q':
            break

