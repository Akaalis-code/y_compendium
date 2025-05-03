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

        Terminology in the order of Ascending size:-
            Nitrogenous/Nucleotide base - ACTG
            Gene - A segment in the sequence
            DNA  - Sequence of Genes
            Chromosome - 
            Cell Nucleus - 
            CELL -


    STORAGE :-
        Local files in CSV format
        Columns will be as below
            ID,GENERATION_ID,DNA,FITNESS_VALUE,PARENT_ID1,PARENT_ID2

# SETUP :

    For first time setup :
        > sudo apt install python3.12-venv          ## To install venv into your system
        > python3 -m venv ~/Documents/y_python_envs/y_env_genetic_algorithm        ## Create an vitual env 
        > . ~/Documents/y_python_envs/y_env_genetic_algorithm/bin/activate         ## activate virtual env

        > pip install pyspark
        > pip install matplotlib
        > pip install numpy
        > sudo apt install python3-tk
        > nano ~/.bashrc                            ## Add a variable in .bashrcfile
            export my_home_fldr="/home/<your PC name or some thing that comes untill Documents>"
        > source .bashrc                            ## to have those variables load in to RAM by rerunning this file
        > python3 y_initial_setup.py                ## To create files that holds information 
        > python3 y_animation.py

        (my_env) > deactivate                       ## This a shell function inside activate file , to comeout of venv
    


    For revisiting this :
        > . ~/Documents/y_python_envs/y_env_genetic_algorithm/bin/activate
        > python3 y_animation.py
