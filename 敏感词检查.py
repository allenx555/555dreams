import jieba
import os
import sys

uft_str = str.encode("iso-8859-1").decode('gbk').encode('utf8').decode('utf8')  

path = os.path.abspath(os.path.dirname(sys.argv[0]))

jieba.load_userdict(path+'/etc/test/1.txt')

def wordslist(filepath):  
    wordslist = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return wordslist

def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())  
    sensitivewords = wordslist(path+'/test/etc/1.txt')
    outstr = ''
    for word in sentence_seged:
        if word not in sensitivewords:
            outstr += word
        else:
            outstr += "[-1s]"
    return outstr  

inputs=open(path+'/test/输入.txt', 'r', encoding='gbk')
outputs=open(path+'/test/etc/中转1.txt', 'w', encoding='utf-8')

for k in inputs.readlines():
    outputs.write(k.replace('\n','abc'))

outputs.close()
inputs.close()

inputs1=open(path+'/test/etc/中转1.txt', 'r', encoding='utf-8')
outputs1=open(path+'/test/etc/中转2.txt', 'w', encoding='gbk')

for i in inputs1:
    seg_outputs=seg_sentence(i)
    outputs1.write(seg_outputs)

outputs1.close()
inputs1.close()

inputs2=open(path+'/test/etc/中转2.txt', 'r', encoding='gbk')
outputs2=open(path+'/test/输出.txt', 'w', encoding='gbk')

for j in inputs2.readlines():
    outputs2.write(j.replace('abc','\n'))

outputs2.close()
inputs2.close()