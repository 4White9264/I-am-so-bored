# 导入扩展库
import re # 正则表达式库
import collections # 词频统计库
import jieba # 结巴分词


# 读取文件
fn = open("word.txt") # 打开文件
string_data = fn.read() # 读出整个文件
fn.close() # 关闭文件

# 文本预处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|') # 定义正则表达式匹配模式
string_data = re.sub(pattern, '', string_data) # 将符合模式的字符去除

# 文本分词
seg_list_exact = jieba.cut(string_data) # 这个地方也可以用别的jieba cut方式
#seg_list_exact = jieba.cut(string_data, cut_all=True)
#seg_list_exact = jieba.cut_for_search(string_data) # 这个方法更全面


#jieba.add_word(word, freq=None, tag=None) # 动态修改词频

#jieba.suggest_freq(non_separated_word, tune=True) # 添加不会被分开的词

stopwords = {}.fromkeys([ line.rstrip() for line in open('stopword.txt') ])
# 这里会有一个停止词的txt，里面都是不会被显示的词

object_list = []
for word in seg_list_exact :
    if word not in stopwords:
        if (word != "。" and word != "，" and word !=" ") :
            object_list.append(word)

# 词频统计
word_counts = collections.Counter(object_list) # 对分词做词频统计
word_counts_top10 = word_counts.most_common(10) # 获取前10最高频的词
# print (word_counts_top10) # 输出检查
for word in word_counts_top10:
    print(word[0])
