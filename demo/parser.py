from __future__ import print_function

import os
from pycparser import c_parser, c_ast, parse_file
import sys, os


class CHeaderParser(object):
    def __init__(self, debug=False):
        self.debug = debug
        pass

    def parse(self, CHeaderFile):
        a_s_t = None
        try:
            print("C header file is %s" % CHeaderFile)
            a_s_t = parse_file(CHeaderFile, use_cpp=True,cpp_path='gcc', cpp_args=['-E'])
            # a_s_t = parse_file(CHeaderFile)
            if self.debug: a_s_t.show(attrnames=True, nodenames=True, showcoord=False)
        except Exception:
            print("parse_file %s failed!" % CHeaderFile)
            return None
        return a_s_t

    pass

class TypeVisitor(c_ast.NodeVisitor):
    def __init__(self, visitor):
        self.visitor = visitor
        print("Define TypedefVisitor.")
        pass

    def visit_Typedef(self, node):
        print("enter visit Typedef node : %s" % node.name)
       
        if type(node.type) is type(None): return
        if type(node.type.type) is type(None): return
        real_type = node.type.type
        if isinstance(real_type, c_ast.IdentifierType):
            typename = ' '.join(real_type.names)
            self.visitor.visitTypedef(typename, node.name)
            # print(real_type)
        elif isinstance(real_type, c_ast.Struct):
            print(node.name)
            self.visitor.visitStructBegin(node.name)
            # self.visit(real_type.decls)
            for decl in real_type.decls:
                if decl.type is None or decl.type.type is None: continue
                if isinstance(decl.type, c_ast.TypeDecl):
                    member_type = ' '.join(decl.type.type.names)
                    self.visitor.visitStrcutMember(member_type, node.name)
                elif isinstance(decl.type, c_ast.ArrayDecl):
                    member_type = ' '.join(decl.type.type.type.names)
                    print(decl.type)
                    if hasattr(decl.type.dim, 'value'):
                        self.visitor.visitStrcutArrayMember(member_type, decl.name, decl.type.dim.value)
                    elif hasattr(decl.type.dim, 'name'):
                        self.visitor.visitStrcutArrayMember(member_type, decl.name, decl.type.dim.name)
            self.visitor.visitStructEnd()
        print("leave visit Typedef node : %s" % node.name)
        pass

    def visit_Decl(self, decl, no_type=False):
        print("visit_Decl")
        if decl.type is None or decl.type.type is None or decl.init is None: return
        if 'const' not in decl.quals:
            print('not const')
            return
        const_type = ' '.join(decl.type.type.names)
        self.visitor.visitConst(const_type, decl.name, decl.init.value)
        pass


    def generic_visit(self, node):
        """ Called if no explicit visitor function exists for a
            node. Implements preorder visiting of the node.
        """
        print("generic_visit node")
        if type(node) is type(None): 
            print("None type")
            return
        print(type(node))
        for c in node:
            self.visit(c)
        pass
    
# if __name__ == '__main__':
#     a_s_t = CHeaderParser().parse("./struct.h")
#     TypeVisitor().visit(a_s_t)
