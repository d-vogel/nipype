# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..dcmstack import CopyMeta


def test_CopyMeta_inputs():
    input_map = dict(
        dest_file=dict(extensions=None, mandatory=True,),
        exclude_classes=dict(),
        include_classes=dict(),
        src_file=dict(extensions=None, mandatory=True,),
    )
    inputs = CopyMeta.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_CopyMeta_outputs():
    output_map = dict(dest_file=dict(extensions=None,),)
    outputs = CopyMeta.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
