from sqlalchemy import types
from sqlalchemy.sql import compiler


class VARBINARY(types.LargeBinary):
    __visit_name__ = "VARBINARY"


class DremioTypeCompiler(compiler.GenericTypeCompiler):
    def visit_large_binary(self, type_, **kw):
        return VARBINARY.__visit_name__

    def visit_ARRAY(self, type_, **kw):
        return "ARRAY"
