#!/usr/bin/env python

# Nathan Wood
# 2014-05-03
# https://github.com/woodnathan/objc_strings/

"""
Unit testing for objc_strings
"""

import unittest
from objc_strings import *

class KeyInCodeLineTests(unittest.TestCase):
    
    def testNone(self):
        self.assertEquals(None, key_in_code_line('#import <UIKit/UIKit.h>'))
    
    def testKeyNoTable(self):
        self.assertEquals([("key", None)], key_in_code_line('NSLocalizedString(@"key", @"comment")'))
    
    def testKeyWithTable(self):
        self.assertEquals([("key", "table")], key_in_code_line('NSLocalizedStringFromTable(@"key", @"table", @"comment")'))
        self.assertEquals([("key", "table")], key_in_code_line('NSLocalizedStringFromTableInBundle(@"key", @"table", [NSBundle mainBundle], @"comment")'))
        self.assertEquals([("key", "table")], key_in_code_line('NSLocalizedStringWithDefaultValue(@"key", @"table", [NSBundle mainBundle], @"default value", @"comment")'))
        
    def testKeyWithComments(self):
        self.assertEquals(None, key_in_code_line('// NSLocalizedString(@"key", @"comment")'))
        self.assertEquals(None, key_in_code_line('// NSLocalizedStringFromTable(@"key", @"table", @"comment")'))
        self.assertEquals(None, key_in_code_line('// NSLocalizedStringFromTableInBundle(@"key", @"table", [NSBundle mainBundle], @"comment")'))
        self.assertEquals(None, key_in_code_line('// NSLocalizedStringWithDefaultValue(@"key", @"table", [NSBundle mainBundle], @"default value", @"comment")'))
        
    # def testKeyWithTableOnNewline(self):
    #     self.assertEquals([("key", "table")], key_in_code_line('NSLocalizedStringFromTable(@"key",\n@"table",\n@"comment")'))
    #     self.assertEquals([("key", "table")], key_in_code_line('NSLocalizedStringFromTableInBundle(@"key",\n@"table",\n[NSBundle mainBundle],\n@"comment")'))
    #     self.assertEquals([("key", "table")], key_in_code_line('NSLocalizedStringWithDefaultValue(@"key",\n@"table",\n[NSBundle mainBundle],\n@"default value",\n@"comment")'))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
