#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit Tests for Sorting Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import pytest
from strumenti.tests.fixtures import ChromalogLogCapture

from foundations import sort


empty = []
empty_expected = output = ((),
                           )
repeating = [9, 9, 8, 8, 0, 0]
repeating_expected = [0, 0, 8, 8, 9, 9]
negative = [-1, -2, -3, -4]
negative_expected = [-4, -3, -2, -1]


# Test Sorting.__repr__()
def test_sorting__repr__():
    assert sort.Sorting().__repr__() == 'Sorting(items=None)'


# Test Sorting.selection_sort()
selection = {'repeating': (repeating, repeating_expected),
             'negative': (negative, negative_expected),
             }


@pytest.mark.parametrize('items, expected',
                         list(selection.values()),
                         ids=list(selection.keys()))
def test_selection_sort(items, expected):
    inst = sort.Sorting(items=items)
    inst.selection_sort()
    assert inst.items == expected


def test_selection_sort_empty():
    inst = sort.Sorting(items=empty)
    with ChromalogLogCapture() as log_cap:
        inst.selection_sort()
    log_cap.filter_records()
    log_cap.check(
        ('foundations.sort', 'WARNING', 'No items to sort were provided.'),
    )
