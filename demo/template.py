import_cstruct = r'''
#!/usr/bin/python
import cstruct
'''

def_struct_begin = r'''
class {name}(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = r"""
'''

def_struct_end = r'''
    """
'''

decl_struct_member = '        {type} {name};\n'

decl_struct_array_member = '        {type} {name}[{dim}];\n'