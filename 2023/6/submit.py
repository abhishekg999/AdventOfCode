import requests
import re
import os
import sys
import subprocess

to_submit = sys.argv[1] if len(sys.argv) == 2 else '1'
code_file = f'solve{to_submit}.py'

path = os.getcwd().split('/')
day = path[-1]
year = path[-2]

print(f"Sending solution {code_file} for day {day}, {year}!")

answer = subprocess.check_output(['python3', code_file]).decode().strip().split('\n')[-1]
print(answer)

cookies = {
    'session': '53616c7465645f5ff19ebb235aeb1c3d91a844d1eda687ba5ffe6faf06694c6ceec6cb028778422960414f8b5fffaf1de95930b4b9057adc0448a8e9f48b6b19',
}
headers = {
    'authority': 'adventofcode.com',
}
data = {
    'level': to_submit,
    'answer': answer,
}

url = f'https://adventofcode.com/{year}/day/{day}/answer'
print(url)
response = requests.post(url, cookies=cookies, headers=headers, data=data)
body = re.search(r'<main>(.*?)<\/main>', response.text, re.VERBOSE | re.DOTALL).group(1)

print(body)