#!/usr/bin/python
# coding: utf-8

import unittest
import ConfigParser

class ConfigFileTest(unittest.TestCase):

    config_filename = 'treidis.conf'

    def setUp(self):
        self.options = ConfigParser.ConfigParser()
        self.options.read(self.config_filename)

    def testHasAuthKey(self):
        if not self.options.has_option('AUTH','key'):
            raise Exception('ConfigFileTest testHasAuthKey: [AUTH] option "key" not found.')
        key = self.options.get('AUTH','key')
        self.assertTrue(isinstance(key,int))

    def testHasSecretKey(self):
        if not self.options.has_option('AUTH','secret'):
            raise Exception('ConfigFileTest testHasSecretKey: [AUTH] option "secret" not found.')

    #if not options.has_option('AUTH','key'):
    #    raise Exception('APIRequests __init__: [AUTH] option "key" not found.')

class FoxBitOrderbookModelTest(unittest.TestCase):
    pass
    #def testFailUnless(self):
    #    self.failUnless(True)

    #def testAssertTrue(self):
    #    self.assertTrue(True)

    #def testFailIf(self):
    #    self.failIf(False)

    #def testAssertFalse(self):
    #    self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()
