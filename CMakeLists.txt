# Created with help from ChatGPT
cmake_minimum_required(VERSION 4.0)
project(pyspec LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Ensure pybind11-global is found
find_package(pybind11 CONFIG REQUIRED)

add_subdirectory(cpp_module)

