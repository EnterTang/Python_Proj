#!/usr/bin/python3
# -*- coding:utf-8 -*-

from aip import AipFace
import base64

class FaceRec(object):
    _APP_ID = ''
    _API_KEY = ''
    _SECRET_KEY = ''
    options = {}
    options["max_face_num"] = 5

    def __init__(self, info):
        if 'APP_ID' in info:
            self._APP_ID = info['APP_ID']
        if 'API_KEY' in info:
            self._API_KEY = info['API_KEY']
        if 'SECRET_KEY' in info:
            self._SECRET_KEY = info['SECRET_KEY']
        self.bd_client = AipFace(self._APP_ID, self._API_KEY, self._SECRET_KEY)
        # 设置建立连接超时时间
        self.bd_client.setConnectionTimeoutInMillis(5*1000)
        # 设置传输数据超时时间
        self.bd_client.setSocketTimeoutInMillis(1*1000)

    def __img2base64(self, img_url):
        with open(img_url, "rb") as f:
            base64_str = base64.b64encode(f.read())
            return base64_str

    def face_detect(self, image, imageType):
        img2b64 = self.__img2base64(image)
        img2b64 = str(img2b64, encoding="utf-8")
        result = self.bd_client.detect(img2b64, imageType, self.options)
        return result