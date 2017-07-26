__author__ = 'Danilo S. Carvalho <danilo@jaist.ac.jp>, Vu Duc Tran <vu.tran@jaist.ac.jp>'

from itertools import izip
from data_model.document import Document
from data_model.sentence import Sentence
from data_model.token import Token
from data_model.term import Term
from importer import Importer
from importers.tokenizers.conll import conll_sentence_tokenize, conll_word_tokenize
from constants import annotation

class CoNLLImporter(Importer):
    def __init__(self, field_list):
        """Formatter constructor

        Constructs a formatter object that tokenizes a plain text document into sentences using
        sentence_tokenizer and words in a sentence using word_tokenizer.

        :param field_list (list of str): list of keys identifying the fields in the CoNLL file.
            Default keys can be found in the constants.annotation module.
            Example: ["POS", "DEP", ...]
        :return: new Formatter instance.
        """

        self.sent_tokenizer = conll_sentence_tokenize
        self.word_tokenizer = conll_word_tokenize
        self.field_list = field_list

    def import_document(self, document):

        doc = Document()

        sentences_raw = self.sent_tokenizer(document)

        for sent_raw in sentences_raw:
            tokens_raw = self.word_tokenizer(sent_raw)

            sentence = Sentence()
            last_term_id = (-1,)

            for token_raw in tokens_raw:
                if(token_raw.startswith(u"#")):
                    continue

                fields = token_raw.split()
                id_raw = fields[0]
                id_raw_range = map(float, id_raw.split('-'))
                annotations = dict(izip(self.field_list, fields[2:]))

                if(len(id_raw_range) == 1):

                    token = Token()
                    token.surface = fields[1]
                    token.annotations = annotations
                    token.annotations[annotation.ID] = id_raw
                    sentence.tokens.append(token)

                    token_id = float(token.annotations[annotation.ID])

                    if(token_id <= last_term_id[-1]):
                        last_term.tokens.append(token)
                    else:
                        term = Term()
                        term.surface = fields[1]
                        term.annotations = annotations
                        term.annotations[annotation.ID] = id_raw
                        sentence.terms.append(term)
                        last_term = term

                        last_term_id = id_raw_range

                        term.tokens.append(token)

                elif(len(id_raw_range) == 2):
                    term = Term()
                    term.surface = fields[1]
                    term.annotations = annotations
                    term.annotations[annotation.ID] = id_raw
                    sentence.terms.append(term)
                    last_term = term

                    last_term_id = id_raw_range

                else:
                    raise ValueError("FUUUU")





            if(len(sentence.tokens) == 0):
                continue

            doc.sentences.append(sentence)

        return doc
