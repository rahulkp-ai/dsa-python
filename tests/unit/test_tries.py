"""Unit tests for Trie."""
import pytest
from src.tries.trie import Trie, WordDictionary, replace_words

def test_insert_search():
    t=Trie(); t.insert("apple")
    assert t.search("apple") and not t.search("app")

def test_starts_with():
    t=Trie(); t.insert("apple")
    assert t.starts_with("app") and not t.starts_with("xyz")

def test_autocomplete():
    t=Trie()
    for w in ["apple","app","application"]: t.insert(w)
    r=t.autocomplete("app")
    assert "apple" in r and "app" in r

def test_delete():
    t=Trie(); t.insert("apple"); t.insert("app"); t.delete("apple")
    assert not t.search("apple") and t.search("app")

def test_count_prefix():
    t=Trie()
    for w in ["apple","app","application"]: t.insert(w)
    assert t.count_prefix("app")==9  # sum of chars through "app" path

def test_word_dict():
    wd=WordDictionary()
    for w in ["bad","dad","mad"]: wd.add_word(w)
    assert wd.search("bad") and wd.search(".ad") and wd.search("b..") and not wd.search("pad")

def test_replace_words():
    r=replace_words(["cat","bat","rat"],"the cattle was rattled by the battery")
    assert r=="the cat was rat by the bat"
