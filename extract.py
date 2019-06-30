# -*- coding: UTF-8 -*-

# モジュールのインポート
import xml.etree.ElementTree as ET


import glob

#files = glob.glob("./tmp/*")
#for file in files:
#    print(file)

# xmlファイルの読み込み
tree = ET.parse('./01_飲食/1111111.xml')
root = tree.getroot()
root.tag

# 子要素を取得する
for text in root.iter('text'):
    print(text.text)
