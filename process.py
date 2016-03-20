#from __future__ import division
import numpy as np
import scipy.ndimage
#import cv2

class Process:
    def __init__(self):
        pass
        # print self.original_image

    def process_image(self, image_points):
        min_y, min_x, max_y, max_x, width, height = self.get_image_details(image_points)
        img_black = np.zeros((width+1, height+1), np.uint8)
        for x, y in image_points:
            y_val = y - min_y
            x_val = x - min_x
            img_black[x_val][y_val] = 255
        img = scipy.ndimage.zoom(img_black, zoom=(32/(width+1), 32/(height+1)), order=1)
        print(img.shape)
        """
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        """

    def get_image_details(self, points):
        min_x, min_y = points[0] 
        max_x, max_y = points[0]
        
        dist_x, dist_y = 0, 0
        for x, y in points[1:]:
            if y < min_y:
                min_y = y
            if x < min_x:
                min_x = x

            if y > max_y:
                max_y = y
            if x > max_x:
                max_x = x
            
            dist_x, dist_y = max_x - min_x, max_y - min_y
        return min_y, min_x, max_y, max_x, dist_x, dist_y
        # return dist_x, dist_y

def main():
    process = Process()
    image = [(239, 48), (237, 49), (235, 51), (233, 52), (231, 54), (227, 55), (225, 57), (221, 58), (216, 60), (212, 61), (205, 62), (202, 64), (196, 64), (191, 66), (184, 69), (178, 70), (172, 72), (165, 74), (158, 76), (152, 79), (145, 82), (139, 85), (131, 88), (126, 90), (120, 93), (113, 97), (107, 99), (101, 101), (95, 103), (89, 106), (84, 109), (78, 111), (72, 114), (68, 115), (63, 118), (59, 120), (54, 121), (50, 123), (47, 125), (45, 126), (43, 127), (40, 129), (38, 130), (37, 131), (36, 132), (35, 133), (35, 135), (36, 140), (42, 145), (46, 149), (53, 153), (61, 159), (68, 164), (76, 170), (98, 177), (110, 183), (122, 191), (131, 195), (141, 201), (150, 204), (161, 209), (170, 213), (179, 216), (189, 221), (197, 224), (206, 228), (212, 231), (221, 234), (228, 237), (233, 239), (237, 240), (240, 240), (243, 242), (245, 242)]
    asdf = process.process_image(image)

if __name__ == '__main__':
    main()