# Pre-trained Image Classifier to Identify Dog Breeds
## Description:
Your city is hosting a citywide dog show and you have volunteered to help the organizing committee with contestant registration. Every participant that registers must submit an image of their dog along with biographical information about their dog. The registration system tags the images based upon the biographical information.

Some people are planning on registering pets that aren’t actual dogs.

You need to use an already developed Python classifier to make sure the participants are dogs.

## Tasks:
* Using Python skills, you will determine which image classification algorithm works the "best" on classifying images as "dogs" or "not dogs".
* Determine how well the "best" classification algorithm works on correctly identifying a dog's breed. If you are confused by the term image classifier look at it simply as a tool that has an input and an output. The Input is an image. The 
  output determines what the image depicts. (for example, a dog). Be mindful of the fact that image classifiers do not always categorize the images correctly.
* Time how long each algorithm takes to solve the classification problem. With computational tasks, there is often a trade-off between accuracy and runtime. The more accurate an algorithm, the higher the likelihood that it will take more 
  time to run and use more computational resources to run.

## Principal Objectives:
* Correctly identify which pet images are of dogs (even if the breed is misclassified) and which pet images aren't of dogs.  
* Correctly classify the breed of dog, for the images that are of dogs.  
* Determine which CNN model architecture (ResNet, AlexNet, or VGG), "best" achieve objectives 1 and 2.  
* Consider the time resources required to best achieve objectives 1 and 2, and determine if an alternative solution would have given a "good enough" result, given the amount of time each of the algorithms takes to run.

## Project outline:
* Time your program
  Use Time Module to compute program runtime
* Get program Inputs from the user
  Use command line arguments to get user inputs
* Create Pet Images Labels
  Use the pet images filenames to create labels
  Store the pet image labels in a data structure (e.g. dictionary)
* Create Classifier Labels and Compare Labels
  Use the Classifier function to classify the images and create the classifier labels
  Compare Classifier Labels to Pet Image Labels
  Store Pet Labels, Classifier Labels, and their comparison in a complex data structure (e.g. dictionary of   lists)
* Classifying Labels as "Dogs" or "Not Dogs"
  Classify all Labels as "Dogs" or "Not Dogs" using dognames.txt file
  Store new classifications in the complex data structure (e.g. dictionary of lists)
* Calculate the Results
  Use Labels and their classifications to determine how well the algorithm worked on classifying images
* Print the Results
