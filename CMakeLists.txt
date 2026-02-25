cmake_minimum_required(VERSION 3.15)
project(DeepThinner LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# --- Locate Nuke NDK ---
if(NOT DEFINED NUKE_INSTALL_PATH)
    message(FATAL_ERROR
        "Set NUKE_INSTALL_PATH to your Nuke 16 installation directory, e.g.\n"
        "  cmake -DNUKE_INSTALL_PATH=\"C:/Program Files/Nuke16.0v8\" ..")
endif()

set(NUKE_INCLUDE_DIR "${NUKE_INSTALL_PATH}/include")
set(NUKE_LIB_DIR     "${NUKE_INSTALL_PATH}")

# --- Plugin shared library ---
add_library(DeepThinner SHARED src/DeepThinner.cpp)

target_include_directories(DeepThinner PRIVATE "${NUKE_INCLUDE_DIR}")
target_link_directories(DeepThinner    PRIVATE "${NUKE_LIB_DIR}")
target_link_libraries(DeepThinner      PRIVATE DDImage)

# No "lib" prefix on any platform
set_target_properties(DeepThinner PROPERTIES PREFIX "")

# --- Platform-specific settings ---
if(WIN32)
    target_compile_definitions(DeepThinner PRIVATE
        NOMINMAX
        _USE_MATH_DEFINES
        FN_OS_WINDOWS
        WIN32_LEAN_AND_MEAN
    )
    set_target_properties(DeepThinner PROPERTIES SUFFIX ".dll")
elseif(APPLE)
    set_target_properties(DeepThinner PROPERTIES SUFFIX ".dylib")
else()
    set_target_properties(DeepThinner PROPERTIES SUFFIX ".so")
    target_compile_definitions(DeepThinner PRIVATE USE_GLEW)
endif()

# Release optimisations by default
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()
