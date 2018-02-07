# coding: utf-8
from PIL import Image
import numpy as np
import math

#Python2
#グレースケール専用
#画像を読み込む
img = Image.open('target.bmp')

#読み込んだ画像がグレースケールでなかったらグレースケールへ変換
if img.mode != 'L':
	img = img.convert('L')

#画像の縦横の取得
originalWidth, originalHeight = img.size

newImgSize = int(math.sqrt(originalWidth * originalWidth + originalHeight * originalHeight) + 1)

#画像貼り付け位置
pasteLocationWidth = int((newImgSize - originalWidth) / 2)
pasteLocationHeight = int((newImgSize - originalHeight) / 2)

img2 = Image.new('L', (newImgSize, newImgSize), 0)
img2.paste(img, (pasteLocationWidth, pasteLocationHeight))

sinogramImg = []
#0.25度ずつ720回回転
for i in range(720):
	imgTmp = img2.rotate(i/4)
	imgArray = np.asarray(imgTmp)
	sinogramImgTmp = []
	for j in range(newImgSize):
		imgArraySum = 0
		for k in range(newImgSize):
			imgArraySum += imgArray[k][j]
		#imgArraySum = int(imgArraySum / newImgSize)
		imgArraySum = int(imgArraySum / originalHeight)
		sinogramImgTmp.append(imgArraySum)
	sinogramImg.append(sinogramImgTmp)

#サイノグラムにする２次元配列の最大値を求めて正規化
#argmax=lambda A:np.unravel_index(np.array(A).argmax(), np.array(A).shape)
#h, w = argmax(sinogramImg)
#max = sinogramImg[h][w]
#for i in range(720):
#	for j in range(newImgSize):
#		sinogramImg[i][j] = int(sinogramImg[i][j] * 255 / max)

#サイノグラム作成
sinogramImg = np.array(sinogramImg)
sinogramImg = Image.fromarray(np.uint8(sinogramImg))
sinogramImg.save('sinogram.bmp')
