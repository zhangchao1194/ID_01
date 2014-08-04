cd ./build
cmake ../
make
make install
cd ../lib
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:`pwd`
cd ../bin
<<<<<<< HEAD
./zhangPoseEstimation ../models/Person_26parts.xml test.jpg
=======
./zhangPoseEstimation ../models/Person_26parts.xml test.JPG
>>>>>>> 66f43d948b36acd21c4cd889d92fc734856ccc8a
cd ..
