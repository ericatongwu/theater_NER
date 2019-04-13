import jieba
import jieba.posseg as pseg

text = """
外婆从轮椅上站起来，企图追过去.
"""

default = jieba.cut(text, cut_all=False, HMM=True)
words =pseg.cut(text)

# print("Default Mode: " + "/ ".join(default))  # default mode
for word in words:
	print(word, word.flag)