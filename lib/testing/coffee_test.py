#!/usr/bin/env python3

from lib.coffee import Coffee

import io
import sys

class TestCoffee:
    '''Coffee in coffee.py'''

    def test_has_size_and_price(self):
        '''has the size and status passed to __init__, and values can be set to new instance.'''
        black = Coffee(size = "Large", price = 1.50)
        assert(black.size == "Large")
        assert(black.price == 1.50)

    def test_requires_specific_size(self):
        '''prints "size must be Small, Medium, or Large" if size is not an one of those options.'''
        latte = Coffee(size = "Large", price = 2.50)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        latte.size = "not an size"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "size must be Small, Medium, or Large\n"

    def test_can_tip(self):
        '''says that the shoe has been repaired.'''
        americano = Coffee(size = "Large", price = 3.50)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        americano.tip()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "This coffee is great, here’s a tip!\n")
    
    def test_tip_adds_to_price(self):
        '''adds 1 to price of coffee'''
        americano = Coffee(size = "Large", price = 3.50)
        americano.tip()
        assert(americano.price == 4.50)
        
        
