from sqlalchemy.testing import exclusions
from sqlalchemy.testing.requirements import SuiteRequirements


class Requirements(SuiteRequirements):
    @property
    def binary_literals(self):
        return exclusions.open()

    @property
    def binary_comparisons(self):
        return exclusions.closed()

    @property
    def autoincrement_insert(self):
        return exclusions.closed()

    @property
    def array_type(self):
        return exclusions.closed()

    @property
    def ctes(self):
        return exclusions.open()

    @property
    def table_ddls(self):
        return exclusions.open()

    @property
    def on_update_cascade(self):
        return exclusions.closed()

    @property
    def self_referential_foreign_keys(self):
        return exclusions.closed()

    @property
    def foreign_key_ddl(self):
        return exclusions.closed()

    @property
    def named_constraints(self):
        return exclusions.closed()

    @property
    def implicitly_named_constraints(self):
        return exclusions.closed()

    @property
    def views(self):
        return exclusions.open()

    @property
    def temporary_tables(self):
        return exclusions.closed()

    @property
    def datetime_timezone(self):
        return exclusions.open()

    @property
    def update_from(self):
        return exclusions.open()

    @property
    def delete_from(self):
        return exclusions.open()

    @property
    def regexp_match(self):
        return exclusions.open()

    @property
    def regexp_replace(self):
        return exclusions.open()

    @property
    def foreign_keys(self):
        return exclusions.closed()
