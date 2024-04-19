# AMSIBye

Tool to automatically obfuscate (malicious) powershell scripts.
This tool aims to bypass AMSI/Windows Defender by transforming variables and functions.

Instead of randomly assigning values to variables this script takes from a dictionary file to make it seems like a regular file.
Some more obfuscation techniques inlude:
* Random capatalisation
* Transforming string to array and reading from left to right
* Chopping up strings and pasting them back together
* Placing random comments to further differantiate the final script
* Transforming IP addresses to hex

Great inspiration taken from https://github.com/tokyoneon/Chimera

## How to use

Firstly, install the required python packages by install with pip

``` bash
pip3 install -r requirements.txt
```

Run the program, file should be the last command option.

```bash
python .\main.py --help
Usage: main.py [OPTIONS] INPUTFILE

Options:
  --all              Obfuscate using all the parameters
  --changevariables  Change variable names to random words from a dictionary.
                     Dictionary words tend to not be suspicious
  --caps             Randomly capatalise variable/function names
  --left2right       Reverses strings to an array and read in reverse        
  --iphex            Transform potential IP addresses in the code to
                     hexaddresses
  --comments         Place random comments in the code to differantiate the  
                     final hash even more
  --oneliner         Convert the powershell into a oneliner. This will not add
                     any comments to fill the script Note:Only advisable on
                     smaller codebases
  --output FILENAME  Custom output filename, default will be
                     Obfuscated_inputfilename_datetime.ps1
  --help             Show this message and exit.
```

This program has been written and tested in python 3.12
