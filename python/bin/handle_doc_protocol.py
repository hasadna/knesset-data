#!/usr/bin/env python
import logging
import sys
import os


def main():
    if len(sys.argv) != 3:
        print "usage: "+sys.argv[0]+" <source_doc_file_name> <output_txt_file_name>"
        print "* to modify the handle_doc_protocol test file:"
        print "* $ "+sys.argv[0]+" knesset_data/dataservice/tests/committees/20_ptv_317899.doc knesset_data/dataservice/tests/committees/20_ptv_317899.txt"
    source_doc_file_name = sys.argv[1]
    output_txt_file_name = sys.argv[2]
    with open(source_doc_file_name) as source_doc_file:
        output_txt = CommitteeMeeting.handle_doc_protocol(source_doc_file)
        with open(output_txt_file_name, 'wb') as output_file:
                output_file.write(output_txt)

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.WARNING)
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from knesset_data.dataservice.committees import CommitteeMeeting
    main()
