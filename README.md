# Pwned Password Checker

This script checks if a given password has been compromised using the "Have I Been Pwned" API. Pwned Passwords are hundreds of millions of real world passwords previously exposed in data breaches. This exposure makes them unsuitable for ongoing use as they're at much greater risk of being used to take over other accounts.

## Features

- Check if a password has been compromised
- Uses the k-Anonymity model for privacy

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

  ```sh
  git clone https://github.com/yourusername/pwned-password-checker.git
  ```

2. Navigate to the project directory:

  ```sh
  cd pwned-password-checker
  ```

3. Install the required dependencies:

  ```sh
  pip install requests
  ```

## Usage

Run the script with the password you want to check:

```sh
python script.py yourpassword
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Have I Been Pwned](https://haveibeenpwned.com) for the API
