import sys
import optparse

import parser
import template
typeAlise = {}
class HeaderVisitor(object):
    def __init__(self, output):
        self.output = output

    def visitStructBegin(self, name):
        self.output.write(template.def_struct_begin.format(name))
    def visitStructEnd(self, name):
        pass
    def visitTypedef(self, origin, newDefined):
        typeAlise[newDefined] = origin
        print(typeAlise)
        pass
    def visitMember(self, memberType, memberName):
        pass
    def visitConst(self, memberType, memberName, memberValue):
        pass

if __name__ == '__main__':
    arg_parser = optparse.OptionParser('%prog [options]')

    arg_parser.add_option('', '--output-file', default = 'msg.py', 
                            help='Generate python code in OUTFILES')
    arg_parser.add_option('', '--input-file',  default='msg.h',
                            help='input c++ header file')

    (opts, args) = arg_parser.parse_args()
    a_s_t = parser.CHeaderParser().parse(opts.input_file)
    
    output = open(opts.output_file, 'w')
    output.write(template.import_cstruct)

    visitor = HeaderVisitor(output)
    parser.TypeVisitor(visitor).visit(a_s_t)
    output.close()
