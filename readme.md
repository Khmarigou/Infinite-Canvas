# Infinite Canvas

## About

**Infinite canvas** is an infinite canvas _(thanks you captain obvious)_ where you can only draw lines that link edges of the grid.

## Use

You can move by using the right click of your mouse. Juste press the left button to start a line and release when you where you want to finish the line, the lines will automatically be align with the grid.  
You can choose the color of the line on the top by clicking the color wanted.  
The **Switch theme** button change the background with some darker color for using white lines.  
The **Clear** button clear all the canvas. ⚠️ this action is definitive.
The **Background off/on** button tell if the background need to be downloaded with the image. When the button is red the image is a png without any background, when it's green it will keep a white background.  
The **Save** button saves the image in png, only the part with drawings will be downloaded, not all the canvas. *This not work with the python version, see below*  

Have fun !

## Runing 

### Basic

You can use the app by opening the `index.html` in your browser

### Node.JS server

You can run it in a node.js serveur with :
```
node app.js
```
and access at your [localhost](http://localhost:3000)

### Python

Or you can use :
```
python app.py
```
to launch a PyQt window.

You need to install all dependencies with 

```
pip install PyQt5 PyQtWebEngine
```

*With the Python version the download is not yet implemented, button just do nothing*
