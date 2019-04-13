import jieba
import jieba.posseg as pseg
from jieba import tokenize
import thulac

# removes all character name and puncutation

def remove_stopwords(script, stopwords):

	script_after_remove = []
	with open(stopwords) as sw:
		stopwords_list = sw.readlines()
	stopwords_list = [x.strip() for x in stopwords_list] 

	with open(script) as s:
		script_list = s.readlines()
	script_list = [y.strip() for y in script_list] 

	for line in script_list:
		# line = pseg.cut(line)
		line = jieba.cut(line, cut_all=False, HMM=True)
		for word in line:
			if word not in stopwords_list:
				script_after_remove.append(word)
	
	return script_after_remove

# get noun

def get_noun(list_words):

	noun_set = set()
	for word in list_words:
		word = pseg.cut(word)
		for segment in word:
			# print(segment)
			if segment.flag == "n":
				noun_set.add(segment.word)
	return noun_set

# clean noun 

def clean_noun(noun_set, big_stopword):

	clean_list = []
	with open(big_stopword) as big:
		big_list = big.readlines()
	big_list = [z.strip() for z in big_list] 

	list_noun = list(noun_set)
	for word in list_noun:
		if word not in big_list:
			clean_list.append(word)

	return clean_list

if __name__ == "__main__":
	stopwords = "stopwords.txt"
	script = "marcel's_8.txt"
	big_stopword = "big_stopwords.txt"
	clean_script = remove_stopwords(script, stopwords)
	noun_set = get_noun(clean_script)
	print(noun_set)
	clean_list = clean_noun(noun_set, big_stopword)
	print(clean_list)	