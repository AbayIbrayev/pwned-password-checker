import hashlib
import sys
from typing import List

import requests


def request_api_data(query_char: str) -> requests.Response:
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    res = requests.get(url, timeout=10)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the API and try again.')
    return res


def get_password_leaks_count(hashes: requests.Response, hash_to_check: str) -> int:
    hashes = (line.split(':') for line in hashes.text.splitlines())
    return next((int(count) for h, count in hashes if h == hash_to_check), 0)


def pwned_api_check(password: str) -> int:
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args: List[str]) -> str:
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f'Oops... Your ({password}) password was found {count} times.')
        else:
            print(
                f'Your {password} password was NOT found. Carry on! For now >:)')
    return 'Done!'


if __name__ == '__main__':
    if sys.argv[1:]:
        sys.exit(main(sys.argv[1:]))
    print('Please enter a password to check.\nUsage: python script.py <password> <password> ...')
    sys.exit(1)
