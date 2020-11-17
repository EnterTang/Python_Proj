class CBK_Process(object):
    def mqtt_cbk_conn(self, client, userdata, flags, rc):
        print("\nConnected with result code " + str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("/python/test")

    def mqtt_cbk_msg_recv(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))