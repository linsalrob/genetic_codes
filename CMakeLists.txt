cmake_minimum_required(VERSION 3.15...3.26)
project(${SKBUILD_PROJECT_NAME} LANGUAGES C VERSION ${SKBUILD_PROJECT_VERSION})

find_package(
  Python
  COMPONENTS Interpreter Development.Module
  REQUIRED)

find_package(ZLIB)
find_package(Threads REQUIRED)
set(THREADS_PREFER_PTHREAD_FLAG ON)
python_add_library(PyGeneticCode MODULE src/pygenetic_code.c WITH_SOABI)
target_link_libraries(PyGeneticCode PRIVATE ZLIB::ZLIB Threads::Threads)

add_executable(get_orfs "")
add_subdirectory(src)
target_link_libraries(get_orfs PRIVATE ZLIB::ZLIB Threads::Threads)

install(TARGETS PyGeneticCode DESTINATION .)
