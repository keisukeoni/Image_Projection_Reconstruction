# coding: utf-8
from PIL import Image
import numpy as np

#Python2
#グレースケール
#サイノグラムを読み込んでNumpy配列に変換
sinogramImg = Image.open('sinogram.bmp')
sinogramImgArray = np.asarray(sinogramImg)
#print sinogramImg.size (363, 720)
sinoWidth, sinoHeight = sinogramImg.size

reconstraction = np.zeros((sinoWidth, sinoWidth), dtype=np.int)

for i in range(sinoHeight):
	sinoTmpArray = np.zeros((sinoWidth, sinoWidth), dtype=np.int)
	print i
	for j in range(sinoWidth):
		sinoTmpArray[j] = sinogramImgArray[i]
	sinoTmpImg = Image.fromarray(np.uint8(sinoTmpArray))
	sinoTmpImg = sinoTmpImg.rotate(-i/4)
	sinoTmpArray = np.asarray(sinoTmpImg)
	for k in range(sinoWidth):
		for l in range(sinoWidth):
			reconstraction[k][l] += sinoTmpArray[k][l]

for i in range(sinoWidth):
	for j in range(sinoWidth):
		reconstraction[i][j] = int(reconstraction[i][j] / sinoHeight)

img = Image.fromarray(np.uint8(reconstraction))
img.save('reconstraction.bmp')
