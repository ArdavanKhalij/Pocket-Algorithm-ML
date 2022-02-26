# Pocket-Algorithm-ML
Programming Exercise 1(Ex 3.2 (book: Learning from Data))</br>
Take d = 2 and create a data set D of size N = 100 that is not linearly
separable. You can do so by first choosing a random line in the plane as your
target function and the inputs xn of the data set as random points in the plane.
Then, evaluate the target function on each xn to get the corresponding output
yn. Finally, flip the labels of N randomly selected yn’s and the data set will 10
likely become non separable.</br>
Now, try the pocket algorithm on your data set using T = 1000 iterations.</br>
Repeat the experiment 20 times. Then, plot the average Ein(w(t)) and the average Ein(wˆ)(which is also a function of t) on the same figure and see how they behave when t increases. Similarly, use a test set of size 1000 and plot a figure to show how Eout(w(t)) and Eout(wˆ) behave.</br>
