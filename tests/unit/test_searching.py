"""Unit tests for binary search."""
import pytest
from src.searching.binary_search import (
    binary_search, search_range, search_rotated, find_peak,
    isqrt, search_matrix, min_eating_speed, ship_days, search_insert, find_min_rotated
)

def test_bs_found(): assert binary_search([-1,0,3,5,9,12],9)==4
def test_bs_not_found(): assert binary_search([-1,0,3,5,9,12],2)==-1
def test_bs_empty(): assert binary_search([],5)==-1

def test_range(): assert search_range([5,7,7,8,8,10],8)==[3,4]
def test_range_none(): assert search_range([5,7,7,8,8,10],6)==[-1,-1]

def test_rotated(): assert search_rotated([4,5,6,7,0,1,2],0)==4
def test_rotated_none(): assert search_rotated([4,5,6,7,0,1,2],3)==-1

def test_peak(): assert [1,2,3,1][find_peak([1,2,3,1])]==3

def test_sqrt(): assert isqrt(4)==2 and isqrt(8)==2 and isqrt(9)==3

def test_matrix(): assert search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)
def test_matrix_none(): assert not search_matrix([[1,3,5,7],[10,11,16,20]],13)

def test_koko(): assert min_eating_speed([3,6,7,11],8)==4
def test_ship(): assert ship_days(list(range(1,11)),5)==15

def test_insert(): assert search_insert([1,3,5,6],2)==1
def test_find_min(): assert find_min_rotated([3,4,5,1,2])==1
