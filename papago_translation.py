import keras_ocr
import matplotlib.pyplot as plt
import requests

# keras-ocr은 감지기와 인식기에 대한 사전 훈련된 가중치를 자동으로 다운로드합니다.
pipeline = keras_ocr.pipeline.Pipeline()

# 예시 이미지 목록
images = [keras_ocr.tools.read('C:/Users/halo0/Desktop/et.jpg')]

# 형태 출력
import numpy as np
print(np.shape(images))

# 예측 그룹 내 각 예측의 목록은 (단어, 상자) 튜플의 목록입니다.
prediction_groups = pipeline.recognize(images)

# 예측 그림
fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
axs = [axs] if len(images) == 1 else axs  # axs가 반복 가능한 형태가 되도록 설정합니다.
for ax, image, predictions in zip(axs, images, prediction_groups):
    keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)

# 인식된 텍스트 출력
ImgText = []
for predictions in prediction_groups:
    for text, _ in predictions:
        print(text)
        ImgText.append(text)

# Papago API를 사용하여 텍스트 번역
translated_text = []
for text in ImgText:
    url = "https://openapi.naver.com/v1/papago/n2mt"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Naver-Client-Id": "PFUMe9nWJs7AzKwPSie6",
        "X-Naver-Client-Secret": "PxexPploT9"
    }
    data = {
        "source": "en",
        "target": "ko",
        "text": text
    }
    response = requests.post(url, headers=headers, data=data)
    result = response.json()
    translated_text.append(result['message']['result']['translatedText'])

print(translated_text)
plt.show()
