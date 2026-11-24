import pytest
import graphics.triplanar_blend as mod

CASES = [
    ("normalize_weights", (1,)),
    ("smooth_weight_transition", (1,)),
    ("sample_after_upload", (1,)),
    ("sampler_per_instance", (1,)),
    ("coords_relative_origin", (1,)),
    ("blend_at_seam", (1,)),
    ("bind_material", (1,)),
    ("load", (1,)),
    ("render", (1,)),
    ("sample", (1,)),
    ("validate_triplanar", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
