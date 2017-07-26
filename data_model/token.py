__author__ = 'Danilo S. Carvalho <danilo@jaist.ac.jp>, Vu Duc Tran <vu.tran@jaist.ac.jp>'


class Token(object):
    """Description of a token.

    Attributes:
    surface (unicode): Surface form of the token.
    annotations (dict): [optional] Token level annotations, identified by the dictionary key.
        Examples: word vector, POS tag.
    """

    def __init__(self):
        self.surface = u""
        self.annotations = dict()
