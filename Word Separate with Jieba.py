# 导入扩展库
import re # 正则表达式库
import collections # 词频统计库
import jieba # 结巴分词


# 读取文件
fn = open("/Users/eric/Documents/Research/人大社科院（王鹏）/LDA主题处理/txt/1996年中央经济工作会议.txt") # 打开文件
string_data = fn.read() # 读出整个文件
fn.close() # 关闭文件

# 文本预处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|') # 定义正则表达式匹配模式
string_data = re.sub(pattern, '', string_data) # 将符合模式的字符去除

# 文本分词
seg_list_exact = jieba.cut(string_data)

stopwords = {}.fromkeys([ line.rstrip() for line in open('/Users/eric/Documents/Research/人大社科院（王鹏）/LDA主题处理/stopword.txt') ])   #fromkeys为创建一个新字典，键及键值 rstrip() 删除 string 字符串末尾的指定字符
#print(stopwords)
object_list = []
for word in seg_list_exact :
    if word not in stopwords:
        if (word != "。" and word != "，" and word !=" ") :
            object_list.append(word)

# 词频统计
word_counts = collections.Counter(object_list) # 对分词做词频统计
word_counts_top10 = word_counts.most_common(50) # 获取前10最高频的词
# print (word_counts_top10) # 输出检查
for word in word_counts_top10:
    print(word[0])
