#!/usr/bin/env python3
import hashlib
import requests
import argparse

parser = argparse.ArgumentParser(description='The password vulnerability checker 1.0')

parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

parser.add_argument('password', type=str, help="The password to check")

args = parser.parse_args()

sha1hash = hashlib.sha1()

sha1hash.update(args.password.encode('utf-8'))

sha1digest = sha1hash.hexdigest().upper()

first_5_of_hash = sha1digest[:5]

print("Checking haveibeenpwned.com...\n")

result = requests.get('https://api.pwnedpasswords.com/range/'+first_5_of_hash)

password_found = False

if(result.status_code == 200):
  list_of_passwords = result.text.split('\n')

  for password in list_of_passwords:
    password_hash_suffix, number_of_times = password.split(':')
    number_of_times = number_of_times.strip()

    full_password_hash = first_5_of_hash + password_hash_suffix

    if(sha1digest == full_password_hash):
      print(f'Password {args.password} found {number_of_times} times!')
      password_found = True
      
  if(not password_found):
    print("The password wasn't found in the list of pwned passwords!")