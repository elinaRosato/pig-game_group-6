# Pig Game - Examination 2

By Dario Ostojic, Simon Persson and Elina Rosato

This is a Python implementation of the classic dice game Pig. The game is designed to be played in the terminal and offers a simple yet entertaining experience.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Structure](#structure)
- [Testing](#testing)
- [Code Analysis](#code-analysis)
- [Documentation](#documentation)
- [License](#license)

## Introduction
Pig Game is a text-based game where players take turns rolling a die to accumulate points. The objective is to reach a score of 100 before your opponent. The game can be played against the computer or with two players.

## Installation
To run the Pig Game, follow these steps:

### Step 1:
Clone the repository to your local machine: 
git clone https://github.com/your-username/pig-game.git

### Step 2: 
Navigate to the project directory

### Step 3:
Create and activate a virtual environment:
make venv
. .venv/bin/activate

### Step 4:
Install dependencies
make install

## Usage
To play the Pig Game, execute the following command in the terminal:
make run

## Structure

-------------------------------------------------------------------------------------


# DRAFT 2:
# Introduction

This guide intends to help with the setup proces for being able to run the game and also provide some guidance about the funcionalities included.

It is important to note that all the commands in this documentation file starting with `$` do not require that `$` when executing them. This `$` is only added for readibility in this documentation to point out that those words are meant to be executed in a terminal.

## Technical requirements

- A computer with a Python interpreter installed version 3.3 or superior.
  - You can install the latest version of Python with a package manager (Brew or Chocolatey)
- A package manager (brew for MacOS and Linux or Chocolatey for Windows)
  - How to install brew for Mac and Linux: https://brew.sh/
  - Chocolatey for Windows: https://docs.chocolatey.org/en-us/choco/setup
- We need also to have installed Git Bash: https://git-scm.com/downloads
- Conection to Internet for downloading the source code

## Required tools to install with our Package Manager

- Python version 3 (if not already installed in the computer). You can check if you have Python installed by opening a terminal and executing the command `$ python --version` or `$ python3 --version`

  - We can use `$ choco install python` or `$ brew install python`
  - On Windows we should also check that the python command is available on the terminal. It may require some restart of the machine. If after this when checking the installed version the `python` command (or `python3`) is not recognized, we need to execute in a PowerShell terminal opened with Administrator rights this command:

    $ [System.Environment]::SetEnvironmentVariable("PATH", $Env:Path + ";C:\Python312", "Machine")

  In that command we would replace `C:\Python312` with the directory in our hard disk where python was installed. You may need to restart the computer or open a new PowerShell terminal to check if the command is available.

- We need to install the `make` tool for being able to use all the commands defined in the `makefile`. This tool is usually already installed on Mac OS, but we can install it also on Windows with Chocolatey, by using this command:
  `$ choco install make`. In case you use Mac Os and this tool is not available in the terminal, you can install it with `$ brew install make`.

- We need also to install in our computer the tool `graphviz` in order to generate UML diagrams from our code.
  - We can use `$ choco install graphviz` or `$ brew install graphviz`

## Setting up the virtual environment

Once we have installed all the required tools and programs in our PC, we need first to clone the repository by using the terminal provided by Git Bash:

    $ git clone https://github.com/elinaRosato/pig-game_group-6.git

We can alternatively also add the repository by using the Visual Studio Code interface or unzip the file uploaded to Canvas.

The repository and the .zip file include the source code that contains the Python files for executing the game and also other files for testing and executing other functionalities.

At the root folder `pig-game_group-6` open a new terminal and create a virtual environment with this command:

    $ make venv

Once created we need to activate it, so we use this command:

Windows:

     $ . .venv/Scripts/activate     # (Note that there is only 1 space between the 2 dots)

MacOs:

    $ . .venv/bin/activate     # (here there is also 1 space between the 2 dots)

The first thing we will notice after activating the virtual environment will be that the command line will start with a `(.venv)`.

Now we install all the modules specified in the requirements.txt file with the command:

     $ make install

You can see the tools installed by executing afterwards the command

     $ make installed

If you type on the terminal `$ deactivate` then you exit from the virtual environment.

## How to play the game

The class `game.py` is the entrypoint for our game. We need to execute the command in our terminal to start playing:

    $ python .\src\game\game.py        # Or python3

We will first need to introduce our chosen name in the terminal and press Enter, and if we have played before we will also be able to update it by giving first our current name and later a new one.

Next you will be asked if you want to play against the computer or against another player.

If you choose to play against the computer it will ask you for the difficulty level.

After that the turns will start. On each turn each player will have 6 options: roll, hold, cheat, histogram, quit or restart.

When rolling the player needs to also input a number of dices. If any dice turns 1, then all the points accumulated in that round get lost.

If the player decides to hold, then the points for that round will get accumulated.

A cheat option has also been introduced to finish the match early and win automatically.

It is also possible to display a histogram that shows how many times each number of the dice has been rolled.

The first player that reaches 100 wins the game, and its name and punctuation gets saved in the .json file called `highscores.json`

## Rules of the game

The game implemented is called Pig. It is a dice game where there are several variants and we have decided to implement the Hog variant. You can read more about the game and other variants at https://en.wikipedia.org/wiki/Pig_(dice_game)

## How to generate Documentation from docsstrings and UML diagrams

This functionality requires to have executed the command `$ make install` in our virtual environment and installed the Python modules from `requirements.txt`.

In order to generate the documentation, we need to execute in the terminal the command:

    $ make doc

This command will create a `.html` file in the `doc/api` folder for each Python class in `src/game`.

The convention chosen for the docstrings comments in the classes is `pep257`. You can read more about it and find some examples at https://peps.python.org/pep-0257/ . This configuration can be changed in the file `.pylintrc`, but keep in mind that it will require updating the format of the existing comments so they are reflected in the output files.

We can also generate UML diagrams from our classes in `src/game` by running the command:

    $ make uml

After running it 2 new `.png` files called `classes.png` and `packages.png` will be created or overwritten in the folder `doc/uml`.

There will also be created 2 files called classes.dot and packages.dot which are used from the tool `graphviz` to generate the `.png` files

## How to contribute to the project

If you want to contribute to the project and develop new functionalities or maintain existing ones you need first to request for access to this repository owner.

You should adhere to the agreed naming conventions and documentation patterns.

It is also important that any changes in the current implementation or new additions get properly tested with unit tests and the coverage is minimum 90%.

## Good syntax and conventions with lint

We can enforce some coding rules across all the files of our project by using linters. Linters are a type of tools that help identifying inconsistencies in the code by using rules. These rules are added to the files `.flake8` and `.pylintrc`, and you can run the command `$ make lint` to get a list of all the syntax problems in the code that match with those rules.

## Running tests and generating the Test coverage report

This functionality requires to have executed the command `$ make install` in our virtual environment and installed the Python modules from `requirements.txt`.

We can execute in the terminal the command:

    $ make test

The results of the test coverage will get displayed on the terminal only if all the tests execute successfully without errors.

If so, a new folder called `htmlcov` will get created at the root of the project. It will include an `index.html` file, which we can open with our browser and see the coverage percentages per class and the total average.
