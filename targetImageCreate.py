# coding: utf-8
from PIL import Image
from PIL import ImageDraw

#Python2
#画像を作成(グレースケール)
width = 256
height = 256

img = Image.new('L', (width, height), 0)

#図形描画
dr = ImageDraw.Draw(img)

#四角を描画
dr.rectangle(((130,50),(230,150)), outline=128, fill=128)

#三角を描画
dr.polygon(((85, 140), (45, 230), (140, 230)), fill=64, outline=64)

#丸を描画
dr.ellipse(((50,50),(90,90)),outline=240 ,fill=240)

#画像を保存
img.save('target.bmp')
