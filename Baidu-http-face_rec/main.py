from BaiduFace.FaceRecognition import FaceRec as BaiduFace
from BaiduFace.draw_rectangle import draw_rect
img_url = "test.jpg"
img_type = "BASE64"

if __name__ == '__main__':
    bd_face_info = {"APP_ID":"11549015",
                    "API_KEY":"ALkDC3iwU2sCmnB9QrXt9rDO",
                    "SECRET_KEY":"E0y8p6C7Ml4ptRsduA5cufeudDPDL877"}
    bd_face = BaiduFace(bd_face_info)
    detect_result = bd_face.face_detect(img_url, img_type)
    #print(detect_result)
    face_nums = int(detect_result["result"]["face_num"])
    coordinate = {"data":[{},{},{},{},{}]}
    for i in range(0, face_nums):
        coordinate["data"][i]["xmin"] = detect_result["result"]["face_list"][i]["location"]["left"]
        coordinate["data"][i]["ymin"] = detect_result["result"]["face_list"][i]["location"]["top"]
        coordinate["data"][i]["xmax"] = coordinate["data"][i]["xmin"] + detect_result["result"]["face_list"][i]["location"]["width"]
        coordinate["data"][i]["ymax"] = coordinate["data"][i]["ymin"] + detect_result["result"]["face_list"][i]["location"]["height"]

    draw_rect(img_url, coordinate, face_nums)

