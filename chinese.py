from nltk.tokenize.stanford_segmenter import StanfordSegmenter 
import jieba
from wxpy import *
import itchat

itchat.auto_login()

itchat.send('韬韬陈，我好喜欢你啊！', toUserName= 'supernova')
# bot = Bot()
# my_friend = bot.friends().search('陈韬', sex=MALE)[0]   # city

# seg_list = jieba.cut("韬韬陈，我好喜欢你啊！", cut_all=True, HMM=False)
# my_friend.send(seg_list)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式

# seg = StanfordSegmenter()
# seg.default_config('zh')

# string = "韬韬陈，我好喜欢你啊！"
# result = seg.segment(string)
# print(result)