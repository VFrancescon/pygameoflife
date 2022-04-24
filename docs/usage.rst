=============
Usage
=============

.. note::

  The following assumes dependencies have been cleared.
   
The program can be simply run from the command line

.. code-block::
  
    python3 src/main.py



.. tip::

  Additionally, the grid size can be manually set as follows:

  .. code-block::

      python3 src/main.py [GridN] [GridM] [GridSize] [WaitTime]


  Where: 

  * GridN and GridM determine the dimensions of the Grid.
  
  * GridSize determines the dimension of each individual cell.
  
  * WaitTime determines the idle time in auto-mode between operations, if any. 


-----------
Keybindings
-----------

The following Keybindings are avaialble at run time:

.. list-table:: 
    :widths: 20 50
    :header-rows: 1

    * - Key
      - Functionality
    * - b
      - Toggle Autorun
    * - h
      - Open Manual Prompt
    * - o
      - Open a CSV File
    * - r 
      - Reset the Board
    * - s
      - Save the current Board
    * - Esc
      - Quit the Program
    * - Left Click
      - Populate Selected Cell
    * - Right Click
      - Delete Selected Cell


-----------------------
File Structure
-----------------------

+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| **File**                 | **Functionality**                                                                                                                         |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| csv_outs/AxBfilename.csv | Output files generated from the program. A and B are x and y size of the grid. Filename describes the feature shown in the file           |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| docs/                    | Documentation Folder                                                                                                                      |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| docs/\ * \.rst           | reStructuredText source files. Compiled into documentation.                                                                               |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| docs/conf.py             | Sphinx configuration file.                                                                                                                |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| docs/make.bat | Makefile | Sphinx makefiles.                                                                                                                         |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| images                   | Demonstrative images.                                                                                                                     |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| src/GOL.py               | Game of Life Python Module. Serves as the back-end to the project. Handles current and future states of the board as well as CSV parsing. |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| src/grid.py              | Front-end Module. Wraps the back-end functionality in a pygame.                                                                           |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| src/main.py              | Driver code. Handles user inputs and passes them to the Front-end wrapper.                                                                |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| .gitignore               | List of files/directories not to upload to git.                                                                                           |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| README.md                | Markdown format info file.                                                                                                                |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| requirements.txt         | List of requirements for the program. See the Usage section for instructions on how to use it.                                            |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+

-----------------------
Limitations and Issues
-----------------------

The following issues exist at the time of writing:

1. While the window can work at any aspect ratio and Grid Size, the window size is calculated at run-time.
Therefore, there will be distortions if the program changes to a different Grid Size. Though Functionality is unaltered.

2. To set a certain parameter from the command line, all previous ones must also be set. 
The values have thus been organised such that the most common ones are first.