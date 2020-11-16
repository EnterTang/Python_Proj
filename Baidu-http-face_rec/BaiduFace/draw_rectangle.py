import cv2
def draw_rect(image_url, coordinate, face_nums):
    image = cv2.imread(image_url)
    for i in range(0, face_nums):
        cv2.rectangle(image,
            (int(coordinate["data"][i]["xmin"]),int(coordinate["data"][i]["ymin"])),
            (int(coordinate["data"][i]["xmax"]),int(coordinate["data"][i]["ymax"])),
            (0, 0, 255),
            1
            )
    cv2.imwrite("out.jpg", image)