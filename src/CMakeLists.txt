set(SRC_FILES   DepthConsistency.cpp 
                DynamicProgram.cpp
                FileStorageModel.cpp
                HOGFeatures.cpp 
                SpatialConvolutionEngine.cpp
                FourierConvolutionEngine.cpp
                PartsBasedDetector.cpp 
                SearchSpacePruning.cpp
                StereoCameraModel.cpp
                Visualize.cpp
                nms.cpp
)

set(LIBS        ${Boost_LIBRARIES}
                ${OpenCV_LIBS}
)
message("")
message("The path of source:            ${PROJECT_SOURCE_DIR}")
message("The name of compiled library:  ${PROJECT_NAME}_lib")
# as a library (always)
add_library(${PROJECT_NAME}_lib SHARED ${SRC_FILES})
target_link_libraries(${PROJECT_NAME}_lib ${LIBS})
set_target_properties(${PROJECT_NAME}_lib PROPERTIES OUTPUT_NAME ${PROJECT_NAME})
install(TARGETS ${PROJECT_NAME}_lib 
        DESTINATION ${PROJECT_SOURCE_DIR}/lib
)

# as an executable
if (BUILD_EXECUTABLE)
    set(SRC_FILES demo.cpp)
    add_executable(${PROJECT_NAME}_bin ${SRC_FILES})
    target_link_libraries(${PROJECT_NAME}_bin ${LIBS} ${PROJECT_NAME}_lib)
    set_target_properties(${PROJECT_NAME}_bin PROPERTIES OUTPUT_NAME ${PROJECT_NAME})
    install(TARGETS ${PROJECT_NAME}_bin
            RUNTIME DESTINATION ${PROJECT_SOURCE_DIR}/bin
    )
endif()
