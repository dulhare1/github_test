import cv2
import pytesseract
import matplotlib.pyplot as plt
import numpy as np
# path = '/Users/moriakiraakira/Desktop/截圖 2020-05-07 下午8.42.04.png'
# im = cv2.imread(path)
# plt.imshow(im)
# plt.show()
#
# print(pytesseract.image_to_string(im))


'''水平投影'''


def getHProjection(image):
    hProjection = np.zeros(image.shape, np.uint8)

    # 圖像高與寬

    (h, w) = image.shape

    # 長度與圖像高度一致的數組

    h_ = [0] * h

    # 循環統計每一行白色像素的個數

    for y in range(h):

        for x in range(w):

            if image[y, x] == 255:
                h_[y] += 1

    # 繪製水平投影圖像

    for y in range(h):

        for x in range(h_[y]):
            hProjection[y, x] = 255

    cv2.imshow('hProjection2', hProjection)

    return h_


def getVProjection(image):
    vProjection = np.zeros(image.shape, np.uint8);

    # 圖像高與寬

    (h, w) = image.shape

    # 長度與圖像寬度一致的數組

    w_ = [0] * w

    # 循環統計每一列白色像素的個數

    for x in range(w):

        for y in range(h):

            if image[y, x] == 255:
                w_[x] += 1

    # 繪製垂直平投影圖像

    for x in range(w):

        for y in range(h - w_[x], h):
            vProjection[y, x] = 255

    # cv2.imshow('vProjection',vProjection)

    return w_


if __name__ == "__main__":

    # 讀入原始圖像

    # path = '/Users/moriakiraakira/Desktop/截圖 2020-05-07 下午8.42.04.png'
    path = '/Users/moriakiraakira/Desktop/截圖 2020-05-08 上午11.03.55.png'

    # path = '/Users/moriakiraakira/PycharmProjects/風管科課程/week1/image_screenshot_29.05.2020.png'
    origineImage = cv2.imread(path)
    print(type(origineImage))
    h,w,c=origineImage.shape
    # print(h,w,c)

    kernel = np.ones((3, 3), np.uint8)

    # 圖像灰度化

    # image = cv2.imread('test.jpg',0)
    resizeImg = cv2.resize(origineImage, (w * 3, h * 3), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('resizeImg', resizeImg)
    image = cv2.cvtColor(resizeImg, cv2.COLOR_BGR2GRAY)

    cv2.imshow('gray', image)

    # 將圖片二值化

    retval, img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

    cv2.imshow('binary', img)

    # 圖像高與寬

    (h, w) = img.shape

    Position = []

    # 水平投影

    H = getHProjection(img)

    start = 0

    H_Start = []

    H_End = []

    # 根據水平投影獲取垂直分割位置

    for i in range(len(H)):

        if H[i] > 0 and start == 0:
            H_Start.append(i)

            start = 1

        if H[i] <= 0 and start == 1:
            H_End.append(i)

            start = 0

    # 分割行，分割之後再進行列分割並保存分割位置

    for i in range(len(H_Start)):

        # 獲取行圖像

        cropImg = img[H_Start[i]:H_End[i], 0:w]

        # cv2.imshow('cropImg',cropImg)

        # 對行圖像進行垂直投影

        W = getVProjection(cropImg)

        Wstart = 0

        Wend = 0

        W_Start = 0

        W_End = 0

        for j in range(len(W)):

            if W[j] > 0 and Wstart == 0:
                W_Start = j

                Wstart = 1

                Wend = 0

            if W[j] <= 0 and Wstart == 1:
                W_End = j

                Wstart = 0

                Wend = 1

            if Wend == 1:
                Position.append([W_Start, H_Start[i], W_End, H_End[i]])

                Wend = 0

    # 秀原圖
    cv2.imshow('originalImg',origineImage)

    print(h, w)
    newImg = np.zeros((480, 1980, 3), np.uint8)
    # 使用白色填充
    newImg.fill(255)


    # 根據確定的位置分割字符
    for m in range(len(Position)):
        # cv2.rectangle(origineImage, (Position[m][0], Position[m][1]), (Position[m][2], Position[m][3]), (0, 229, 238),
        #               1)
        #print('----------------')
        #print('(', Position[m][1], ',', Position[m][3], ')(', Position[m][0], ',', Position[m][2], ')')
        #print('----Separate----')
        # 秀每個字,應該要把空白也當成字元才可算入padding中,否則每個字的間隔相同(只能有字元無法分別單字)
        #cv2.imshow('letter',origineImage[Position[m][1]:Position[m][3],Position[m][0]:Position[m][2]])
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        letterImg = resizeImg[Position[m][1]:Position[m][3],Position[m][0]:Position[m][2]]
        # cv2.imshow('letter', letterImg)
        # dilateImg = cv2.dilate(letterImg, (5, 5), iterations=1)
        # cv2.imshow('dilate', dilateImg)
        # erodeImg = cv2.erode(letterImg, (5, 5), iterations=1)
        # cv2.imshow('erode', erodeImg)
        # print(pytesseract.image_to_string(erodeImg, lang='eng'))
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # 重排
        #padding = 30 * m
        #print('padding:',padding)
        #newImg[Position[m][1]:Position[m][3],padding+Position[m][0]:padding+Position[m][2]]=letterImg
        #print('(',Position[m][1],',',Position[m][3],')(',padding+Position[m][0],',',padding+Position[m][2],')')

        # print(pytesseract.image_to_string(dilateImg, lang='eng'))



    # cv2.imshow('image', letterImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(pytesseract.image_to_string(resizeImg, lang='eng'))
    print('-----')
    print(pytesseract.image_to_string(origineImage, lang='eng'))

    # 圖檔文字
    # Oo00000OOo0o0
    # dfijJILlnmhuwv