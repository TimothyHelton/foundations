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

    def bubble_sort(self):
        pass

    def merge_sort(self):
        """Sorts items into ascending order using the merge sort algorithm."""
        def split_list(base_list):
            """Split original list into two lists."""
            if len(base_list) < 2:
                return base_list

            middle = len(base_list) // 2
            front = split_list(base_list[:middle])
            back = split_list(base_list[middle:])

            return sort_list(front, back)

        def sort_list(first, last):
            if not first:
                return last
            if not last:
                return first

            if first[0] < last[0]:
                return [first[0]] + sort_list(first[1:], last)
            return [last[0]] + sort_list(first, last[1:])

        logger.debug('execute: merge_sort')
        self.items = split_list(self.items)
        logger.debug(self.items)

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
    solution_methods = ('merge_sort',
                        'selection_sort',
                        )

    test_items = random.sample(range(1000), 100)
    # test_items = [4, 3, 2, 1]
    # test_items = [4, 3, 3, 2]

    # sort = Sorting(items=test_items)
    # sort.selection_sort()
    # sort.merge_sort()

    from timeit import timeit
    iterations = int(10e1)
    times = {x: timeit('calc = Sorting(items={}); calc.{}()'.format(test_items,
                                                                    x),
                       'from __main__ import Sorting', number=iterations)
             for x in solution_methods}

    for sol in sorted(solution_methods, key=lambda x: times[x]):
        logger.info('{:30}{}'.format(sol + ':', times[sol]))
