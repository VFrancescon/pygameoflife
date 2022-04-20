=============
Usage
=============

.. note::

  Assuming all Dependencies have been cleared, the program can be simply run from the command line

.. code-block::
  
    python3 src/main.py

Additionally, the grid size can be manually set as follows:

.. code-block::

    python3 src/main.py 20 20

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
Limitations and Issues
-----------------------

The following issues exist at the time of writing:

1. While the window can work at any aspect ratio and Grid Size, the window size is calculated at run-time.
Therefore, there will be distortions if the program changes to a different Grid Size. Though Functionality is unaltered.