import visitor
import sys, os

class CppEncoder(visitor.HeaderVisitor):
    def __init__(self, file_name):
        self.fd = open(file_name)
        
    def visitStructBegin(self, name):
        raise NotImplementedError
    def visitStructEnd(self, name):
        raise NotImplementedError
    def visitTypedef(self, origin, newDefined):
        raise NotImplementedError
    def visitMember(self, memberType, memberName):
        raise NotImplementedError
    def visitConst(self, memberType, memberName, memberValue):
        raise NotImplementedError
    
    def close(self):
        self.fd.close()

if __name__ == '__main__':
    a_s_t = CHeaderParser().parse("./struct.h")
    CppEncoder("1.cpp").visit(a_s_t)

