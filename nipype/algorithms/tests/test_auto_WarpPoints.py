# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..mesh import WarpPoints


def test_WarpPoints_inputs():
    input_map = dict(
        interp=dict(mandatory=True, usedefault=True,),
        out_points=dict(
            extensions=None,
            keep_extension=True,
            name_source="points",
            name_template="%s_warped",
            output_name="out_points",
        ),
        points=dict(extensions=None, mandatory=True,),
        warp=dict(extensions=None, mandatory=True,),
    )
    inputs = WarpPoints.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_WarpPoints_outputs():
    output_map = dict(out_points=dict(extensions=None,),)
    outputs = WarpPoints.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
