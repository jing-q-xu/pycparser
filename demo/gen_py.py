import sys
import optparse

import parser
import template

class HeaderVisitor(object):
    def __init__(self, output):
        self.output = output

    def visitStructBegin(self, name):
        self.output.write(template.def_struct_begin.)
    def visitStructEnd(self, name):
        raise NotImplementedError
    def visitTypedef(self, origin, newDefined):
        raise NotImplementedError
    def visitMember(self, memberType, memberName):
        raise NotImplementedError
    def visitConst(self, memberType, memberName, memberValue):
        raise NotImplementedError

if __name__ == '__main__':
    arg_parser = optparse.OptionParser('%prog [options]')

    arg_parser.add_option('', '--output-file', default = 'msg.py', 
                            help='Generate python code in OUTFILES')
    arg_parser.add_option('', '--input-file',  default='msg.h',
                            help='input c++ header file')

    a_s_t = parser.CHeaderParser().parse(opts.input_file)
    
    output = open(opts.output_file, 'w')
    output.write(template.import_cstruct)

    visitor = HeaderVisitor(output)
    parser.TypeVisitor(visitor).visit(a_s_t)
    output.close()
