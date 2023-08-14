import easyocr
import matplotlib.pyplot as plt

# EasyOCR 인스턴스 생성
reader = easyocr.Reader(['ch_sim'])

# 이미지 읽기
image_path = 'C:/Users/halo0/Desktop/et.jpg'

# 중국어 텍스트 인식
result = reader.readtext(image_path)

# 인식된 텍스트 출력
for detection in result:
    text = detection[1]
    print(text)

# 이미지 표시
image = plt.imread(image_path)
plt.imshow(image)
plt.show()
