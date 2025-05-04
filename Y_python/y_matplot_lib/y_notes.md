## Matplotlib Setup 

    Python vitual environment setup  -->> Because Ubuntu doesnt allow you to install any libraries of SYSTEM python
        > sudo apt install python3.12-venv
        > python3 -m venv my_env
        > source my_env/bin/activate        -->> To activate vitual enviroment
        > deactivate                        -->> To deactivate virtual environment
    
    Matplotlib library installation
        > source my_env/bin/activate
        > pip install matplotlib


## CONCEPTS

    matplotlib.pyplot
        figure
            axes
                matplotlib.pyplot  -->> This is not correct but for now think of it as circular
    
    Artist - Every thing you see on the Figure has their own individual artists like text , axis , graphs 