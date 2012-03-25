# -*- coding: utf-8 -*-

import os
import re
import sys
import zipfile
from os.path import join
from optparse import OptionParser,make_option

if __name__=='__main__':
    if len(sys.argv)!=4 :
        print("Usage: %s input_directory_path condition_string output_directory_path"%sys.argv[0]);
        exit(-1);
    
    #extract input arguments
    inputDir=sys.argv[1];
    conditionString=sys.argv[2];
    outputDir=sys.argv[3];

    #convert condition string to be regular expression
    reString=conditionString.replace('\\', '\\\\').replace('.', '\\.').replace('*', '.+');
    print("regular expression: %s"%reString);
    prog=re.compile(reString);

    #list all *.zip
    for root,dirs,files in os.walk(inputDir):
        for f in files:
            if f.endswith(".zip") :
                zipFile=os.path.join(root, f)
                #print("find zip file: %s"%zipFile)
                sourceZip=zipfile.ZipFile(zipFile, 'r')
                for name in sourceZip.namelist():
                    if prog.match(name):
                        print("find target file: %s"%name);
                        sourceZip.extract(name, outputDir);
                sourceZip.close();
            if f.endswith(".rar") :
                rarFile=os.path.join(root, f)
                print("find rar file: %s"%rarFile)

    print("DONE, output directory: %s"%outputDir);
