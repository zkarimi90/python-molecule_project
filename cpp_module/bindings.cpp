#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "atom.cpp"


// This file was generated with assistance from ChatGPT.


namespace py = pybind11;

PYBIND11_MODULE(my_atom, m) {
    py::class_<Atom>(m, "Atom")
        .def(py::init<std::string, int, double, double, double>())
        .def("set_coords", &Atom::set_coords)
        .def_readwrite("symbol", &Atom::symbol)
        .def_readwrite("z", &Atom::z)
        .def_readwrite("mass", &Atom::mass)
        .def_readwrite("r_single", &Atom::r_single)
        .def_readwrite("r_double", &Atom::r_double)
        .def_readwrite("coords", &Atom::coords);
}

