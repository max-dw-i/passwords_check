"""This module checks whether passwords from a txt file are in the database of the
leaked passwords.

Arguments:
the first one -- the path to a txt file containing passwords. Each password must be
on a separate line. The file mustn't have a blank line in the end.
the other ones -- the paths to txt files (leaked passwords databases) containing SHA-1
hashes in assending order. The txt files mustn't have a blank line in the end.

Examples:
python passwords_check.py my_passes.txt leaked_passwords.txt
python passwords_check.py c:\my_passes.txt c:\leaked1.txt d:\leaked2.txt leaked3.txt
"""

import sys
import os
from hashlib import sha1
from bisect import bisect_left

class TxtDatabase():
    """Allow to iterate through a txt file as if it was a list of passwords (or hashes).

    Args:
    file_pointer -- an object pointing on a txt file.
    record_size -- the length of a record. Default value is 40 (SHA1-hash length).
    """
    def __init__(self, file_pointer, record_size=40):
        self.file_pointer = file_pointer
        self.file_pointer.seek(0, 2)
        self.record_size = record_size
        self.record_full_size = len(os.linesep) + record_size
        self.record_number = self.file_pointer.tell() // (self.record_full_size) + 1

    def __len__(self):
        return self.record_number

    def __getitem__(self, position):
        self.file_pointer.seek(position * self.record_full_size)
        return self.file_pointer.read(self.record_size).lower()

def password_search(password, passwords_list):
    """Checks if the password (hash) is in the passwords_list."""
    # Use bisect_left from the standard bisect module
    position = bisect_left(passwords_list, password)
    if position != len(passwords_list) and password == passwords_list[position]:
        return True
    return False

if __name__ == '__main__':
    # Read arguments
    PASSWORD_CHECK_TXT = sys.argv[1]
    PASSWORD_DBS = []
    for i in range(1, len(sys.argv)):
        PASSWORD_DBS.append(sys.argv[i])

    # Read passwords to check from a text file
    PASSWORD_CHECK_LIST = []
    with open(PASSWORD_CHECK_TXT, 'r') as passw_check:
        for passw in passw_check:
            # A password's SHA1-hash
            password_sha1 = sha1(passw.rstrip().encode()).hexdigest()
            # Form a list of tuples (password, its SHA-1 hash)
            PASSWORD_CHECK_LIST.append((passw.rstrip(), password_sha1))

    # Check if the passwords in the databases
    for dbase in PASSWORD_DBS:
        with open(dbase, 'r') as file:
            db = TxtDatabase(file)
            for passw in PASSWORD_CHECK_LIST:
                if password_search(passw[1], db):
                    print(passw[0] + ' is leaked.')

    print('Done.')
