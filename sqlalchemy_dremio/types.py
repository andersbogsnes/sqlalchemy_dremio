from typing import Optional

from sqlalchemy.sql import compiler
from sqlalchemy.sql import sqltypes




class DremioTypeCompiler(compiler.GenericTypeCompiler):

    def visit_BINARY(self, type_, **kw):
        return "VARBINARY"

    def visit_VARBINARY(self, type_, **kw):
        return "VARBINARY"
