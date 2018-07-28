from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from os import path
import matplotlib.pyplot as plt
import jieba
import jieba.posseg as pseg
from PIL import Image
import numpy as np
d = path.dirname(__file__)
stopwords = set(STOPWORDS)
# 中文分词处理
def processChinese(text):  
    seg_generator = jieba.cut(text)
    seg_list = [i for i in seg_generator if i not in stopwords]  # 排除stopwords
    seg_list = [i for i in seg_list if i != '\n']  # 排除换行
    seg_list = r' '.join(seg_list)
    return seg_list

def  main():
    # 读取文本
    text = open('short.txt', encoding = 'utf-8').read()
    # 读取图片
    alice_mask = np.array(Image.open(path.join(d, "xx.png")))
    # jieba分词
    text = processChinese(text)
    fontpath = "./SourceHanSerifK-Light.otf"
    wordcloud = WordCloud(font_path = fontpath,background_color='white',mask=alice_mask,max_words=200).generate(text)
    # 绘制
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

main()