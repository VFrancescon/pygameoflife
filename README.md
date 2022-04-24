# Pygame of Life
[Pygame](https://www.pygame.org/news) based Game of Life implementation, featuring [Sphinx](https://www.sphinx-doc.org/en/master/) documentation.

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

Additionally, the following parameters can be affected from the command line, as follows

```
python3 src/main.py [GridN] [GridM] [GridSize] [WaitTime]
```

Where: 

* GridN and GridM determine the dimensions of the Grid.

* GridSize determines the dimension of each individual cell.

* WaitTime determines the idle time in auto-mode between operations, if any. 

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

# File Structure

| **File**                  | **Functionality**                                                                                                                         |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| csv_outs/AxBfilename.csv  | Output files generated from the program. A and B are x and y size of the grid. Filename describes the feature shown in the file           |
| docs/                     | Documentation Folder                                                                                                                      |
| docs/*.rst                | [reStructuredText](https://docutils.sourceforge.io/rst.html) source files. Compiled into documentation.                                   |
| docs/conf.py              | [Sphinx](https://www.sphinx-doc.org/en/master/) configuration file.                                                                       |
| docs/make.bat \| Makefile | Sphinx makefiles.                                                                                                                         |
| images                    | Demonstrative images.                                                                                                                     |
| src/GOL.py                | Game of Life Python Module. Serves as the back-end to the project. Handles current and future states of the board as well as CSV parsing. |
| src/grid.py               | Front-end Module. Wraps the back-end functionality in a [pygame](https://www.pygame.org/news).                                            |
| src/main.py               | Driver code. Handles user inputs and passes them to the Front-end wrapper.                                                                |
| .gitignore                | List of files/directories not to upload to git.                                                                                           |
| README.md                 | Markdown format info file.                                                                                                                |
| requirements.txt          | List of requirements for the program. See the Usage section for instructions on how to use it.                                            |

# Build Environment

* OS: Ubuntu 20.04
* Python3 ver: 3.8.10
* [Pygame](https://pypi.org/project/pygame/) ver: 2.1.2
* [EasyGUI](https://pypi.org/project/easygui/) ver: 0.98.3

# Credits

Author: Vittorio Francescon for the University of Leeds