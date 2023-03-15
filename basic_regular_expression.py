# https://wikidocs.net/21703


import re


r = re.compile("a.c")
# print(r.search("avc"))

r = re.compile("ab?c")
# print(r.search("ac"))

r = re.compile("ab*c")
# print(r.search("ac"))
# print(r.search("adc"))
# print(r.search("abbbbc"))

r = re.compile("ab+c")
# print(r.search("abc"))

r = re.compile("^ab")
# print(r.search("abc"))
# print(r.search("bcab"))

r = re.compile("ab{3}c")
# print(r.search("abbbc"))

r = re.compile("ab{2,5}c")
# print(r.search("abbbbbc"))

r = re.compile("a{3,}bc")
# print(r.search("aaaaabc"))ㄴ

r = re.compile("[abc]")
# print(r.search("zzzzbbb"))

r = re.compile("[a-z]")
# print(r.search("AAAAAAAAAAa"))

r = re.compile("[^def]")
# print(r.search("d"))


text = "감자 고구마 오이 양파 마늘"
# print(re.split(" ", text))

text = """감자
고구마
오이
양파
마늘"""
# print(re.split("\n", text))


text = """이름 : 김철수
전화번호 : 010 - 1234 - 5678
나이 : 30
성별 : 남"""
# print(re.findall("\d+", text))


text = "Regular expression : A regular expression, regex or regexp[1] (sometimes called a rational expression)[2][3] is, in theoretical computer science and formal language theory, a sequence of characters that define a search pattern."
preprocessed_text = re.sub('[^a-zA-Z]', ' ', text)
# print(preprocessed_text)


text = """100 John  PROF
101 James   STUD
102 Mac  STUD"""
# print(re.split('\s+', text))
# print(re.findall('\d+', text))
# print(re.findall('[A-Z]', text))
# print(re.findall('[A-Z]{4}', text))
# print(re.findall('[A-Z][a-z]+', text))


""" RegexpTokenizer """
from nltk.tokenize import RegexpTokenizer


tokenizer1 = RegexpTokenizer("[\w]+") # 문자 또는 숫자가 1개 이상
tokenizer2 = RegexpTokenizer("\s+", gaps=True) # 공백을 기준으로 토큰화

text = "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop"
print(tokenizer1.tokenize(text))
print(tokenizer2.tokenize(text))
