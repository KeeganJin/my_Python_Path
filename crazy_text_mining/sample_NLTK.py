from nltk import FreqDist


def tm_func():
    f = open("./corpora/abc/science.txt",'rb')
    text1 = f.read()
    print(len(text1))

#     frequency distribution of words
    freq_dist = FreqDist(text1)
    print(len(freq_dist))
    print(freq_dist)
#     distribution of a word
    print(freq_dist['The'])

if __name__ == '__main__':
    tm_func()