from sqlalchemy.testing.suite import ArgSignatureTest as _ArgSignatureTest
from sqlalchemy.testing.suite import BitwiseTest as _BitwiseTest
from sqlalchemy.testing.suite import CTETest as _CteTest
from sqlalchemy.testing.suite import CollateTest as _CollateTest
from sqlalchemy.testing.suite import ComponentReflectionTest as _ComponentReflectionTest
from sqlalchemy.testing.suite import ComponentReflectionTestExtra as _ComponentReflectionTestExtra
from sqlalchemy.testing.suite import CompositeKeyReflectionTest as _CompositeKeyReflectionTest
from sqlalchemy.testing.suite import CompoundSelectTest as _CompoundSelectTest
from sqlalchemy.testing.suite import ComputedColumnTest as _ComputedColumnTest
from sqlalchemy.testing.suite import ComputedReflectionTest as _ComputedReflectionTest
from sqlalchemy.testing.suite import DeprecatedCompoundSelectTest as _DeprecatedCompoundSelectTest
from sqlalchemy.testing.suite import DifficultParametersTest as _DifficultParametersTest
from sqlalchemy.testing.suite import EscapingTest as _EscapingTest
from sqlalchemy.testing.suite import ExceptionTest as _ExceptionTest
from sqlalchemy.testing.suite import ExistsTest as _ExistsTest
from sqlalchemy.testing.suite import ExpandingBoundInTest as _ExpandingBoundInTest
from sqlalchemy.testing.suite import FetchLimitOffsetTest as _FetchLimitOffsetTest
from sqlalchemy.testing.suite import HasTableTest as _HasTableTest
from sqlalchemy.testing.suite import IdentityColumnTest as _IdentityColumnTest
from sqlalchemy.testing.suite import IdentityReflectionTest as _IdentityReflectionTest
from sqlalchemy.testing.suite import InsertBehaviorTest as _InsertBehaviorTest
from sqlalchemy.testing.suite import IsOrIsNotDistinctFromTest as _IsOrIsNotDistinctFromTest
from sqlalchemy.testing.suite import JoinTest as _JoinTest
from sqlalchemy.testing.suite import LikeFunctionsTest as _LikeFunctionsTest
from sqlalchemy.testing.suite import LongNameBlowoutTest as _LongNameBlowoutTest
from sqlalchemy.testing.suite import NormalizedNameTest as _NormalizedNameTest
from sqlalchemy.testing.suite import OrderByLabelTest as _OrderByLabelTest
from sqlalchemy.testing.suite import PercentSchemaNamesTest as _PercentSchemaNamesTest
from sqlalchemy.testing.suite import PingTest as _PingTest
from sqlalchemy.testing.suite import PostCompileParamsTest as _PostCompileParamsTest
from sqlalchemy.testing.suite import QuotedNameArgumentTest as _QuotedNameArgumentTest
from sqlalchemy.testing.suite import RowCountTest as _RowCountTest
from sqlalchemy.testing.suite import RowFetchTest as _RowFetchTest
from sqlalchemy.testing.suite import SameNamedSchemaTableTest as _SameNamedSchemaTableTest
from sqlalchemy.testing.suite import SimpleUpdateDeleteTest as _SimpleUpdateDeleteTest
from sqlalchemy.testing.suite import TableDDLTest as _TableDDLTest
from sqlalchemy.testing.suite import TableNoColumnsTest as _TableNoColumnsTest
from sqlalchemy.testing.suite import UnicodeSchemaTest as _UnicodeSchemaTest
from sqlalchemy.testing.suite import ValuesExpressionTest as _ValuesExpressionTest
from sqlalchemy.testing.suite import WeCanSetDefaultSchemaWEventsTest as _T
from sqlalchemy.testing.suite import WindowFunctionTest as _WindowFunctionTest
from sqlalchemy.testing.suite.test_types import *  # noqa


class SimpleUpdateDeleteTest(_SimpleUpdateDeleteTest):
    pass


class UnicodeSchemaTest(_UnicodeSchemaTest):
    pass


class BitwiseTest(_BitwiseTest):
    pass


class WindowFunctionTest(_WindowFunctionTest):
    pass


class IsOrIsNotDistinctFromTest(_IsOrIsNotDistinctFromTest):
    pass


class ExistsTest(_ExistsTest):
    pass


class IdentityColumnTest(_IdentityColumnTest):
    pass


class ComputedColumnTest(_ComputedColumnTest):
    pass


class LikeFunctionsTest(_LikeFunctionsTest):
    pass


class ExpandingBoundInTest(_ExpandingBoundInTest):
    pass


class PostCompileParamsTest(_PostCompileParamsTest):
    pass


class CompoundSelectTest(_CompoundSelectTest):
    pass


class JoinTest(_JoinTest):
    pass


class SameNamedSchemaTableTest(_SameNamedSchemaTableTest):
    pass


class FetchLimitOffsetTest(_FetchLimitOffsetTest):
    pass


class ValuesExpressionTest(_ValuesExpressionTest):
    pass


class OrderByLabelTest(_OrderByLabelTest):
    pass


class CollateTest(_CollateTest):
    pass


class RowCountTest(_RowCountTest):
    pass


class PercentSchemaNamesTest(_PercentSchemaNamesTest):
    pass


class RowFetchTest(_RowFetchTest):
    pass


class TableNoColumnsTest(_TableNoColumnsTest):
    pass


class QuotedNameArgumentTest(_QuotedNameArgumentTest):
    pass


class HasTableTest(_HasTableTest):
    pass


class NormalizedNameTest(_NormalizedNameTest):
    pass


class ComputedReflectionTest(_ComputedReflectionTest):
    pass


class IdentityReflectionTest(_IdentityReflectionTest):
    pass


class CompositeKeyReflectionTest(_CompositeKeyReflectionTest):
    pass


class CteTest(_CteTest):
    pass


class ComponentReflectionTest(_ComponentReflectionTest):
    pass


class ComponentReflectionTestExtra(_ComponentReflectionTestExtra):
    pass


class TableDDLTest(_TableDDLTest):
    pass


class LongNameBlowoutTest(_LongNameBlowoutTest):
    pass


class DeprecatedCompoundSelectTest(_DeprecatedCompoundSelectTest):
    pass


class PingTest(_PingTest):
    pass


class ArgSignatureTest(_ArgSignatureTest):
    pass


class ExceptionTest(_ExceptionTest):
    pass


class EscapingTest(_EscapingTest):
    pass


class WeCanSetDefaultSchemaWEventsTest(_T):
    pass


class DifficultParametersTest(_DifficultParametersTest):
    pass


class InsertBehaviorTest(_InsertBehaviorTest):
    pass
