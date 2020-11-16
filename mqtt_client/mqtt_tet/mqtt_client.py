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

    def mqtt_set_cbk(self):
        self.client.on_connect = self.__on_connect
        self.client.on_message = self.__on_message

        self.mqtt_config_flag |= 0x02

    def mqtt_create_conn(self):
        if (self.mqtt_config_flag & 0x01) ^ 0x01:
            print(self.mqtt_config_flag)
            print("未设置mqtt broker等，请检查配置后重试!!!")
        else:
            self.client.connect(self.server, self.port, 60)

        self.mqtt_config_flag |= 0x04

    def mqtt_sub_topic(self, topic):
        self.client.subscribe(topic)
    def mqtt_pub_topic(self, topic, payload):
        self.client.publish(topic, payload)

    def __mqtt_loop(self):
        self.client.loop_start()

    def __on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("/python/test")

    # The callback for when a PUBLISH message is received from the server.
    def __on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

    def mqtt_create_process(self):
        if self.mqtt_config_flag ^ 0x07:
            print("请先检查是否完成配置！！！")
        else:
           p1 = multiprocessing.Process(target=self.__mqtt_loop())
           p1.start()