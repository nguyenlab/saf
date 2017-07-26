__author__ = 'danilo@jaist.ac.jp'


def conll_sentence_tokenize(conll_document):
    return [sent_raw.strip() for sent_raw in conll_document.split("\n\n")]


def conll_word_tokenize(conll_sentence):
    return conll_sentence.split("\n")