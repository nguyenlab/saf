__author__ = 'danilo@jaist.ac.jp'

from constants import annotation

class CoNLLFormatter(object):
    def __init__(self, field_list):
        self.field_list = field_list

    # def dumps(self, document):
    #     output = []
    #     for sentence in document.sentences:
    #         for token in sentence.tokens:
    #             output.append([token.surface] + [token.annotations[field] if (field in token.annotations) else u"-" for field in self.field_list])
    #         output.append([])
    #
    #     return u"\n".join((u"\t".join(line) for line in output))

    # def dump(self, document, file):
    #     for sentence in document.sentences:
    #         for token in sentence.tokens:
    #             file.write(u"\t".join([token.surface] + [token.annotations[field] if (field in token.annotations) else u"-" for field in self.field_list]))
    #             file.write(u"\n")
    #
    #         file.write(u"\n")


    def dumps(self, document):
        if(len(document.sentences) == 0):
            return "";

        has_term = len(document.sentences[0].terms) > 0

        has_id = annotation.ID in document.sentences[0].tokens[0].annotations

        if(has_term and has_id):
            return self.dumps_w_term_w_id(document)
        elif(has_term and not has_id):
            return self.dumps_w_term_wo_id(document)
        elif(not has_term and has_id):
            return self.dumps_wo_term_w_id(document)
        elif(not has_term and not has_id):
            return self.dumps_wo_term_wo_id(document)
        else:
            raise


    def dumps_w_term_w_id(self, document):
        output = []
        for sentence in document.sentences:
            for term in sentence.terms:
                if(len(term.tokens) > 1):
                    output.append(
                        [term.annotations[annotation.ID], term.surface]
                        + [term.annotations[field] if (field in term.annotations) else u"-" for field in self.field_list])

                for token in term.tokens:
                    output.append([token.annotations[annotation.ID], token.surface]
                                  + [token.annotations[field] if (field in token.annotations) else u"-" for field in self.field_list])

            output.append([])

        return u"\n".join((u"\t".join(line) for line in output))

    def dumps_w_term_wo_id(self, document):
        output = []

        for sentence in document.sentences:
            last_token_id = 0
            for term in sentence.terms:
                if(len(term.tokens) > 1):
                    output.append(
                        [u"%d-%d" % (last_token_id+1, last_token_id+len(term.tokens)), term.surface]
                        + [term.annotations[field] if (field in term.annotations) else u"-" for field in self.field_list])

                for token in term.tokens:

                        output.append([unicode(last_token_id + 1), token.surface]
                                      + [token.annotations[field] if (field in token.annotations) else u"-" for field in self.field_list])
                        last_token_id += 1

            output.append([])

        return u"\n".join((u"\t".join(line) for line in output))

    def dumps_wo_term_w_id(self, document):
        output = []
        for sentence in document.sentences:
            for token in sentence.tokens:
                output.append([token.annotations[annotation.ID], token.surface] + [token.annotations[field] if (field in token.annotations) else u"-" for field in self.field_list])

            output.append([])

        return u"\n".join((u"\t".join(line) for line in output))

    def dumps_wo_term_wo_id(self, document):
        output = []

        for sentence in document.sentences:
            last_token_id = 0
            for token in sentence.tokens:
                output.append([unicode(last_token_id+1),token.surface] + [token.annotations[field] if (field in token.annotations) else u"-" for field in self.field_list])
                last_token_id += 1
            output.append([])

        return u"\n".join((u"\t".join(line) for line in output))

