# Fiorella Code

Hello everyone, welcome to Fiorella Code, the fiorella programming language!

## Install Fiorella Code MacOS
Fiorella Code is currently only available for MacOS. In order to install Fiorella Code on MacOS, you need to have as well ```homebrew``` and ```python ≥ 3.9``` installed.

### Install Homebrew
In order to install ```homebrew```, run the following command:
 ```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
 ```

### Install Python
In order to install ```python ≥ 3.9```, run the following command:
 ```
 brew install python
 ```
Lower versions of ```python``` might work, but they are not supported. 

### Install Fiorella Code
Now you are ready to install ```Fiorella Code```, by running the following command:
 ```
 curl "https://raw.githubusercontent.com/BenNorsk/fiorella/main/install_fiorella.sh" --output install_fiorella.sh
 chmod 777 install_fiorella.sh
 ./install_fiorella.sh
 rm install_fiorella.sh
 ```
 Once, you have it installed, use the command  ```fiorella```  to run it. For further instructions on how to use and write the fiorella language, use ```fiorella -h```.
 
 # Documentation
 Fiorella Code follows the logical model of a Turing machine. Each program starts with an "infinte" tape of individual elements (bytes). The pointer, at the beginning of the program, is pointed at the first element. You may then manipulate the value of the element (byte) or move the pointer to the left or right. Additionally, you may create loops, in the same manner as its sister language [https://gist.github.com/roachhd/dce54bec8ba55fb17d3a](Brainfuck). Finally, you may also print or read values from the terminal.
 
 In order to write fiorella, you may use the following commands:
 
 ```fiorella```    Increase pointer.
 
 ```benjamin```    Decrease pointer.
 
 ```fiestas```     Inrease the element under the pointer.
 
 ```bruckner```    Decrease the element under the pointer.
 
 ```rimini```      Start a loop.
 
 ```amo```         End the loop.
 
 ```peru```        Print the ASCII character of the element under the pointer.
 
 ```koala```       Read the character and store it.
 

 
 # Tutorial Hello World
 
 If you are not yet so fluent in fiorella, here is some example code to write a program that prints out "Hello World!". First, create a file called "helloworld.fiorella". This can be done using the following command:
 
```
 touch helloworld.fiorella
```

Then, open the file with a text editor and copy-paste the following fiorella-code into the file:

```
fiestas fiestas fiestas fiestas fiestas fiestas fiestas fiestas fiestas fiestas rimini fiorella fiestas fiestas fiestas fiestas fiestas fiestas fiestas fiorella fiestas fiestas fiestas fiestas fiestas fiestas fiestas fiestas fiestas fiestas fiorella fiestas fiestas fiestas fiorella fiestas benjamin benjamin benjamin benjamin bruckner amo fiorella fiestas fiestas peru fiorella fiestas peru fiestas fiestas fiestas fiestas fiestas fiestas fiestas peru peru fiestas fiestas fiestas peru fiorella fiestas fiestas peru benjamin benjamin fiestas fiestas fiestas fiestas fiestas fiestas fiestas fiestas fiestas fiestas fiestas fiestas fiestas fiestas fiestas peru fiorella peru fiestas fiestas fiestas peru bruckner bruckner bruckner bruckner bruckner bruckner peru bruckner bruckner bruckner bruckner bruckner bruckner bruckner bruckner peru fiorella fiestas peru fiorella peru
```
You are nearly done! Now run the file by using the following command:

```
fiorella helloworld.fiorella
```
