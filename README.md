# FastHub TTS Python Module

This Python module provides a convenient interface for interacting with FastHub.net's Text-to-Speech (TTS) service.

## Installation

To install the FastHub TTS Python module, use the following pip command:

```bash
pip install FastHub
```
## Usage
Shouldn't be an issue, use one of the two functions:

```python
PlayTTS()
```
```python
TTStoMP3()
```
There are default parameters, but you can supply your own, the easiest being the *Text* property.

```python
PlayTTS("Hello, World!")
```

These parameters are the same throught the functions, but the ```TTStoMP3()``` function has one additional parameter, *filename* which just tells the program where to save your file/what to call it.  It will automatically add *.mp3* to the end of the name.

The rest are pretty much self explanitory.
