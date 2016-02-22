# -*- coding: utf-8 -*-
import logging
import subprocess
import os
import re


logger = logging.getLogger(__name__)


def antixml(str):
    return re.sub('[\n ]{2,}', '\n\n', re.sub('<.*?>','',str))


def antiword(filename):
    cmd='antiword -x db '+filename+' > '+filename+'.awdb.xml'
    logger.debug(cmd)
    output = subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
    logger.debug(output)
    with open(filename+'.awdb.xml','r') as f:
        xmldata=f.read()
    logger.debug('len(xmldata) = '+str(len(xmldata)))
    os.remove(filename+'.awdb.xml')
    return xmldata
