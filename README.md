# Digital-Clock-with-python(Tkinter)-APPARKY

> In this article we have designed a Digital Clock in [`Python`](https://www.python.org/) using [`Tkinter`](https://docs.python.org/3/library/tkinter.html)
> 
> To know more about [`Python Programming`](https://www.python.org/) Click [Here](https://www.python.org/)
>
> 
## Code Guide

> The code starts by importing the necessary modules.
> The first module is the `tkinter library`, which provides basic functionality for creating `graphical user interfaces (GUIs)`.
> Next, the `strftime function` is imported to retrieve system time.
> Next, a window is created and given a title of “Clock.”
> A function called `time()` is then created to display the current time on the `label` widget.
> This function uses the `strftime()` function to format the time string according to system conventions.
> The last part of this code sets up styling for the label widget so that it will look nicer.
> Finally, an instance of Label is created and placed at the center of the window.
> The code creates a window and assigns it the title “Clock”.
> The `time()` function is then called to display the current time on the label widget.
> The `lbl.config()` function is used to set the text of the label widget.
> The `after()` function is used to delay displaying the time for 1000 milliseconds.
> Finally, the style of the label widget is modified with `lbl.pack()`.
> 
> 
> We also attach the `exe` Version of it with this project repo.
> 
You can also convert this program in to exe file. You just neet to install [`Babel`](https://babel.pocoo.org/en/latest/) for that

To install `Babel` follow the given command billow
```commandline
pip install Babel
```

And also follow the given code to all your project files like this
```commandline
from babel.numbers import *
from babel.dates import *
```
`Babel` is used to fix images in `exe` version of your code.

You also need [`Pyinstaller`](https://pyinstaller.org/en/stable/). This library converts the `.py` scripts to `exe`.

To install `Pyinstaller` follow the given command billow.
```commandline
pip install pyinstaller
```

You are all set to go. Open your native terminal and run the following command to convert your `.py` script into `exe` file.
```commandline
pyinstaller --onefile -w --hiddenimport=babel.numbers filename.py   
# in this project the filename.py is PythonClock.py
```



-------------------
> 
> To get more interesting projects follow you GitHub page at [Here](https://github.com/Apparky)
> 
> To get more interesting projects follow you Bitbucket page at [Here](https://bitbucket.org/apparky-web/workspace/overview)
> 
> To know more about [APPARKY](https://apparky-soumenmtec-gmailcom.vercel.app/) Click [Here](https://apparky-soumenmtec-gmailcom.vercel.app/)

