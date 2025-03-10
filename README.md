# PythonBatchNovDec2024
A repository with all the classes material for becoming a python developer


## Git Commands

To clone a repository(not needed in codespace, needed for local development):

    git clone <url>

To list the branches:

    git branch

To create a branch:

    git checkout -b class01

To checkout to an existing branch

    git checkout <branch-name>

To see the latest local changes:

    git status

To  check/verify the modified content in existing file:

    git diff 

To stage the changes:

    git add <filename>

To stage all the changes:

    git add *

To commit the changes:

    git commit -m "commit message"

To push the changes:

    git push origin <sourceBranch>

        class01 -> main
        ex: git push origin class01

### Daily

To check the branch is clean,

    git status

To checkout to the main branch

    git checkout main

To get the latest changes

    git pull origin main

To create new branch

    git checkout -b <NEW BRANCH NAME>

## Virtual Environment

    Isolated environment 

    why needed
        - same system, multiple projects
            - different python versions 
            - same python verison, but different module versions

    How to create Virtual Environment 
        - Virtualenv
        - venv
        - pipenv
        - poetry 
        - uv

    Using Virtualenv
        
        Install
            pip install virtualenv
        
        create virtual environment
            python -m virtualenv .venv
        
        activate virtual environment
            linux
                source .venv/bin/activate

            windows
                .venv/script/activate

    Using Poetry
        pip install -U pip
        pip install poetry
        python -m poetry init
        python -m poetry shell

        pip install poetry
        poetry add pandas        

## Course Completed

[class 00](link)

    00. Dev Setup
        Installing IDE/Editor
        Installing Python and local setup
        Github access, creating project

[class 01](link)

        git commands
        markdown syntax
        daily activity and usage

    01. Introduction
        Importance of Python
        Two versions of Python (2.x & 3.x)

[class 02](link)

        PEP 8 Guidelines (https://peps.python.org/pep-0008/)
        Shebang Line
        Indentation issue and best practices
        built-in functions
        print function
        Script mode vs interactive mode
        Jupyter notebook usage
        Ascii and unicode characters

[class 03](link)

        Comment Operator
        Keywords and Identifiers
        Line continuation and statement separator operators

    02.Basics
        Arithmetic operations
            +, -, *, /, //, %
            divmod() function
            compound operations

[class 04](link)

            Practical Problem solving
            Working with complex numbers
            abs() function
            Operator precedence in arithmetic operations

    Assignments:
        1) Savings Bank
        2) Bank loan
            simple interest
            compound interest
        3) convert from hex to oct, vice versa
        4) feet to cms conversion

[class 05](link)

    String operations
        Usage of single, double, and triple quotes
        len() function
        Indexing and Slicing Strings

[class 06](link)

        string attributes

[class 07](link)

        string attributes

[class 08](link)

        String formatting: old & new styles, f-strings
        unicode strings

[class 09](link)

        bytearray() and byte() strings
        Usage of help
        Usage of pydoc
    
    03.Language Components
        Relational Operations
        Logical Operations

[class 10](link)

        Boolean Operations
        Bitwise Operations
        Identity Operations
            Dual Memory management Strategy
        range() function
        Conditional Operations

[class 11](link)

            Structural Pattern Matching
            Loops: for & while, break, continue, pass, sys.exit
        # Assignment: Try these break, continue, pass, on a for loop example

[class 12](link)

            Walrus Operator

        04.Exception Handling
            Exceptions Hierarchy
            Different types of errors, error vs exception and exception groups
            Handling single and multiple exceptions
            raising exceptions
            asserts
            traceback
            exception Groups
            warnings

[class 13](link)

        05.Debugging
            Importance of logical errors
            Debugging with pydevd
            Debugging with pdb, ipdb
            breakpoint() function
            PYTHONBREAKPOINT environment variable usage
            post analyses of executed script

[class 14](link)

        06.Collections
            Lists

[class 15](link)

            Copy Problem - shallow copy vs deepcopy
            Tuples & namedtuples
            Immutability & unpacking
            Sets
                attributes, operations

[class 16](link)

            fronzensets
            Dictionaries
                zip() function
                workaround for switch case
            Comprehensions
            Working with Iterables - sum(), max(), min()

[class 17](link)

        07.Functions
           Functions with & without arguments, keyword arguments
        Functions with Different return types and unpacking
        Functions with with Default arguments
        variadic functions : variable arguments and variable keyword arguments
        Functions with keyword only arguments
        Scoping: Global vs Local
        call by reference
        call by value

[class 18](link)

        Partial Functions
        Anonymous(Lambda) Functions
        Higher order functions: map(), filter(), functool.reduce()
        Recursions and recursions limit

[class 19](link)

            inner functions
            closures

        08.Decorator Design Pattern
            Necessity
            function Decorator
            Practical Examples
            syntactic sugar for decorators
            multiple decorators on same function
            decorators with arguments
            functools - wrap, lru_cache
            class decorator

[class 20](link)

        09.Iterables, Iterators, Generators and co-routines
            Iterables
                different ways of extracting values from iterables
            Iterators
                iter() protocol
                itertools module

[class 21](link)

                Generators
                yield vs return
                function vs Generator
                Generator pipelining
                Generator Expression

[class 22](link)

            Coroutine
            Generator vs Coroutine
            coroutine pipelining

        10.Modules
            Basic Modules
                - math, sys, argparse

[class 23](link)

                os, pathlib, psutil

[class 24](link)

                shutil, subprocess, getpass
            time related
                - time, datetime, pytz, timeit, calendar
            others
                - random, collections, atexit, contextlib, base64

[class 25](link)

            create user-defined module
            creating user-defined package
            packaging
            creating the wheel files, tar files
            publishing with twine
            egg files

        11. File Operations
            flat files

[class 28](link)

        12.Logging
            Simple logging
            Configuring log file
            formatting logs and adding timestamp
            working with file handler and stream handler
            configuring multiple handlers
            color logging
            Rotating logger

[class 33](link)

                profiling
                Objgraph
                doctest

[class 34](link)

                    unittest
                    pytest

                16. AWS Cloud

                    AWS Development setup 
                    AWS CLI setup and usage
                    AWS IAM 
                        creation of Users, Groups, and assiging policies    

[class 35](link)

