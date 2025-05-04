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
        4)Crossover and mutation
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
    
    Crossover and mutation (plan) :
        parent1 = [4,7,16,....20..................,9]
        parent2 = [15,..4,2,11,14..7,3,....20.....,6]

        offspring 1 :
            Start with parent1's first gene and calculate the best succeding gene to the preceeding 
            by comparing in both both parent genes

            For example :

                STEP1:
                    In parent 1 while starting at "4" find out which sequence is better 
                    is it parent1's "4,7" or parent2's "4,2"
                    whichever is best will be passed to offspring.

                STEP2 :
                    If "4,7" is decided as best , continue to next step
                STEP3 :
                    If "4,2" is decided as best follow STEP 3.5
                STEP3.5 :
                    While evaluating if the best selected value is already used up , take the runnerup value ,
                    if runner up value is also usedup go for random selection until non used value shows up.

                    If in Parent2 edge is detected let the parent1's sequence be selected

                    If and onlyif the above scenarios have not come up 
                    in parent1_temp's sequence swap "2" and "7" positions
                Step4:
                    Move forward to next gene and follow same steps from STEP1
        
        offspring 2:
            Follow the same steps as in creation of offspring1 ,
            but the only change is while taking the sequence from parent2 we will skip one gene in between 

            For example :
                For evaluation process
                Parent1 gives "4,7"  but parent2 gives "4,11" instead of "4,2" it skips '2'
        
        offspring 3:
            Follow the same steps as in creation of offspring1 ,
            but the only change is while taking the sequence from parent2 we will skip TWO genes in between 

            For example :
                For evaluation process
                Parent1 gives "4,7"  but parent2 gives "4,14" instead of "4,2" it skips '2' and '11'


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


# CHECKPOINT for next visit :
    in y_cross_mutator.py--->> mth_cross_mutation()