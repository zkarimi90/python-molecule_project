import numpy as np
import pytest
from molecules.atom import Atom
from molecules.io import read_xyz, write_xyz

def test_write_and_read_xyz(tmp_path):
    atoms = [Atom("h", coords=(0,0,0)), Atom("o", coords=(1,0,0))]
    file_path = tmp_path / "test.xyz"
    
    write_xyz(file_path, atoms)
    read_atoms = read_xyz(file_path)
    
    assert len(read_atoms) == 2
    assert read_atoms[0].symbol == "h"
    assert np.allclose(read_atoms[1].coords, [1,0,0])

