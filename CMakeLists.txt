project( ID_01 )
cmake_minimum_required( VERSION 2.8 )
#add_subdirectory ( ./src )
set( CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/cmake-modules )
find_package( OpenCV REQUIRED )
add_executable( run ./src/main.cpp )
target_link_libraries( run ${OpenCV_LIBS} )

