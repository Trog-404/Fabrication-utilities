# import os.path
#
# from nomad.client import normalize_all, parse
#
#
# def test_schema_package():
#    test_file = os.path.join('tests', 'data', 'icp.archive.yaml')
#    entry = parse(test_file)[0]
#    normalize_all(entry)
#    el = entry.data.synthesis_steps[0].fluximeters[0].elemental_composition[0].element

#    assert el is not None
