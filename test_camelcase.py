from unittest import TestCase
import camelcase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', camelcase.camelcase('Hello World'))
        self.assertEqual('', camelcase.camelcase(''))
        self.assertEqual('helloWorld', camelcase.camelcase('Hello      world    '))
        self.assertEqual('helloWorld!', camelcase.camelcase('Hello   World !'))