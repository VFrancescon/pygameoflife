================
Main Driver Code
================

------------------
Key input handling
------------------

Pygame comes with general event handling, which can be used to discern key presses and clicks.

.. code-block:: python
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: #a key has been pressed
            if event.key == pygame.K_n: #then the key 'n' has been pressed
        if event.type == pygame.MOUSEBUTTONDOWN: #mouse has been clicked

-------------------
Flags and Operation
-------------------

The following flags are used to govern operation within the driver code:

.. list-table:: 
    :widths: 20 50
    :header-rows: 1

    * - Flag
      - Functionality
    * - running
      - Main loop is operational
    * - autoRun
      - Toggles automatic state advance