import_cstruct = r'''
#!/usr/bin/python
import cstruct
'''

def_strct_begin = r'''
class {name}(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = \"\"\"
'''
