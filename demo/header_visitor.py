import sys

class HeaderVisitor(object):
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

