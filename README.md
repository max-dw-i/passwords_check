## Is my password leaked?
There are many databases containing leaked passwords. They help to brute your password easier. Recently the 320 million passwords (SHA1-hashes actually) leaked database has been published [here](https://haveibeenpwned.com/Passwords). So you can download it from there and use *passwords_check.py* to check if your passwords are in it.

## Installation
You need Python 3.x installed.

To install:
- Download *passwords_check.py* in some directory or
- Clone the whole repository.

## How to use
1. Create a txt file and type the passwords you want to check in it one on a line. The txt file mustn't have a blank line at the end;
2. Type in the command line:

```
  # Go to the directory where passwords_check.py is (for example)
  cd /D C:\passwords_check

  # C:\my_passes.txt - the path to the txt containing your passwords
  # C:\leaked1.txt - the path to the txt containing the leaked passwords hashes
  python passwords_check.py C:\my_passes.txt C:\leaked1.txt
```

## Licensing
MIT