import multiprocessing
import paho.mqtt.client as mqtt

class MQTT(object):
    client = mqtt.Client()
    mqtt_config_flag = 0

    def mqtt_config(self, info):
        if 'Server' in info:
            self.server = info['Server']
        else:
            self.server = '47.110.80.10'
        if 'Port' in info:
            self.port = info['Port']
        else:
            self.port = 1883

        self.mqtt_config_flag |= 0x01
        if 'username' in info:
            self.username = info['username']
        if 'pwd' in info:
            self.pwd = info['pwd']

    def mqtt_set_cbk(self, cbk_conn, cbk_msg_recv):
        self.client.on_connect = cbk_conn
        self.client.on_message = cbk_msg_recv

        self.mqtt_config_flag |= 0x02

    def mqtt_create_conn(self):
        if (self.mqtt_config_flag & 0x01) ^ 0x01:
            print(self.mqtt_config_flag)
            print("未设置mqtt broker等，请检查配置后重试!!!")
        else:
            if(hasattr(self, "username") and hasattr(self, "pwd")):
                self.client.username_pw_set(self.username, self.pwd)
            self.client.connect(self.server, self.port, 60)

        self.mqtt_config_flag |= 0x04

    def mqtt_sub_topic(self, topic):
        self.client.subscribe(topic)
    def mqtt_pub_topic(self, topic, payload):
        self.client.publish(topic, payload)

    def __mqtt_loop(self):
        self.client.loop_start()

    def mqtt_create_process(self):
        if self.mqtt_config_flag ^ 0x07:
            print("请先检查是否完成配置！！！")
        else:
           p1 = multiprocessing.Process(target=self.__mqtt_loop())
           p1.start()
