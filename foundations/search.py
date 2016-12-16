#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Searching Algorithm Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import logging
import random

from strumenti import system


logger = system.logger_setup(name=__name__, master_level=logging.INFO)


class Searching:
    """Searching Algorithms

    :param list items: sequence of items to be searched

    :Attributes:

        - **items**: *list* items to be searched
    """
    def __init__(self, items=None):
        self.items = items

    def __repr__(self):
        return 'Searching(items={})'.format(self.items)

    def binary_search(self):
        pass

    def linear_search(self):
        pass


if __name__ == '__main__':
    pass
