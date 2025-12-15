# Created with help from ChatGPT
# Build the Python extension module using pybind11-global
pybind11_add_module(atom_module
    ${CMAKE_CURRENT_SOURCE_DIR}/binding.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/atom.cpp
)

target_include_directories(atom_module
    PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}
)

install(TARGETS atom_module
        LIBRARY DESTINATION molecules
        ARCHIVE DESTINATION molecules
        RUNTIME DESTINATION molecules)


