#!/usr/bin/env python3
""" Helper function for pagination files """
from typing import Tuple, Union


def index_range(page: int, page_size: int) -> Union[Tuple[int, int], None]:
    """ Function to calculate start and end index of page """
    if page == 0 and page_size:
        end = page_size
        start = 0
        return (start, end)
    if page and page_size:
        end = page * page_size
        start = end - page_size
        return (start, end)
    return None
