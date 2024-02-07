# Triton NeuroTech BCI P300 Magician

This project uses Wearable Sensing's DSI 7 and P300 signals to classify which playing card you choose.

The card game works like this: _____

Required software:

HOW TO NAVIGATE THIS REPO:

- Data Collection
    - DSI_to_Python.py = reads DSI Streamer TCP/IP output into a sequence of integers & floats
    - Training Data
        - all files of recorded Data
        
- Models
    - cnn2a.py = neural net initialization and training code
    - oz-speller.py = main(), runs everything. Puts live data into CNN and outputs which card was chosen
    - welcome.md = a fun surprise

- GUI
    - GUI outline
    - code for P300 matrix/paradigm
    - code for neural net input into UI output/screen