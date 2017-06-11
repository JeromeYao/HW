#coding:utf-8
#Filename:Wordclould.py


import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
#wordcloud和jieba同时支持py2.x和py3.x。
text_from_file_with_apath = open('/home/jerome/Documents/test.txt').read()

#修改wordcloud.py文件中一下这行：
# FONT_PATH = os.environ.get("FONT_PATH", os.path.join(os.path.dirname(__file__), "DroidSansMono.ttf"))
#以适配中文字体 可以改为 wqy-microhei.ttc。

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud().generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
