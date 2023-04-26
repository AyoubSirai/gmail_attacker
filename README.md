# Email Brute Force Attack Script
![screenshot from 2018-01-12 20 47 45](https://user-images.githubusercontent.com/28595515/34894595-f5ce60b6-f7d9-11e7-8ac1-5eb0180745e3.png)
## Introduction and Purpose

This script is designed to perform a brute force attack on an email account using a list of passwords. The script utilizes Python's `smtplib` library to attempt to log into an email account with a list of provided passwords.

## Prerequisites and Installation Instructions

The following prerequisites are needed to run the script:

- Python version 2.0 or higher
- An active internet connection
- A list of password guesses in a text file

To install and run the script, follow these steps:

1. Download the script to your local machine
   `git clone https://github.com/ayoubsiray/gmail_attacker.git`
2. Install the required `smtplib` library: `pip install secure-smtplib`
3. Open a terminal or command prompt and navigate to the directory where the script is located.
4. Type the following command: `python email_brute_force.py`
5. Follow the prompts to enter the necessary information to run the script.

## Getting Started

To use the script, follow these steps:

1. Launch the script by executing the command `python email_brute_force.py`
2. Choose option 1 to start the brute force attack.
3. Enter the full path of the file containing password guesses.
4. Enter the email address of the target account.
5. The script will attempt to log in to the account using each password in the file until it succeeds or the list is exhausted.

## Architecture and Design

This script is built using Python and utilizes the `smtplib` library to connect to the SMTP server of the email provider. The script reads in a list of passwords from the user and then attempts to log in with each password in the list.
