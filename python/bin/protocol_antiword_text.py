#!/usr/bin/env python
""" converts word document to text using the protocols.BaseProtocolFile class

This is usefull for update the autoamted tests files if you make a modification to the method

Running without parameters will show a usage message:

$ python bin/protocol_antiword_text.py
"""

import logging
import sys
import os
from knesset_data.protocols.base import BaseProtocolFile

help_text = """
usage: {cmd} <source_doc_file_name> <output_txt_file_name>
* to modify the committee meeting test file:"
* $ {cmd} knesset_data/protocols/tests/20_ptv_317899.doc knesset_data/protocols/tests/20_ptv_317899.txt
"""


def main():
    if len(sys.argv) != 3:
        print help_text.format(cmd=sys.argv[0])
    else:
        source_doc_file_name = sys.argv[1]
        output_txt_file_name = sys.argv[2]
        with BaseProtocolFile.get_from_filename(source_doc_file_name) as protocol:
            output_txt = protocol.antiword_text
            with open(output_txt_file_name, 'wb') as output_file:
                    output_file.write(output_txt)
        print "DONE"

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.WARNING)
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    main()
