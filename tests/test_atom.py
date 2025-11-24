import pytest
from molecules.atom import Atom

def test_atom_creation_symbol():
    a = Atom(symbol="C", coords=(1.0, 2.0, 3.0))
    assert a.symbol == "c"
    assert a.z == 6
    assert a.mass == 12.011
    assert a.coords == (1.0, 2.0, 3.0)

def test_atom_creation_z():
    a = Atom(z=8, coords=(0.0, 0.0, 0.0))
    assert a.symbol == "o"
    assert a.z == 8
    assert a.mass == 15.999

def test_atom_set_coords():
    a = Atom(symbol="h")
    a.set_coords(1.1, 2.2, 3.3)
    assert a.coords == (1.1, 2.2, 3.3)

def test_atom_invalid_symbol():
    with pytest.raises(KeyError):
        Atom(symbol="Xx")

def test_atom_invalid_z():
    with pytest.raises(KeyError):
        Atom(z=999)

