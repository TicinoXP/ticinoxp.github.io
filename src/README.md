TicinoXP's WebSite
======================


This is the Pelican source code for the static website of TicinoXP.

The compiled HTML is hosted in the repository [http://ticinoxp.github.io](http://ticinoxp.github.io).

## Setup
We recommend working inside a Python3's virtual environment.

You can create and configure a virtualenv with a working Pelican installation using a script provided by this repo itself.

Clone this repo, or one of its forks with:

    git clone git@github.com:TicinoXP/ticinoxp-website.git
    cd ticinoxp-website

Then run:

    source install.sh

This will create a virtualenv called ```venv``` in the repo's root, and install all the packages listed in requirements.txt.

The script will also activate the virtualenv. Don't forget to deactivate it when you are finished, with:

    deactivate

## Build
You can compile the source code with:

    pelican

which will compile the HTML static site in the directory

    ./output
    
It is also possible to compile and self-host the result with

    ./develop_server.sh start
    
which will continuosly watch for file modification, compile the project as needed and serve the result at

    http://localhost:8000
    
Stop the server with:

    ./develop_server.sh stop
    
