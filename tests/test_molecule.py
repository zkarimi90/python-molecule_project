import numpy as np
from molecules import Atom, Molecule

def test_add_atom_and_get_coords():
    m = Molecule()
    a1 = Atom("h", coords=(0,0,0))
    a2 = Atom("o", coords=(1,0,0))
    m.add_atom(a1)
    m.add_atom(a2)
    coords = m.get_coords()
    assert coords.shape == (2, 3)
    assert np.allclose(coords[1], [1,0,0])

def test_translate_molecule():
    m = Molecule([Atom("h", coords=(0,0,0)), Atom("o", coords=(1,0,0))])
    m.translate([1,1,1])
    coords = m.get_coords()
    assert np.allclose(coords[0], [1,1,1])
    assert np.allclose(coords[1], [2,1,1])

def test_rotate_molecule_90_deg_z():
    m = Molecule([Atom("h", coords=(1,0,0))])
    m.rotate(axis=(0,0,1), angle_deg=90)
    coords = m.get_coords()
    assert np.allclose(coords[0], [0,1,0], atol=1e-7)

def test_stretch_bond():
    m = Molecule([Atom("h", coords=(0,0,0)), Atom("h", coords=(1,0,0))])
    m.stretch_bond(0, 1, 1.0)
    coords = m.get_coords()
    assert np.allclose(coords[1], [2,0,0])

