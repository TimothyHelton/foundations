#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Sorting Algorithm Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import logging
import random

from strumenti import system


logger = system.logger_setup(name=__name__, master_level=logging.INFO)


class Sorting:
    """Sorting Algorithms

    :param list items: sequence of items to be sorted

    :Attributes:

        - **items**: *list* items to be sorted
        - **item_length**: *int* length of the items list
    """
    def __init__(self, items=None):
        self.items = items
        self._item_length = None

    @property
    def item_length(self):
        try:
            self._item_length = len(self.items)
        except TypeError:
            pass
        return self._item_length

    def __repr__(self):
        return 'Sorting(items={})'.format(self.items)

    def selection_sort(self):
        """Sorts items into ascending order using the selection sort algorithm.

        :returns: items sorted from smallest to largest value
        :rtype: list
        """
        logger.debug('execute: selection_sort')
        if not self.items:
            logger.warning('No items to sort were provided.')
            return None

        for idx in range(self.item_length):
            min_loc = idx
            for loc in range(idx, self.item_length):
                if self.items[loc] < self.items[min_loc]:
                    min_loc = loc
            if min_loc is idx:
                continue
            else:
                old_value = self.items[idx]
                self.items[idx] = self.items[min_loc]
                self.items[min_loc] = old_value
        logger.debug(self.items)


if __name__ == '__main__':
    solution_methods = ('selection_sort',
                        )
    test_items = random.sample(range(100), 100)
    # test_items = [4, 3, 2, 1]
    # test_items = [4, 3, 3, 2]

    sort = Sorting(items=test_items)
    sort.selection_sort()

    from timeit import timeit
    iterations = int(10e1)
    times = {x: timeit('calc = Sorting(items={}); calc.{}()'.format(test_items,
                                                                    x),
                       'from __main__ import Sorting', number=iterations)
             for x in solution_methods}

    for sol in sorted(solution_methods, key=lambda x: times[x]):
        logger.info('{:30}{}'.format(sol + ':', times[sol]))
