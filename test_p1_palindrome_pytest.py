import pytest
import p1_palindrome

def test_palindrome1():
    result = p1_palindrome.palindrome("HanNah")
    assert result == True

def test_palindrome2():
    result = p1_palindrome.palindrome("A")
    assert result == True

def test_palindrome3():
    result = p1_palindrome.palindrome(" ! ")
    assert result == True