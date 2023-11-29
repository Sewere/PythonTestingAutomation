#All programming languages support unit testing, and most languages contain a built-in unit testing framework.
#Python is no exception with its "unittest" module:

#https://docs.python.org/3/library/unittest.html

#Use the below Python code and improve it by writing unit tests to it by using the "unittest" feature.

#Code to write the tests for:

#---------------------------------
import Mathematical

class TestMathMethods():

    def test_addition(self):
        plussa = Mathematical.add(5, 4)
        miinus = Mathematical.add(-6, 3)
        assert plussa == 9
        assert miinus == -3

    def test_multiply(self):
        multi = Mathematical.multiply(3, 4)
        nolla = Mathematical.multiply(0, 9)
        assert multi == 12
        assert nolla == 0        

    def test_split(self):
        exponentti = Mathematical.power(2, 8)
        assert exponentti == 256
        