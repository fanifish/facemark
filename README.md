# facemark


## initial installation
### working with python2
   1/ Install conda python package manager ### using this link https://repo.continuum.io/archive/Anaconda2-5.0.1-Linux-x86_64.sh
   2/ using conda install the required python packages
      - conda install numpy
      - conda install -c conda-forge opencv
      - conda install -c menpo dlib
   


## Runing code
 ### on the top level directory execute
 python face-mask.py --shape-predictor ./models/shape_predictor_68_face_landmarks.dat --image images/leo.jpeg
