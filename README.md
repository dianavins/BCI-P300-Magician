# Triton NeuroTech BCI P300 Magician

This project uses Wearable Sensing's DSI 7 and P300 signals to classify which playing card you choose.

The card game works like this: _____

Required software:

HOW TO NAVIGATE THIS REPO:

- Data Collection
    - DSI_to_Python.py = TCP/IP --> signal_log --> model --> outputs by time interval
    - Training Data
        - all files of recorded Data that has been turned into signal logs
        - function that turns recordings into signal_log?
        
- Models
    - cnn2a.py = neural net initialization and training code
    - P300-CNNT.py = other neural net example, doesn't include editing training and testing data
    - welcome.md = a fun surprise

- GUI
    - GUI outline
    - code for P300 matrix/paradigm
    - code for neural net input into UI output/screen