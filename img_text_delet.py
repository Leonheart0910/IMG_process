
import matplotlib.pyplot as plt
import keras_ocr
import cv2
import math
import numpy as np
#일반적인 접근법...
#keras OCR을 사용하여 텍스트를 감지하고, 텍스트 주위에 마스크를 정의하고, 그림을 그릴 수 있습니다
#텍스트를 제거할 영역을 지정합니다.
#마스크를 적용하기 위해서는 시작과 시작의 좌표를 제공해야 합니다
# 라인의 끝점 및 라인의 두께

#시작점은 왼쪽 상단 모서리와
#상자의 왼쪽 하단 모서리.
#끝점은 오른쪽 상단 모서리와 오른쪽 하단 모서리 사이의 중간점이 됩니다.
#다음 함수는 정확히 수행

def midpoint(x1, y1, x2, y2):
    x_mid = int((x1 + x2)/2)
    y_mid = int((y1 + y2)/2)
    return (x_mid, y_mid)

#텍스트와 인페인팅을 감지하는 메인 기능.
#입력은 이미지 경로 및 kreas_ocr 파이프라인입니다
def inpaint_text(img_path, pipeline):
    # read the image 
    img = keras_ocr.tools.read(img_path) 
    
# 텍스트(및 해당 영역) 인식
# prediction_groups의 각 예측 목록은 다음과 같습니다
# (단어, 상자) 튜플.
    prediction_groups = pipeline.recognize([img])
    
    #Define the mask for inpainting
    mask = np.zeros(img.shape[:2], dtype="uint8")
    for box in prediction_groups[0]:
        x0, y0 = box[1][0]
        x1, y1 = box[1][1] 
        x2, y2 = box[1][2]
        x3, y3 = box[1][3] 
        
        x_mid0, y_mid0 = midpoint(x1, y1, x2, y2)
        x_mid1, y_mi1 = midpoint(x0, y0, x3, y3)
        
#라인 두께에 대해 다음 사이의 라인 길이를 계산합니다
#왼쪽 상단 모서리와 왼쪽 하단 모서리.
        thickness = int(math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 ))
        
        #Define the line and inpaint
        cv2.line(mask, (x_mid0, y_mid0), (x_mid1, y_mi1), 255,    
        thickness)
        inpainted_img = cv2.inpaint(img, mask, 7, cv2.INPAINT_NS)
                 
    return(inpainted_img)

# keras-ocr은 자동으로 사전 훈련된 상태로 다운로드됩니다
# 검출기 및 인식기에 대한 가중치.
pipeline = keras_ocr.pipeline.Pipeline()

img_text_removed = inpaint_text('C:/Users/halo0/Desktop/et.jpg', pipeline)

plt.imshow(img_text_removed)

cv2.imwrite('text_removed_image.jpg', cv2.cvtColor(img_text_removed, cv2.COLOR_BGR2RGB))