cmake_minimum_required(VERSION 3.14)
project(pingu VERSION 0.1.0)

# Set default build type to 'Release' if not specified
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "" FORCE)
endif()
message(STATUS "CMAKE_BUILD_TYPE: ${CMAKE_BUILD_TYPE}")

# Define an interface library for common compiler settings
add_library(cxx_setup INTERFACE)

# Add standard compiler warnings and set C++17 requirement
target_compile_options(cxx_setup INTERFACE -Wall -Wpedantic -Wextra)
target_compile_features(cxx_setup INTERFACE cxx_std_17)

# Add the project source directory to the include path
target_include_directories(cxx_setup INTERFACE ${PROJECT_SOURCE_DIR})


# GoogleTest requires at least C++14, but we will set C++17 
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(
  googletest 

  # reccomend updating the hash time to time
  URL URL https://github.com/google/googletest/archive/71815bbf7de6e10c11821d654a2fae2cf42de0f7.zip
)
FetchContent_MakeAvailable(googletest)

# enable testing for this project
include(CTest)

# add subdirectories
add_subdirectory(main_hub)
