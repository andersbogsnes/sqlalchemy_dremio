from sqlalchemy.testing.suite import *
from sqlalchemy.testing import skip
from sqlalchemy.testing.suite import BinaryTest as _BinaryTest


class BinaryTest(_BinaryTest):
    @skip("dremio", reason="Need to implement CAST(val as VARBINARY) behaviour on insert")
    def test_binary_roundtrip(self, connection, data):
        return

    @skip("dremio", reason="Need to implement CAST(val as VARBINARY) behaviour on insert")
    def test_pickle_roundtrip(self, connection):
        return
