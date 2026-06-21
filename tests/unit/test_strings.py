"""Unit tests for string algorithms."""
import pytest
from src.strings.string_algorithms import (
    longest_substring_no_repeat, min_window_substring, is_anagram,
    group_anagrams, longest_palindromic_substring, kmp_search,
    count_palindromic_substrings, longest_common_prefix, check_inclusion,
    reverse_words, encode, decode
)

def test_no_repeat(): assert longest_substring_no_repeat("abcabcbb")==3
def test_no_repeat_all_same(): assert longest_substring_no_repeat("bbbbb")==1

def test_min_window(): assert min_window_substring("ADOBECODEBANC","ABC")=="BANC"
def test_min_window_no(): assert min_window_substring("a","b")==""

def test_anagram(): assert is_anagram("anagram","nagaram")
def test_not_anagram(): assert not is_anagram("rat","car")

def test_group_anagrams(): assert len(group_anagrams(["eat","tea","tan","ate","nat","bat"]))==3

def test_longest_palindrome():
    assert longest_palindromic_substring("babad") in ["bab","aba"]
def test_palindrome_single(): assert longest_palindromic_substring("a")=="a"

def test_kmp(): assert kmp_search("AABAACAADAABAABA","AABA")==[0,9,12]
def test_kmp_not_found(): assert kmp_search("HELLO","XYZ")==[]

def test_palindrome_count(): assert count_palindromic_substrings("aaa")==6
def test_palindrome_count_abc(): assert count_palindromic_substrings("abc")==3

def test_common_prefix(): assert longest_common_prefix(["flower","flow","flight"])=="fl"
def test_no_common_prefix(): assert longest_common_prefix(["dog","racecar"])==""

def test_inclusion(): assert check_inclusion("ab","eidbaooo")
def test_not_inclusion(): assert not check_inclusion("ab","eidboaoo")

def test_reverse_words(): assert reverse_words("the sky is blue")=="blue is sky the"

def test_encode_decode():
    strs=["hello","world","dsa","python"]
    assert decode(encode(strs))==strs
