import requests
import re
import os
import sys
import subprocess

path = os.getcwd().split('/')
day = path[-1]
year = path[-2]

print(f"Year = {year}")
print(f"Day = {day}")

level = sys.argv[1] if len(sys.argv) == 2 else '1'
print(f"Level = {level}")

code_file = f'solve{level}.py'
print(f"File = {code_file}")

# execute specified solution, use last input provided as answer
answer = subprocess.check_output(['python3', code_file]).decode().strip().split('\n')[-1]
print(answer)

session = os.environ.get('ADVENT_SESSION', None)
if session is None:
    print("ADVENT SESSION IS NOT SPECIFIED")
    session = input("Input Session Token: ")

cookies = {
    'session': session,
}

headers = {
    'authority': 'adventofcode.com',
}
data = {
    'level': level,
    'answer': answer,
}

url = f'https://adventofcode.com/{year}/day/{day}/answer'
print(url)

response = requests.post(url, cookies=cookies, headers=headers, data=data)
body = re.search(r'<main>(.*?)<\/main>', response.text, re.VERBOSE | re.DOTALL).group(1)

print(body)