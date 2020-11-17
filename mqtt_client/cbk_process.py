from database import *
import json
class CBK_Process(object):
    def mqtt_cbk_conn(self, client, userdata, flags, rc):
        print("\nConnected with result code " + str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("/python/test")

    def mqtt_cbk_msg_recv(self, client, userdata, msg):
        output_flag = 1
        jsData = json.loads(str(msg.payload, encoding='utf-8'))

        if msg.topic in sub_topic["sub_no_sn"]:
            for i in sub_topic["sub_no_sn"][msg.topic]:
                if i in jsData:
                    if sub_topic["sub_no_sn"][msg.topic][i] == jsData[i]:
                        output_flag = 1
                    else:
                        output_flag = 0
                        break
                else:
                    # 如果payload里无这个参数，可以选择放他一马，也可以不放
                    # output_flag = 0
                    pass
        else:
            output_flag = 1

        if output_flag == 1:
            print('------------------------------------\n' + \
                  'topic: {}\n'.format(msg.topic) + \
                  'payload: {}\n'.format(json.dumps(jsData, sort_keys=True, indent=4, separators=(',', ':'))) + \
                  '------------------------------------\n'
                  )