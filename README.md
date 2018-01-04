# facemark </br>


## initial installation </br>
    working with python2
   1/ Install conda python package manager [https://repo.continuum.io/archive/Anaconda2-5.0.1-Linux-x86_64.sh] </br>
   2/ using conda install the required python packages </br>
      - conda install numpy </br>
      - conda install -c conda-forge opencv </br>
      - conda install -c menpo dlib </br>
   3/ pip install imutils </br>
   
   
## Running code </br>
 ### on the top level directory execute </br>
 python face-mask.py --shape-predictor ./models/shape_predictor_68_face_landmarks.dat --image images/leo.jpeg </br>
