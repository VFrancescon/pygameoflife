# Pygame of Life
Pygame based Game of Life implementation, featuring [Sphinx](https://www.sphinx-doc.org/en/master/) documentation.

# Build Instructions

## Install Dependencies
```
python3 get-pip.py # install pip for python3
pip3 install -r requirements.txt # install all dependencies 
```

## Build Documentation
Documentation can be built as follows:

```
cd docs/
make html
```

Next, the documentation can be accessed as follows (assumes cd is docs/)

```
<\htmlviewer> _build/html/index.html
```

Where <\htmlviewer> is whatever browser or program the user may prefer.

If you are receiving this software as a zipped archive, a pre-built copy of the documentation will be included.

Note that the requirements.txt file also clears documentation related dependencies.


# Usage

Once all the dependencies are cleared, the program can be simply run from the command line:

```
python3 src/main.py
```

Additionally, the grid size may be specified in the command line:

```
python3 src/main.py 15 20
```
Where the above will generate a 15x20 Grid

## Keybindings

At runtime, the following can be used to control the program.

| Key         | Functionality          |
|-------------|------------------------|
| b           | Toggle Autorun         |
| h           | Open Manual Prompt     |
| o           | Open a CSV File        |
| r           | Reset the Board        |
| s           | Save the current Board |
| Esc         | Quit the Program       |
| Left Click  | Populate Selected Cell |
| Right Click | Delete Selected Cell   |

Note: saved boards will be output as CSVs in the csv_outs/ directory.

# Build Environment

* OS: Ubuntu 20.04
* Python3 ver: 3.8.10
* [Pygame](https://pypi.org/project/pygame/) ver: 2.1.2
* [EasyGUI](https://pypi.org/project/easygui/) ver: 0.98.3

# Credits

Author: Vittorio Francescon for the University of Leeds