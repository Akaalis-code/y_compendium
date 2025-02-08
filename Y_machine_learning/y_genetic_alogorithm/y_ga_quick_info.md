# GOAL :
    1)  you have 20 points , Find the order in which if you traverse, 
        it will give least possible distance path

# ARCHITECHTURE :

    python              ->  Control language
    matplotlib          ->  For animation
    Genetic algorithm   ->  Machine learning strategy
    Local files         ->  Storage of Populations DNA


    GENETIC AGORITHM :-
        1)Population in the generation
        2)Fitness Screening
        3)Pair Selection for next generation creation
        4)Crossver and mutation
        5)Start again at step 1

        Terminology :-
            Gene - Each individual point in the sequence
            DNA  - Sequence of Genes


    STORAGE :-
        Local files in CSV format
        Columns will be as below
            ID,GENERATION_ID,DNA,FITNESS_VALUE,PARENT_ID1,PARENT_ID2

# SETUP :

    > pip install pyspark
    > pip install matplotlib
    > sudo apt install python3-tk
    > python3 y_animation.py