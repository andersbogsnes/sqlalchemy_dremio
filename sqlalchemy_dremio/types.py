from sqlalchemy.sql import compiler


class DremioTypeCompiler(compiler.GenericTypeCompiler):

    def visit_BINARY(self, type_, **kw):
        return "VARBINARY"

    def visit_VARBINARY(self, type_, **kw):
        return "VARBINARY"

    def visit_null(self, type_, **kw):
        return "NULL"
