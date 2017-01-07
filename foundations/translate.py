#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Module for Translating the English Language

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import string


class PigLatin:
    """Methods for translating English into other Pig Latin.

    :param str phrase: phrase in English to be translated

    :Attributes:

        - **original_phrase**: *str* initial phrase in English to be translated
        - **phrase**: *list* list of phrase to be translated with whitespace \
            removed
        - **pig_latin**: *str* phrase translated into Pig Latin
    """

    def __init__(self, phrase):
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.consonants = [x for x in string.ascii_lowercase
                           if x not in self.vowels]
        self.original_phrase = phrase
        self.phrase = phrase.split()
        self._pig_latin = None

    @property
    def pig_latin(self):
        self.translate()
        return ' '.join(self._pig_latin)

    def __repr__(self):
        return "PigLatin(phrase='{}')".format(self.original_phrase)

    def translate(self):
        """Translate phrase into pig latin."""

        def trans_consonant(wrd, capitalize):
            """Translate word that begins with a consonant.

            :param str wrd: word to be translated
            :param bool capitalize: if True the word will be capitalized
            :returns: word beginning with consonant translated into pig latin
            :rtype: str
            """
            idx = 0
            for (idx, letter) in enumerate(wrd):
                if letter in self.vowels:
                    break
            leading_consts = wrd[:idx]
            new_beginning = wrd[idx:]
            trans = '{}{}ay'.format(new_beginning, leading_consts)
            if capitalize:
                return trans.capitalize()
            return trans

        def trans_vowel(wrd, capitalize):
            """Translate word that begins with a vowel.

            :param str wrd: word to be translated
            :param bool capitalize: if True the word will be capitalized
            :returns: word beginning with vowel translated into pig latin
            :rtype: str
            """
            trans = '{}way'.format(wrd)
            if capitalize:
                return trans.capitalize()
            return trans

        self._pig_latin = []
        for word in self.phrase:
            first_letter = word[0]
            cap = False
            if first_letter.isupper():
                cap = True

            lower_first = first_letter.lower()
            lower_word = word.lower()
            if lower_first in self.consonants:
                self._pig_latin.append(trans_consonant(wrd=lower_word,
                                                       capitalize=cap))
            elif lower_first in self.vowels:
                self._pig_latin.append((trans_vowel(wrd=lower_word,
                                                    capitalize=cap)))
