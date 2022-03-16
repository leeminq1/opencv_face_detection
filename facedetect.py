import cv2
import numpy as np
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

path = 'D:/개발/SPARTA1/web_개발/crwaling'
idols = ['가인 얼굴', '강호동 얼굴']


def image_write(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False



for idol in idols:
    os.mkdir(f'./detection/{idol}')
    print(f"{idol} 폴더가 생성되었습니다.")
    imgNum = 1
    while imgNum <= 199:

        full_path = f"{path}/{idol}/{imgNum}.jpg"

        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        try:
            if len(faces) > 0 :
                for (x, y, w, h) in faces:
                    print(f"{imgNum}사진 face 찾기 성공")
                    cropped = img[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)]
                    # 이미지를 저장
                    # 저장 경로
                    save_path = f'D:/개발/SPARTA1/web_개발/crwaling/face_detection/detection/{idol}'
                    # print(save_path)

                    # cv2.imwrite(os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{imgNum}.png'), cropped)
                    # cv2.imwrite(f"./detection/gain/"+"face" + str(imgNum) + ".png", cropped)

                    response=image_write(f'{save_path}/{imgNum}.png',cropped)
                    # cv2.imwrite(f"./detection/{imgNum}.png", cropped)
                    if response:
                        print("이미지 저장")
                    imgNum += 1
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    cv2.imshow('Image view', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    # roi_gray = gray[y:y+h, x:x+w]
                    # roi_color = img[y:y+h, x:x+w]
                    # eyes = eye_casecade.detectMultiScale(roi_gray)
                    # for (ex, ey, ew, eh) in eyes:
                    #     cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),(0,255,0),2)
            else:
                print(f"{imgNum}사진 face 찾기 실패")
                imgNum += 1
        except:
            print("error 발생")
            imgNum += 1
            pass
