import pytest

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphorddde'

#def test_raises_exception_on_non_string_arguments():
#    with pytest.raises(TypeError):
#        capital_case('david')