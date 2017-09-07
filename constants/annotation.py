__author__ = 'Danilo S. Carvalho <danilo@jaist.ac.jp>, Vu Duc Tran <vu.tran@jaist.ac.jp>'


"""Annotation key constants

This module provides annotation key constants for use with the "annotations" dict
in each level of the data model: document, sentence, term and token.

Declared keys are:
    ID       Identifier
    POS      Part of Speech tag.
    DEP      Dependency tag.
    UPOS     Universal POS tag. See [http://universaldependencies.org/u/pos/index.html]
    UDEP     Universal dependency tag. See [http://universaldependencies.org/u/dep/index.html]
    DEPREL   ID of dependency relation head.
    CHUNK    Chunking tag.
    CSTRUCT  Syntactic constituency tag.
    TOPIC    Topic model tag.
    INCL     Inclusion tag. For extractive summarization.
    MORPHO   Morphological decomposition.
    VEC      Vector representation.
    W2V      word2vec embedding. See [https://code.google.com/archive/p/word2vec/]
    GLOVE    Global Vectors embedding. See [https://nlp.stanford.edu/projects/glove/]
    TDV      Term Definition Vector representation. See [https://github.com/dscarvalho/tdv]

"""

# public symbols
__all__ = ["ID", "LEMMA", "POS", "DEP", "UPOS", "UDEP", "DEPREL", "CHUNK", "CSTRUCT", "TOPIC", "INCL", "MORPHO", "VEC", "W2V", "GLOVE", "TDV"]

# constants
ID = "ID"
LEMMA = "LEMMA"
POS = "POS"
DEP = "DEP"
UPOS = "UPOS"
UDEP = "UDEP"
DEPREL = "DEPREL"
CHUNK = "CHUNK"
CSTRUCT = "CSTRUCT"
TOPIC = "TOPIC"
INCL = "INCL"
MORPHO = "MORPHO"
VEC = "VEC"
W2V = "W2V"
GLOVE = "GLOVE"
TDV = "TDV"