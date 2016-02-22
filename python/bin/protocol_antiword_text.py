#!/usr/bin/env python
import logging
import sys
import os
from knesset_data.protocols.base import BaseProtocolFile


def main():
    if len(sys.argv) != 3:
        print "usage: "+sys.argv[0]+" <source_doc_file_name> <output_txt_file_name>"
        print "* to modify the committee meeting test file:"
        print "* $ "+sys.argv[0]+" knesset_data/protocols/tests/20_ptv_317899.doc knesset_data/protocols/tests/20_ptv_317899.txt"
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
