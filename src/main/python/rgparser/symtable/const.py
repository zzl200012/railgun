#-*- coding: UTF-8 -*-
#
# -----------------------------------------------------------------------------
# This file is copied from Lib/compiler/consts.py
# author : gzxuwei@corp.netease.com
# date : 2015-08-15
# -----------------------------------------------------------------------------

# operation flags
OP_ASSIGN = 'OP_ASSIGN'
OP_DELETE = 'OP_DELETE'
OP_APPLY = 'OP_APPLY'

SC_LOCAL = 1
SC_GLOBAL_IMPLICIT = 2
SC_GLOBAL_EXPLICIT = 3
SC_FREE = 4
SC_CELL = 5
SC_UNKNOWN = 6

CO_OPTIMIZED = 0x0001
CO_NEWLOCALS = 0x0002
CO_VARARGS = 0x0004
CO_VARKEYWORDS = 0x0008
CO_NESTED = 0x0010
CO_GENERATOR = 0x0020
CO_GENERATOR_ALLOWED = 0
CO_FUTURE_DIVISION = 0x2000
CO_FUTURE_ABSIMPORT = 0x4000
CO_FUTURE_WITH_STATEMENT = 0x8000
CO_FUTURE_PRINT_FUNCTION = 0x10000