#!/usr/bin/env python
# coding: utf-8

from datetime import datetime
import argparse
import io
import json
import os
import re
import shutil
import string
import subprocess
import sys
import time

class PrintProgress():
    def __init__(self, taskName):
        self.taskName = taskName
        self.beginTime = datetime.now()

    def printSpendingTime(self):
        self.endTime = datetime.now()
        print '%s Begins at :%s' % (self.taskName, self.beginTime)
        print '%s Ends at   :%s' % (self.taskName, self.endTime)
        print 'Spend time: %s \n'%(self.endTime - self.beginTime)
        print 'Finish!'

class PreProcesser():

    def __init__(self, parameters):
       self.input_dir = parameters.input;
       self.output_dir = parameters.output;
       self.exclude_files = []
       if not os.path.exists(self.output_dir):
           os.makedirs(self.output_dir)
       with io.open(parameters.macros, 'r') as handle:
           self.macros = handle.read()

       with io.open(parameters.exclude, 'r') as handle:
           self.exclude_files = handle.readlines()
    
    def DoPreProcessing(self):
        printProgress = PrintProgress('DoPreProcessing')
        for root,dirs,files in os.walk(self.input_dir):
            for file in files:
                input_file = root + os.sep + file
                if self.is_excluded(file):
                    continue
                output_file = input_file.replace(self.input_dir, self.output_dir)
                output_file_dir = output_file.rstrip(file)
                if not os.path.exists(output_file_dir):
                    os.makedirs(output_file_dir)
                self.preprocess_file(input_file, output_file)
        printProgress.printSpendingTime()

    def preprocess_file(self, input_file, output_file):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        CPP_SCRIPT = os.path.join(BASE_DIR, "cpp_preprocesser.py")
        try:
            subprocess.check_call([sys.executable, CPP_SCRIPT, "-i=%s" %input_file, "-m=%s" %self.macros, "-o=%s" %output_file])
        except subprocess.CalledProcessError as e:
            print >>sys.stderr,e
            print >>sys.stderr, "Failed to run cpp_preprocesser.py!"

    def is_excluded(self, file):
        for exclude_file in self.exclude_files:
            exclude_file_s = exclude_file.strip().strip('\n')
            if file.count(exclude_file_s) > 0:
                return True
        return False
def main():
    parser = argparse.ArgumentParser(description='Run Preprocessing')
    parser.add_argument(
      '-i', '--input', type=str,
      help='path to the input files dictionary'
    )
  
    parser.add_argument(
      '-m', '--macros', type=str,
      help='macros define file, contents split by comma'
    )

    parser.add_argument(
      '-o', '--output', type=str,
      help='path to the output files dictionary'
    )
    

    parser.add_argument(
      '-e', '--exclude', type=str,
      help='excluded files file'
    )

    parameters = parser.parse_args()
    p = PreProcesser(parameters)
    p.DoPreProcessing()

if __name__ == '__main__':
    main()
