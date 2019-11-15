# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..io import SQLiteSink


def test_SQLiteSink_inputs():
    input_map = dict(
        database_file=dict(extensions=None, mandatory=True,),
        table_name=dict(mandatory=True,),
    )
    inputs = SQLiteSink.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
