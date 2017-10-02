#!/usr/bin/env python

import os, subprocess
from unittest import TestCase
from boutiques import __file__ as bfile
from boutiques.bosh import bosh

class TestExample1(TestCase):

    def get_examples_dir(self):
        return os.path.join(os.path.dirname(__file__),
                            "..","schema","examples")
                
    def test_example1_no_exec(self):
        example1_dir = os.path.join(self.get_examples_dir(),"example1")       
        self.assertFalse(bosh(["exec", '-i',
                                    os.path.join(example1_dir,"invocation.json"),
                                    os.path.join(example1_dir,"example1.json")]))

    def test_example1_exec(self):
        example1_dir = os.path.join(self.get_examples_dir(),"example1")       
        self.assertFalse(bosh(['exec', '-i',
                                    os.path.join(example1_dir,"invocation.json"),
                                    os.path.join(example1_dir,"example1.json"),
                                    '-e']))
        self.assertFalse(bosh(['exec', '-i',
                                    os.path.join(example1_dir,"invocation.json"),
                                    os.path.join(example1_dir,"example1.json"),
                                    '-e', '-k']))


    def test_example1_no_exec_random(self):
        example1_dir = os.path.join(self.get_examples_dir(),"example1")       
        self.assertFalse(bosh(['exec', os.path.join(example1_dir,"example1.json"),
                                    '-r', '-n' '3']))
