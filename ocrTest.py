import cv2
import pytesseract

def cathayOCR(origineImage,resize_num=2,threshold=128,erodeIterationTimes=3,dilateIterationTimes=1,medianBlurKernel=3,isRevert=True):

    isShowImg = True

    # resize
    origineImage = cv2.resize(origineImage,(origineImage.shape[1] * int(resize_num), origineImage.shape[0] * int(resize_num)), interpolation=cv2.INTER_CUBIC)

    # gray
    grayImg = cv2.cvtColor(origineImage, cv2.COLOR_BGR2GRAY)

    # binary
    retval, binImg = cv2.threshold(grayImg, threshold, 255, cv2.THRESH_BINARY_INV)

    # erode
    erodeImg = cv2.erode(binImg, (5, 5), iterations=erodeIterationTimes)

    # dilate
    dilateImg = cv2.dilate(erodeImg, (5, 5), iterations=dilateIterationTimes)

    # medianBlur
    medianBImg = cv2.medianBlur(dilateImg, medianBlurKernel)

    # 反相
    if isRevert:
        resultImg = 255 - medianBImg

    if isShowImg:
        cv2.imshow('oriImg', origineImage)
        cv2.imshow('grayImg', grayImg)
        cv2.imshow('binImg', binImg)
        cv2.imshow('erodeImg', erodeImg)
        cv2.imshow('dilateImg', dilateImg)
        cv2.imshow('medianBlur', medianBImg)
        cv2.imshow('resultImg', resultImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return (pytesseract.image_to_string(resultImg, lang='eng', config='--psm 6 '))

if __name__ == "__main__":
    path = '/Users/moriakiraakira/Desktop/OCR_Sample/數字驗證碼1-2.png'
    origineImage = cv2.imread(path)
    print(cathayOCR(origineImage))