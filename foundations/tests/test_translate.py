#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit Tests for Pig Latin Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import pytest


from foundations import translate


# Test Translation.__repr__()
def test__repr__():
    inst = translate.PigLatin(phrase='test phrase')
    assert inst.__repr__() == "PigLatin(phrase='test phrase')"


# Test PigLatin.translate()
trans_pig_latin = {'leading_consonant': ('pig', 'igpay'),
                   'leading_cluster': ('glove', 'oveglay'),
                   'leading_vowel': ('omelet', 'omeletway'),
                   'multi-word': ('happy eat', 'appyhay eatway'),
                   'capital': ('Duck Are', 'Uckday Areway'),
                   'punctuation': ('happy. eat!', 'appyhay. eatway!'),
                   }


@pytest.mark.parametrize('input_phrase, expected',
                         list(trans_pig_latin.values()),
                         ids=list(trans_pig_latin.keys()))
def test__pig_latin(input_phrase, expected):
    inst = translate.PigLatin(phrase=input_phrase)
    assert inst.pig_latin == expected
