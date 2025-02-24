import pandas as pd
import numpy as np


def main():

    count = 0

    with open("CC7genome.fna", "r") as file:
        with open("CC7genome_chopped.fna", "w") as file2:
            for line in file:
                cleanLine = line.strip()
                if ">" not in cleanLine:
                    print(">" + "read_" + str(count), file=file2)
                    print(cleanLine, file=file2)
                    count+=1

main()