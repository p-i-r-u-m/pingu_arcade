# BUILD_TESTING variable is created by include (CTest)
# Is is set to ON by default
if(BUILD_TESTING)
  add_executable(unit_tests unit-tests.cpp)
  target_link_libraries(unit_tests PRIVATE GTest::gtest_main)
  target_link_libraries(unit_tests PRIVATE lib cxx_setup)

  include(GoogleTest)
  # Finds all the Google tests associated with add_executable
  gtest_discover_tests(unit_tests)
endif()
