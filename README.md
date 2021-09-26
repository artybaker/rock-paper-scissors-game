# rock-paper-scissors-game
    A python application used for you to play a game of rock, paper, scissors against the computer. 
# Prerequisites
    - Anaconda 3.7
    - Python 3.7
    - Pip
# Repo Setup & Installation 
Fork this [remote repository](https://github.com/basilbseiso/rock-paper-scissors-game) under your own control and "clone" or download your remote copy onto your local device. 
Following this step, navigate from the command line to the root directory before you run other commands. 
    
    cd rock-paper-scissors-game
# Environment Setup
Since we are using environment variables and require a third party package to read them from the ".env" file, we need to use a new and different specific python environment which will allow us to install the necessary packages. 

Create and activate a new Anaconda virtual environment that is specific for the project. 

    conda create -n my-game-env python=3.8 # first time only
    conda activate my-game-env

After activating the virtual environment, install package dependencies

    pip install -r requirements.txt
# Customization
In the root directory of your local repository create a new file called ".env" and update the contents of the file to specify your player name. Also be sure to save the ".env" file once your finished setting it up. 

    PLAYER_NAME="Player One"
# Usage
Run the python script on your local terminal 

    python game.py