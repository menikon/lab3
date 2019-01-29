import xml.etree.ElementTree as ET
from xml.etree.ElementTree import *
import MeCab
import re

# xmlファイルの読み込み
tree = ET.parse('Center-1993--Main-Nihonshi.xml')
elem = tree.getroot()

#print("".join(elem.itertext()))
question = elem.findall('question/question/instruction')
choice = elem.findall('question/question/choices/choice')
result1 = ""
for item1 in question:
    result1 += "".join(item1.itertext())
#print(result1)

f = open('question.txt','w')

f.write(result1)

f.close()

result2 = ""
for item2 in choice:
    result2 += "".join(item2.itertext())
#print(result2)

#pattern = ".*①.*"
#matchOB = re.match(pattern , result2)
#print (matchOB)
f = open('choice.txt','w')

f.write(result2)

f.close()

#mecabでテキストファイル内の文章を形態素解析
m = MeCab.Tagger("")
m.parse('')
#ここでテキストファイルを選択
doc = input('select file(ex,●●.txt):')
f = open(doc,'r')
text = f.read()
f.close()
mecab_parse = m.parse(text)
target = mecab_parse.split('\t')
#mecab_parse = m.parseToNode(text)
keywords = []
for word in target:
    temp = word.split('\t')
    #temp2 = temp[0].split(',')
    temp2 = temp[0].replace("*\n", "")
    temp3 = temp2.split(',')

    #print(temp2)
    if temp3[0] == '名詞':
        keywords.append(temp3[6])
    elif temp3[0] == '形容詞':
        keywords.append(temp3[6])
    elif temp3[0] == '動詞':
        keywords.append(temp3[6])

    #print(temp)
#print(keywords)

#形態素解析の結果をテキストファイルに書き込む
word = ""
for i in keywords:
#    print(i, end = " ")
    word = word + i + " "
f=open("MeCab_" + doc,'w')
f.write(word)
f.close()
