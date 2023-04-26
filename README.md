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

## In-Production Usage Guides

To use this script safely and effectively in production, follow these best practices:

- Use the script only with permission from the email account owner.
- Ensure that the password list is created using ethical and legal methods, such as through password cracking contests.
- Use a stop list to exclude passwords that have already been tried or that are known to be ineffective.
- Limit the number of login attempts per session to avoid account suspension or blacklisting.
- Monitor the SMTP logs to detect unusual login attempts.

If you encounter issues while running the script, consult the following troubleshooting tips:

- Ensure that you have the correct login credentials and permission to access the target account.
- Check that the password list is in the correct format and that it contains viable passwords.
- Enable two-factor authentication on the target account to make it more difficult to hack.
- If the script continues to fail, consider trying a different password cracking tool or approach.

## Real-World Use Cases

This script can be used in ethical hacking engagements, password cracking contests, and forensic investigations. It can be used to demonstrate the weaknesses of email security and to educate users on the importance of creating strong passwords.

## References

The script was built using the `smtplib` library, which is part of the Python Standard Library. Additional resources used in the development of this script include:

- [Python documentation](https://docs.python.org/)
- [smtplib documentation](https://docs.python.org/3/library/smtplib.html)
- [How to Brute Force SMTP](https://www.cybrary.it/0p3n/brute-force-smtp/)
- [SMTP Authentication Error Codes](https://github.com/awick/smtplib/blob/master/smtplib.py#L742)