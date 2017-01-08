#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit Tests for Pig Latin Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import pytest


from foundations import translate


# Test Translation.__repr__()
def test__translation__repr__():
    inst = translate.PigLatin(phrase='test phrase')
    assert inst.__repr__() == "PigLatin(phrase='test phrase')"


# Test PigLatin.translate()
pig_latin = {'leading_consonant': ('pig', 'igpay'),
             'leading_cluster': ('glove', 'oveglay'),
             'leading_vowel': ('omelet', 'omeletway'),
             'multi-word': ('happy eat', 'appyhay eatway'),
             'capital': ('Duck Are', 'Uckday Areway'),
             'punctuation': ('happy. eat!', 'appyhay. eatway!'),
             }


@pytest.mark.parametrize('input_phrase, expected',
                         list(pig_latin.values()),
                         ids=list(pig_latin.keys()))
def test__pig_latin(input_phrase, expected):
    inst = translate.PigLatin(phrase=input_phrase)
    assert inst.pig_latin == expected


# Test ReversePolish.__repr__()
def test__reversepolish__repr__():
    inst = translate.ReversePolish(expression='1 2 +')
    assert inst.__repr__() == "ReversePolish(expression='1 2 +'"


# Test ReversePolish.evaluate()
reverse_polish = {'addition': ('1 2 +', 3),
                  'subtraction': ('2 1 -', 1),
                  'multiplication': ('4 5 *', 20),
                  'division': ('100 10 /', 10),
                  'exponential': ('10 2 **', 100),
                  'two_expressions': ('5 1 2 + 4 * + 3 -', 14),
                  }


@pytest.mark.parametrize('expression, expected',
                         list(reverse_polish.values()),
                         ids=list(reverse_polish.keys()))
def test__reversepolish_evaluate(expression, expected):
    inst = translate.ReversePolish(expression=expression)
    assert inst.evaluate() == expected
