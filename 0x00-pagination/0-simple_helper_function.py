#!/usr/bin/env python3
''' task0 '''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' tonight is gonna be the lonileeeessstttt '''
    bidaya = (page - 1) * page_size
    nihaya = page * page_size
    return (bidaya, nihaya)
