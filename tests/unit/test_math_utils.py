"""Unit tests for math utility functions."""

import pytest

from src.math_algorithms.math_utils import (
    count_digits,
    digit_sum,
    factorial_mod,
    gcd,
    is_perfect_square,
    is_prime,
    lcm,
    nCr_mod,
    nth_fibonacci_matrix,
    power_mod,
    reverse_number,
    sieve_of_eratosthenes,
)


def test_gcd_basic():
    assert gcd(48, 18) == 6


def test_gcd_with_zero():
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0


def test_lcm_basic():
    assert lcm(4, 6) == 12
    assert lcm(-4, 6) == 12
    assert lcm(4, -6) == 12
    assert lcm(-4, -6) == 12


def test_sieve_of_eratosthenes_small():
    assert sieve_of_eratosthenes(1) == []
    assert sieve_of_eratosthenes(2) == [2]
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]


def test_is_prime_values():
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(17)
    assert not is_prime(18)
    assert not is_prime(100)


def test_power_mod():
    assert power_mod(2, 10, 1000) == 24
    assert power_mod(3, 0, 7) == 1
    assert power_mod(10, 1, 6) == 4
    assert power_mod(2, 50, 13) == pow(2, 50, 13)


def test_factorial_mod():
    assert factorial_mod(0, 1000) == 1
    assert factorial_mod(1, 1000) == 1
    assert factorial_mod(10, 1000000007) == 3628800


def test_nCr_mod_values():
    assert nCr_mod(10, 3, 1000000007) == 120
    assert nCr_mod(5, 0, 7) == 1
    assert nCr_mod(5, 6, 7) == 0
    assert nCr_mod(10, 5, 13) == 252 % 13


def test_count_digits():
    assert count_digits(0) == 1
    assert count_digits(7) == 1
    assert count_digits(12345) == 5
    assert count_digits(100000) == 6


def test_digit_sum():
    assert digit_sum(0) == 0
    assert digit_sum(123) == 6
    assert digit_sum(-456) == 15


def test_reverse_number():
    assert reverse_number(123) == 321
    assert reverse_number(-123) == -321
    assert reverse_number(1200) == 21
    assert reverse_number(1534236469) == 0


def test_is_perfect_square():
    assert not is_perfect_square(-1)
    assert is_perfect_square(0)
    assert is_perfect_square(1)
    assert is_perfect_square(16)
    assert not is_perfect_square(18)


def test_nth_fibonacci_matrix():
    assert nth_fibonacci_matrix(0) == 0
    assert nth_fibonacci_matrix(1) == 1
    assert nth_fibonacci_matrix(2) == 1
    assert nth_fibonacci_matrix(10) == 55
    assert nth_fibonacci_matrix(20) == 6765


if __name__ == "__main__":
    pytest.main([__file__])
