import argparse

parser = argparse.ArgumentParser(description='This is a test script to see if I can do something with Docker.')
parser.add_argument("--print_string", help="Prints the supplied argument", default='No string defined.')
parser.add_argument("--param", help="Stores a number in a parameter", default=0, type=int)


print('Hello, is this docker builder?')

import pandas as pd
print('Pandas imported: ',pd.__version__)

import geopandas as gpd
print('Geopandas imported: ',gpd.__version__)

if __name__ == "__main__":
    args = parser.parse_args()
    # Print a string
    if args.print_string != "No string defined.":
        print(args.print_string)

    # Multiple number by 5
    else:
        print("The parameter multiplied by 5 equals: ", args.param*5)