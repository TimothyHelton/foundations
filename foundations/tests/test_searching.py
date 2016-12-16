#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit Tests for Searching Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import pytest
from strumenti.tests.fixtures import ChromalogLogCapture

from foundations import search


# Test Searching class
# Test Searching.__repr__()
def test_searching__repr__():
    assert search.Searching().__repr__() == 'Searching(items=None)'
