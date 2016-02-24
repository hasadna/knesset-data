# -*- coding: utf-8 -*-
import logging
import subprocess
import os
import xml.etree.ElementTree as ET


logger = logging.getLogger(__name__)


def antixml(str):
    tree = ET.fromstring(str.replace("\n\n", ""))
    text = ET.tostring(tree, encoding='utf8', method='text')
    text = "\n".join([line.strip() if len(line.strip()) == 0 else line for line in text.split("\n")])
    return text


def antiword(filename):
    cmd='antiword -x db '+filename+' > '+filename+'.awdb.xml'
    try:
        logger.debug(cmd)
        output = subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
    except subprocess.CalledProcessError, e:
        # this error can be very annoying to debug
        # so hopefully, even if someone forgot to setup logging we want to make sure they know what the problem is
        print "\n"
        print "encountered an error running antiword"
        print "\n"
        print "check if you have antiword installed (sudo apt-get install antiword)"
        print "\n"
        print "cmd:", e.cmd
        print "returncode:", e.returncode
        print "output:", e.output
        raise e
    logger.info(output)
    with open(filename+'.awdb.xml','r') as f:
        xmldata=f.read()
    logger.debug('len(xmldata) = '+str(len(xmldata)))
    os.remove(filename+'.awdb.xml')
    return xmldata
