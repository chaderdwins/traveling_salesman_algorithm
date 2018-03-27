tspfinal.py

INTRODUCTION
tspfinal_3.py implements the Nearest Neighbor and 2-Opt algorithms to find a solution to the Travelling Salesman Problem (TSP). The TSP is the problem were there is an input file consisting of n cities, and the distance d between each two cities. The goal is to find a minium tour of the cities, where each city is visited only once and the tour, or distance, is minimized. The tour begins and ends at the same city. For this implementation we only considered the 2D (x and y) distances between the cities. We also tracked the runtime of the program for each file. 

This program uses the Nearest Neighbor algorithm if the input file size is less than 10000 bytes. If the input file size is greater than 10000 bytes then a hybrid approach of Nearest Neighbor and 2-Opt is used. In the hyprid approach Nearest Neighbor is used to find an initial tour, then 2-Opt is used to optimize the result. 

The tour length and the cities visitied, in order, are outputted to a file with the name "inpute_file".tour.


TO RUN
To run tspfinal.py, first substitute the input file name for "input_file" on line 7 and "sys.argv[1]" on line 165. For example, if the name of the input file is "tsp_example_1.txt" then line 7 would read:

tsp = TSP("tsp_example_1.txt") 

and line 165 would read:

main("tsp_example_1.txt")


Save the program, then open the command prompt, navigate to the directory that contains the source file (note that the input file should be in the same folder), and type

python tspfinal_3.py

to run the program.

