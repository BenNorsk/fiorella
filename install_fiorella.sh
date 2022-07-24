#!/bin/bash
echo "Installing fiorella..."
brew install brainfuck
wget "https://raw.githubusercontent.com/BenNorsk/fiorella/273aa1fbe01768c6cd99438a70a369ddacb0a315/fiorella.py"
mv fiorella.py ~/Documents/fiorella.py
echo "alias fiorella = 'python  ~/Documents/fiorella/fiorella.py'" >> ~/.zshsrc
echo "Installation complete."
echo "Restart the terminal, and then use 'fiorella' to run the language." 
