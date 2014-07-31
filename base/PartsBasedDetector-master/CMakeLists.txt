project(zhangPoseEstimation)
cmake_minimum_required(VERSION 2.8.5)

# self defined variables
option(BUILD_EXECUTABLE "Build as executable to test functionality"                     ON)
option(BUILD_DOC        "Build documentation with Doxygen"                              ON)
option(WITH_OPENMP      "Build with OpenMP support for multithreading"                  ON)
option(WITH_OPENCV      "Build with OpenCV"                                             ON)
option(WITH_BOOST       "Build with BOOST"                                              ON)

# include all warning types
#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Werror -Wno-unused-parameter -Wno-unused-variable -pedantic")

# set the build type
if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE RelWithDebInfo CACHE STRING
        "Choose the type of build. Options are: None, Debug, Release, RelWithDebInfo, MinSizeRel"
    FORCE)
endif()

# set as 64 bit application
SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -m64")
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m64")

# add OpenMP support
if (WITH_OPENMP)
    find_package(OpenMP QUIET)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
    set(CMAKE_C_FLAGS   "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    if (NOT OPENMP_FOUND)
        set(WITH_OPENMP OFF)
    endif()
endif()

# add vectorization support
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -msse4.1")
set(CMAKE_C_FLAGS   "${CMAKE_C_FLAGS} -msse4.1")

# use highest level of optimization in Release mode
if ("${CMAKE_BUILD_TYPE}" STREQUAL "Release")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")
    set(CMAKE_C_FLAGS   "${CMAKE_C_FLAGS} -O3")
endif ()

# find the dependencies
if (WITH_BOOST)
find_package(Boost COMPONENTS system filesystem signals REQUIRED)
endif ()

if (WITH_OPENCV)
find_package(OpenCV REQUIRED)
endif ()

# include the dependencies
include_directories(SYSTEM  ${OpenCV_INCLUDE_DIRS}
                            ${Boost_INCLUDE_DIRS}
)
include_directories(include)


# add documentation
if(BUILD_DOC)
    find_package(Doxygen)
    configure_file(${PROJECT_SOURCE_DIR}/doc/Doxyfile.in ${PROJECT_SOURCE_DIR}/doc/Doxyfile @ONLY)
    add_custom_target(${PROJECT_NAME}_doc ALL ${DOXYGEN_EXECUTABLE} ${PROJECT_SOURCE_DIR}/doc/Doxyfile)
endif()


# add subdirectories
add_subdirectory(src)

# link_directories()
# build summary
message("")
message("---------------------------------------------")
message(${PROJECT_NAME} " Configuration Summary")
message("")
message("Project name:                  ${PROJECT_NAME}")
message("c++ build flags:               ${CMAKE_CXX_FLAGS}")
message("c build flags:                 ${CMAKE_C_FLAGS}")
message("Build type:                    ${CMAKE_BUILD_TYPE}")
message("Build with threading (OpenMP): ${WITH_OPENMP}")
message("Build as executable:           ${BUILD_EXECUTABLE}")
message("Build with documentation:      ${BUILD_DOC}")
message("Build with OpenCV:             ${WITH_OPENCV}")
message("Build with Boost:              ${WITH_BOOST}")
message("")
message("Include file directories:")
get_property(dirs DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY INCLUDE_DIRECTORIES)
foreach(dir ${dirs})
  message(STATUS "dir='${dir}'")
endforeach()
message("")
message("Link file directories:")
get_property(dirs DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY LINK_DIRECTORIES)
foreach(dir ${dirs})
  message(STATUS "dir='${dir}'")
endforeach()
message("---------------------------------------------")
message("")
