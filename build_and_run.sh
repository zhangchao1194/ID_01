cd ./build
cmake ../
make
make install
cd ../lib
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:`pwd`
cd ../bin
./zhangPoseEstimation ../models/Person_26parts.xml test.JPG
