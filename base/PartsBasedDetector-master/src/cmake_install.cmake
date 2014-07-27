# Install script for directory: /root/git/repos/ID_01/base/PartsBasedDetector-master/src

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/usr/local")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  IF(EXISTS "$ENV{DESTDIR}/root/git/repos/ID_01/base/PartsBasedDetector-master/src/lib/libProject.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/root/git/repos/ID_01/base/PartsBasedDetector-master/src/lib/libProject.so")
    FILE(RPATH_CHECK
         FILE "$ENV{DESTDIR}/root/git/repos/ID_01/base/PartsBasedDetector-master/src/lib/libProject.so"
         RPATH "")
  ENDIF()
  list(APPEND CPACK_ABSOLUTE_DESTINATION_FILES
   "/root/git/repos/ID_01/base/PartsBasedDetector-master/src/lib/libProject.so")
FILE(INSTALL DESTINATION "/root/git/repos/ID_01/base/PartsBasedDetector-master/src/lib" TYPE SHARED_LIBRARY FILES "/root/git/repos/ID_01/base/PartsBasedDetector-master/src/libProject.so")
  IF(EXISTS "$ENV{DESTDIR}/root/git/repos/ID_01/base/PartsBasedDetector-master/src/lib/libProject.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/root/git/repos/ID_01/base/PartsBasedDetector-master/src/lib/libProject.so")
    IF(CMAKE_INSTALL_DO_STRIP)
      EXECUTE_PROCESS(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/root/git/repos/ID_01/base/PartsBasedDetector-master/src/lib/libProject.so")
    ENDIF(CMAKE_INSTALL_DO_STRIP)
  ENDIF()
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(CMAKE_INSTALL_COMPONENT)
  SET(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
ELSE(CMAKE_INSTALL_COMPONENT)
  SET(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
ENDIF(CMAKE_INSTALL_COMPONENT)

FILE(WRITE "/root/git/repos/ID_01/base/PartsBasedDetector-master/src/${CMAKE_INSTALL_MANIFEST}" "")
FOREACH(file ${CMAKE_INSTALL_MANIFEST_FILES})
  FILE(APPEND "/root/git/repos/ID_01/base/PartsBasedDetector-master/src/${CMAKE_INSTALL_MANIFEST}" "${file}\n")
ENDFOREACH(file)
