# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /root/git/repos/ID_01/base/PartsBasedDetector-master

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /root/git/repos/ID_01/base/PartsBasedDetector-master/build

# Include any dependencies generated for this target.
include src/CMakeFiles/PartsBasedDetector_bin.dir/depend.make

# Include the progress variables for this target.
include src/CMakeFiles/PartsBasedDetector_bin.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/PartsBasedDetector_bin.dir/flags.make

src/CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.o: src/CMakeFiles/PartsBasedDetector_bin.dir/flags.make
src/CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.o: ../src/demo.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /root/git/repos/ID_01/base/PartsBasedDetector-master/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object src/CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.o"
	cd /root/git/repos/ID_01/base/PartsBasedDetector-master/build/src && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.o -c /root/git/repos/ID_01/base/PartsBasedDetector-master/src/demo.cpp

src/CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.i"
	cd /root/git/repos/ID_01/base/PartsBasedDetector-master/build/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /root/git/repos/ID_01/base/PartsBasedDetector-master/src/demo.cpp > CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.i

src/CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.s"
	cd /root/git/repos/ID_01/base/PartsBasedDetector-master/build/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /root/git/repos/ID_01/base/PartsBasedDetector-master/src/demo.cpp -o CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.s

src/CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.o.requires:
.PHONY : src/CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.o.requires

src/CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.o.provides: src/CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.o.requires
	$(MAKE) -f src/CMakeFiles/PartsBasedDetector_bin.dir/build.make src/CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.o.provides.build
.PHONY : src/CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.o.provides

src/CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.o.provides.build: src/CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.o

# Object files for target PartsBasedDetector_bin
PartsBasedDetector_bin_OBJECTS = \
"CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.o"

# External object files for target PartsBasedDetector_bin
PartsBasedDetector_bin_EXTERNAL_OBJECTS =

src/PartsBasedDetector: src/CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.o
src/PartsBasedDetector: /usr/lib/libboost_system-mt.so
src/PartsBasedDetector: /usr/lib/libboost_filesystem-mt.so
src/PartsBasedDetector: /usr/lib/libboost_signals-mt.so
src/PartsBasedDetector: /usr/local/lib/libopencv_videostab.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_video.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_ts.a
src/PartsBasedDetector: /usr/local/lib/libopencv_superres.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_stitching.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_photo.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_ocl.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_objdetect.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_nonfree.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_ml.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_legacy.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_imgproc.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_highgui.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_gpu.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_flann.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_features2d.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_core.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_contrib.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_calib3d.so.2.4.7
src/PartsBasedDetector: src/libPartsBasedDetector.so
src/PartsBasedDetector: /usr/lib/libboost_system-mt.so
src/PartsBasedDetector: /usr/lib/libboost_filesystem-mt.so
src/PartsBasedDetector: /usr/lib/libboost_signals-mt.so
src/PartsBasedDetector: /usr/local/lib/libopencv_videostab.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_ts.a
src/PartsBasedDetector: /usr/lib/x86_64-linux-gnu/libGLU.so
src/PartsBasedDetector: /usr/lib/x86_64-linux-gnu/libGL.so
src/PartsBasedDetector: /usr/lib/x86_64-linux-gnu/libSM.so
src/PartsBasedDetector: /usr/lib/x86_64-linux-gnu/libICE.so
src/PartsBasedDetector: /usr/lib/x86_64-linux-gnu/libX11.so
src/PartsBasedDetector: /usr/lib/x86_64-linux-gnu/libXext.so
src/PartsBasedDetector: /usr/local/lib/libopencv_superres.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_stitching.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_contrib.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_nonfree.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_ocl.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_gpu.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_photo.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_objdetect.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_legacy.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_video.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_ml.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_calib3d.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_features2d.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_highgui.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_imgproc.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_flann.so.2.4.7
src/PartsBasedDetector: /usr/local/lib/libopencv_core.so.2.4.7
src/PartsBasedDetector: src/CMakeFiles/PartsBasedDetector_bin.dir/build.make
src/PartsBasedDetector: src/CMakeFiles/PartsBasedDetector_bin.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable PartsBasedDetector"
	cd /root/git/repos/ID_01/base/PartsBasedDetector-master/build/src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/PartsBasedDetector_bin.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/CMakeFiles/PartsBasedDetector_bin.dir/build: src/PartsBasedDetector
.PHONY : src/CMakeFiles/PartsBasedDetector_bin.dir/build

src/CMakeFiles/PartsBasedDetector_bin.dir/requires: src/CMakeFiles/PartsBasedDetector_bin.dir/demo.cpp.o.requires
.PHONY : src/CMakeFiles/PartsBasedDetector_bin.dir/requires

src/CMakeFiles/PartsBasedDetector_bin.dir/clean:
	cd /root/git/repos/ID_01/base/PartsBasedDetector-master/build/src && $(CMAKE_COMMAND) -P CMakeFiles/PartsBasedDetector_bin.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/PartsBasedDetector_bin.dir/clean

src/CMakeFiles/PartsBasedDetector_bin.dir/depend:
	cd /root/git/repos/ID_01/base/PartsBasedDetector-master/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /root/git/repos/ID_01/base/PartsBasedDetector-master /root/git/repos/ID_01/base/PartsBasedDetector-master/src /root/git/repos/ID_01/base/PartsBasedDetector-master/build /root/git/repos/ID_01/base/PartsBasedDetector-master/build/src /root/git/repos/ID_01/base/PartsBasedDetector-master/build/src/CMakeFiles/PartsBasedDetector_bin.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/CMakeFiles/PartsBasedDetector_bin.dir/depend
