# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import DWI2Tensor


def test_DWI2Tensor_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        debug=dict(argstr="-debug", position=1,),
        encoding_file=dict(argstr="-grad %s", extensions=None, position=2,),
        environ=dict(nohash=True, usedefault=True,),
        ignore_slice_by_volume=dict(argstr="-ignoreslices %s", position=2, sep=" ",),
        ignore_volumes=dict(argstr="-ignorevolumes %s", position=2, sep=" ",),
        in_file=dict(argstr="%s", mandatory=True, position=-2,),
        out_filename=dict(
            argstr="%s",
            extensions=None,
            name_source="in_file",
            name_template="%s_tensor.mif",
            output_name="tensor",
            position=-1,
        ),
        quiet=dict(argstr="-quiet", position=1,),
    )
    inputs = DWI2Tensor.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_DWI2Tensor_outputs():
    output_map = dict(tensor=dict(extensions=None,),)
    outputs = DWI2Tensor.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
