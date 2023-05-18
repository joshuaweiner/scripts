#!/usr/bin/env python

"""
Extract Emails From Text

This script extracts email addresses from a given text. It uses regular expressions to identify valid email patterns
and returns a list of extracted emails.

Usage:
    $ python extract_emails.py -t "text to be analyzed"

Example:
    $ python extract_emails.py -t "email1@domain.com sent a message to email3@domain.com"

    Output:
    email1@domain.com
    email3@domain.com

"""

import sys
import re
import argparse


def extract_emails(text):
    """
    Extracts email addresses from the given text.

    Args:
        text (str): Text to search for email addresses.

    Returns:
        list: List of extracted email addresses.
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails


def main():
    """
    Main function that demonstrates the usage of extracting emails from a text.
    """
    parser = argparse.ArgumentParser(description='Extract emails from text')
    parser.add_argument('-t', '--text', required=True, help='Text to be analyzed')
    args = parser.parse_args()

    text =  args.text
    emails = extract_emails(text)

    for email in emails:
        print(email)

    return 0


if __name__ == '__main__':
    retval = main()
    sys.exit(retval)
