# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os
import keyboard

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

path = 'D:/개발/SPARTA1/web_개발/crwaling'
idols = ['강호동 얼굴', '고현정 얼굴', '공유 얼굴', '공효진 얼굴', '김강우 얼굴', '김다미 얼굴', '김대명 얼굴', '김범수 얼굴', '김우빈 얼굴', '김유정 얼굴', '김종국 얼굴', '김태리 얼굴', '김태희', '다니엘헤니 얼굴', '려원 얼굴', '로제 얼굴', '류준열 얼굴', '문채원 얼굴', '박경림', '배두나 얼굴', '뷔 얼굴', '서은광 얼굴', '손예진 얼굴', '송중기 얼굴', '신민아 얼굴', '오지호 얼굴', '윤아 얼굴', '윤은혜 얼굴', '이민정 얼굴', '이병헌 얼굴', '이서진 얼굴', '이솜 얼굴', '이윤석 얼굴', '이이경 얼굴', '임시완 얼굴', '정유미 얼굴', '정지찬 얼굴', '정형돈 얼굴', '존박 얼굴', '청하 얼굴', '태연 얼굴', '트럼프 얼굴', '한소희 얼굴']


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

        try:
            with open(full_path, 'rb') as f:
                data = f.read()
            encoded_img = np.frombuffer(data, dtype=np.uint8)

            # img_array = np.fromfile(full_path, np.uint8)
            img_org = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
            # img_drawn=img_org.copy()
            gray = cv2.cvtColor(img_org, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            if len(faces) > 0 :
                for (x, y, w, h) in faces:
                    cropped = img_org[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)]
                    print(f"{imgNum}사진 face 찾기 성공")
                    # 이미지를 저장
                    # 저장 경로
                    save_path = f'D:/개발/SPARTA1/web_개발/crwaling/face_detection/detection/{idol}'
                    # print(save_path)

                    # cv2.imwrite(os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{imgNum}.png'), cropped)
                    # cv2.imwrite(f"./detection/gain/"+"face" + str(imgNum) + ".png", cropped)

                    response = image_write(f'{save_path}/{imgNum}.png', cropped)
                    if response:
                        print("이미지 저장완료")
                        cv2.destroyAllWindows()
                        pass

                    imgNum += 1

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
    print(f"{idol} 사진찾기 완료")