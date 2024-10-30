add_executable(main main.cpp)
add_subdirectory(lib)
add_subdirectory(tests)
target_link_libraries(main PRIVATE lib cxx_setup)
