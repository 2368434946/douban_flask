#-*- codeing = utf-8 -*-
#@Time : 2021/3/31 13:49
#@Author : 刘也
#@File : testCloud.PY
#@Software : PyCharm

import jieba  #分词
from matplotlib import pyplot as plt #绘图，数据可视化
from wordcloud import WordCloud  #词云
from PIL import Image   #图片处理
import numpy as np      #矩阵运算
import sqlite3       #数据库


#准备词云所需的文字
con = sqlite3.connect('movie.db')
cul = con.cursor()
sql = 'select instroduction from movie250'
data = cul.execute(sql)
text = ""
for item in data:
    text = text + item[0]
    # print(item[0])
    # print(text)
cul.close()
con.close()


cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))
#打开遮罩图片
img = Image.open(r'.\static\assets\img\tree.jpg')
#将图片转换为数组
img_array = np.array(img)

wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="msyh.ttc"
)
wc.generate_from_text(string)



#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
#是否显示坐标轴
plt.axis('off')
#显示生成的词云图片
#plt.show()
#输出词云图片到文件
plt.savefig(r'.\static\assets\img\word.jpg',dpi=500)