import argparse
from lps.myfile import longest_palindromic_substring

parser = argparse.ArgumentParser()
parser.add_argument("--input", help = "Returns the longest palindromic substring for the given the input string", type=str)
args = parser.parse_args()

if args.input:
    print("Longest palindromic substring is : ", longest_palindromic_substring(args.input))
else:
    print("----No input received----\nTry using:\npython main.py --input <INPUT_STRING>\npython3 main.py --input <INPUT_STRING>")



