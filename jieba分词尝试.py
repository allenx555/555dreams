import jieba
import os
import sys

path = os.path.abspath(os.path.dirname(sys.argv[0]))
jieba.load_userdict(path+'/test/1.txt')

def wordslist(filepath):  
    wordslist = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return wordslist

def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())  
    outstr = ''
    for word in sentence_seged:
            outstr = outstr + word + " "
    return outstr  

inputs=open(path+'/test/inputs.txt', 'r', encoding='utf-8')
outputs=open(path+'/test/outputs.txt', 'w', encoding='utf-8')


for i in inputs:
    seg_outputs=seg_sentence(i)
    outputs.write(seg_outputs)

outputs.close()
inputs.close()