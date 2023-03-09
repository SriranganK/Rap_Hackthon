# Computer Vision - RAP Hackthon 2023
The model is trained using Inception V2 arch in the Tensorflow framework,The dataset was normalised from (0-255) to (0.0-1.0). In the end of the training saved as H5 format,Then Flask Web server was built with user-interface for uploading images that saved in MONGO_DB preprocessed the images .Then image is passed to the trained model, Finally the output from model showed in frontend. 

Accuracy of model: 90%
Validation Accuaracy :89%.

Home page:![1](https://i.postimg.cc/R0K5yb4t/29f663c9-2d28-44e3-a9e4-57d70699ed42.jpg)
Predicated Result:![1](https://i.postimg.cc/Twndj3pZ/7fee5f02-e12f-4afd-bb84-7488e89b4992.jpg)

##Pytorch code debugging:
From the code syntax error is might less but i am not familar with pythorch ,I worked in Tensorflow framwork, It hard to solve, but in Future We learn Pytorch. Hereby finding some error upto our knowledge.
If there is more time we will solve.

In line 49 it rise the exception becomes it value is 0 intger to pass as float 
the correct code is *assert c2f(0) == net(torch.tensor([0.0])).item(), "Model didn't learn the parameters"*



## Technologies & Framework Used:
* Python ( Flask, Tensorflow, OpenCV,  pymongo,Numpy )


## Contributors

1. [VENKAT P R](https://www.linkedin.com/in/venkat-p-r/)
2. [SRIRANGAN K](https://www.linkedin.com/in/srirangank)