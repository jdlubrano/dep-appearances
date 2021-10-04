from dep_appearances.import_statement import ImportStatement

class TestImportStatement:
    def test_import(self):
        import_statement = ImportStatement(
            source_file="example.py",
            source_code="import foo",
            line_number=1
        )

        assert import_statement.package_name() == "foo"

    def test_leading_whitespace_import(self):
        import_statement = ImportStatement(
            source_file="example.py",
            source_code=" import foo",
            line_number=1
        )

        assert import_statement.package_name() == "foo"

    def test_from_import(self):
        import_statement = ImportStatement(
            source_file="example.py",
            source_code="from foo import bar",
            line_number=1
        )

        assert import_statement.package_name() == "foo"

    def test_leading_whitespace_from_import(self):
        import_statement = ImportStatement(
            source_file="example.py",
            source_code=" from foo import bar",
            line_number=1
        )

        assert import_statement.package_name() == "foo"


    def test_nested_import(self):
        import_statement = ImportStatement(
            source_file="example.py",
            source_code="import foo.bar",
            line_number=1
        )

        assert import_statement.package_name() == "foo"

    def test_nested_from_import(self):
        import_statement = ImportStatement(
            source_file="example.py",
            source_code="from foo.bar import Bar",
            line_number=1
        )

        assert import_statement.package_name() == "foo"

    def test_not_an_import_statement(self):
        import_statement = ImportStatement(
            source_file="example.py",
            source_code="print('Hello')",
            line_number=1
        )

        assert import_statement.package_name() is None
