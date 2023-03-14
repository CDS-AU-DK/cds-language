"""
An example script using argparse for command line arguments
"""

#!/usr/bin/python
import argparse

def main():
    # Argument parser
    ap = argparse.ArgumentParser()
    
    # Command line interface arguments
    ap.add_argument("-n", "--name", default="World", help="Name we want to print")   
    ap.add_argument("-v", "--value", required=True, type=bool, help="Boolean value")   
    
    # Parse arguments
    args = vars(ap.parse_args())
    
    # Create 'name' variable
    name = args["name"]
    # Create value variable
    value = args["value"]
    
    # print
    if value==True:
        print(f"Hello, {name}!")
    else:
        pass

if __name__=="__main__":
    # execute
    main()