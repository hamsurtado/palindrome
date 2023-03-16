from palindrome import check_palindrome


def test_palindrome_check_single_odd():
    assert check_palindrome("baa") == True #aba

def test_palindrome_check_all_even():
    assert check_palindrome("tyygtg") == True #tyggyt

def test_palindrome_check_odd():
    assert check_palindrome("tydtyygtd") == False #tttyyyddg

def test_palindrome_check_empty_string():
    assert check_palindrome("") == True # ""

def test_palindrome_check_case():
    assert check_palindrome("GtYgTyhh") == True #GgTtYyhh

