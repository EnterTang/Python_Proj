from PIL import Image

class ImageProcess(object):
    def img_create_obj(self, templete):
        return Image.new(templete.mode, templete.size, (255, 255, 255))

    def img_open(self, filename):
        return Image.open(filename)

    def img_cut(self, in_img, out_img, rect):
        if not isinstance(rect, tuple):
            print("rect is not a tuple")
        else:
            if len(rect) == 4:
                out_img = in_img.crop(rect)
            else:
                print("非法参数")

    def img_cover(self, in_img, rect):
        if not isinstance(rect, tuple):
            print("rect is not a tuple")
        else:
            if len(rect) == 4:
                for x in range(rect[0], rect[1]):
                    for y in range(rect[2], rect[3]):
                        in_img.putpixel((x, y), (128, 128, 128))
                return in_img
            else:
                print("非法参数")

    def img_show(self, in_img):
        in_img.show()


