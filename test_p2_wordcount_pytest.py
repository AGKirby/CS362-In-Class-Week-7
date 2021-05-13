import pytest
import p2_wordcount

def test_wordcount1():
    result = p2_wordcount.wordcount("Greetings!   ")
    assert result == 1

def test_wordcount2():
    result = p2_wordcount.wordcount("1,336,472")
    assert result == 1

def test_wordcount3():
    result = p2_wordcount.wordcount("!!H!! is a word")
    assert result == 4