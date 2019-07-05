import sys
import optparse

import parser
import template
type_alias = {}
const_dict = {}

class HeaderVisitor(object):
    def __init__(self, output):
        self.output = output

    def visitStructBegin(self, structName):
        self.output.write(template.def_struct_begin.format(name=structName))

    def visitStrcutMember(self, member_type, member_name):
        m_type = member_type
        if member_type in type_alias:
            m_type = type_alias[member_type]
        self.output.write(template.decl_struct_member.format(type = m_type, name = member_name))

    def visitStrcutArrayMember(self, member_type, member_name, dim):
        print(type(dim))
        if dim in const_dict:
            size = const_dict[dim]
        else:
            size = dim
        self.output.write(template.decl_struct_array_member.format(type = member_type, name = member_name, dim = size))

    def visitStructEnd(self):
        self.output.write(template.def_struct_end)

    def visitTypedef(self, origin, new_type):
        type_alias[new_type] = origin
        print(type_alias)
        pass

    def visitMember(self, member_type, member_name):
        pass

    def visitConst(self, const_type, const_name, const_value):
        const_dict[const_name] = const_value
        print(const_dict)
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
    # print(a_s_t)
    parser.TypeVisitor(visitor).visit(a_s_t)
    output.close()
