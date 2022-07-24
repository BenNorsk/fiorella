#!/bin/bash
echo "Installing fiorella..."
brew install brainfuck
curl "https://raw.githubusercontent.com/BenNorsk/fiorella/main/fiorella.py" --output fiorella.py
mv fiorella.py ~/Documents/fiorella/fiorella.py
echo "alias fiorella = 'python  ~/Documents/fiorella/fiorella.py'" >> ~/.zshsrc
echo "Installation complete."
echo "Restart the terminal, and then use 'fiorella' to run the language." 
