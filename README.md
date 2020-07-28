# custom-text-model
This repository contains a custom implementation of the classes in Sci-Kit Learn to make text analysis smoother and more efficient.
The class uses Support Vector Machine as the base class, but any other class can be used and the code will be the same (ex: GuassianNB, NearestCentroid, etc.).
The main purpose of building a custom model like this is to bypass the vectorization phase during a text classification project. Here, the text vectorization is automatically performed by the model, so raw data can be fed in without any errors.
To actually make use of this, you should import this class during your project and use this model instead of the standard SKLearn modules.
