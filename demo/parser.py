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
    def __init__(self):
        print("Define TypedefVisitor.")
        pass

    def visit_Typedef(self, node):
        print("enter visit Typedef node : %s" % node.name)
        self.visit(node.type)
        # self._generate_type(node, emit_declname=False)
        print("leave visit Typedef node : %s" % node.name)
        # for c in node:
        #     self.visit(c)
        # print(node.type)
        pass

    def visit_Struct(self, node):
        print("visit struct node : %s" % node.name)
        # self._generate_type(node, emit_declname=False)
        for c in node:
            self.visit(c)
        pass

    def visit_DeclList(self, node):
        print("visit_DeclList")
        if type(node.decls) is type(None): pass
        for c in node.decls:
            self.visit(c)
        pass

    def visit_Decl(self, node, no_type=False):
        print("visit_Decl")
        self.visit(node.type)
        # print(node.type.names)
        print(node.name)
        pass

    def visit_Typename(self, n):
        print("visit_Typename")
        pass

    def visit_ArrayDecl(self, n):
        print("visit_ArrayDecl")
        for c in n:
            self.visit(c)
        pass
        
    def visit_TypeDecl(self, n):
        print("visit_TypeDecl")
        # n.show()
        # self._generate_type(n, emit_declname=False)
        self.visit(n.type)
        pass
        
    def visit_PtrDecl(self, n):
        print("visit_PtrDecl")
        pass

    def visit_IdentifierType(self, n):
        print("visit_IdentifierType ")
        print(" ".join(n.names))
        pass

    def generic_visit(self, node):
        """ Called if no explicit visitor function exists for a
            node. Implements preorder visiting of the node.
        """
        print("generic_visit node")
        if type(node) is type(None): 
            print("None type")
            return
        # print(type(node))
        for c in node:
            self.visit(c)
        pass
    



# if __name__ == '__main__':
#     a_s_t = CHeaderParser().parse("./struct.h")
#     TypeVisitor().visit(a_s_t)
