import os
import sys


# ----------- This code is to translat BF to Fiorella -------

def translate_to_fiorella(bf_code):
    fio_code = ""
    translation = {
        ">": "fiorella",
        "<": "benjamin",
        "-": "bruckner",
        "+": "fiestas",
        ".": "peru",
        ",": "koala",
        "[": "rimini",
        "]": "amo"
    }
    for word in bf_code:
        if word != "":
            fio_word = translation[word]
            #print(fio_word)
            fio_code += fio_word + " "
    return fio_code

def create_fiorella_file(filename):
    with open(filename, 'r') as file:
        bf_code = file.read().replace('\n', '').replace(" ", "")
    bfcode_statements = list(bf_code)
    fio_code = translate_to_fiorella(bfcode_statements)
    fio_file_name = filename.replace(".bf", ".fiorella")
    os.system(f'touch {fio_file_name}')
    f = open(fio_file_name, "a")
    f.write(fio_code)
    f.close()


# --------------- Here is the Fiorella Code -----------


def translate_to_bf(fio_code):
    bf_code = ""
    translation = {
        "fiorella": ">",
        "benjamin": "<",
        "bruckner": "-",
        "fiestas": "+",
        "peru": ".",
        "koala": ",",
        "rimini": "[",
        "amo": "]"
    }
    for word in fio_code:
        if word != "":
            try: # if the word is not in the translation dictionary, it will throw an error
                bf_word = translation[word]
                bf_code += bf_word
            except KeyError:
                print(word + "' is not a valid keyword in fiorella.")
                return()
    return bf_code




def create_and_execute_brainfuck_file(filename):
    with open(filename, 'r') as file:
        fio_code = file.read().replace('\n', ' ')
    fiocode_statements = fio_code.split(" ")
    bf_code = translate_to_bf(fiocode_statements)
    os.system("touch temp_fio.bf")
    f = open("temp_fio.bf", "a")
    f.write(bf_code)
    f.close()
    os.system("brainfuck temp_fio.bf")
    os.system("rm temp_fio.bf")

    
def main():
    try:
        arg = sys.argv[1]
    except IndexError:
        print("use fiorella -h to display your options.")
        return()

    if arg == "h" or arg == "-h":
        print("Write 'fiorella program_name.fiorella' to run your program.")
        print("Else, write -h for help.")
        print("Else, write -co to see all commands needed to write fiorella.")
        print("Else, write -c filename.bf to convert a .bf file into a .fiorella file")
        print("Else, write -v to see the current version of fiorella.")
    elif arg == "v" or arg == "-v":
        print("fiorella, version 1.0.0")
    elif ".fiorella" in arg.lower():
        create_and_execute_brainfuck_file(arg)
    elif arg == "c" or arg == "-c":
        try:
            file = sys.argv[2]
            if ".bf" in file:
                create_fiorella_file(file)
            else:
                print("You can only convert .bf files into .fiorella files.")
        except IndexError:
            print("Use 'fiorella -c filename.bf' to convert a bf file into a fiorella file.")
    elif arg == "co" or arg == "-co":
        print("In order to write fiorella, use the following commands:")
        print("fiorella:    Increase pointer.")
        print("benjamin:    Decrease pointer.")
        print("fiestas:     Inrease element under the pointer.")
        print("bruckner:    Decrease element under the pointer.")
        print("rimini:      Start a loop.")
        print("amo:         End the loop.")
        print("peru:        Print ASCII code of element.")
        print("koala:       Read character and store it.")
    else:
        print("No valid arguments.")
        print("Type 'fiorella -h' to see all commands.")

main()

"""
1. fiorella     >
2. benjamin     <
3. fiestas     +
4. bruckner      -
5. peru         .
6. koala        ,
7. rimini       [
8. amo          ]
"""
