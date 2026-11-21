from PIL import Image # pip install pillow 
import pathlib
import os
import argparse


def main():
    print("Hello CS457!")
    
    # Argument Parser test setup
    parser = argparse.ArgumentParser(description ='Image metadata remover tools')
    parser.add_argument("--date", action="store_true", help="Remove date and time.")
    args = parser.parse_args()
    print(str(args))



if __name__ == "__main__":
    main()