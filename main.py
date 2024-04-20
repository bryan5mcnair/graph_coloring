import networkx as nx
import matplotlib.pyplot as plt
import os

def construct_graph():
    # initialize graph
    graph = nx.Graph()

    while True:
        os.system('cls')
        print()
        print("Choose an option between 1 and 5")
        print("Option 1. Add vertex")
        print("Option 2. Add edge")
        print("Option 3. Color vertex")
        print("Option 4. Draw graph")
        print("Option 5. Quit")

        option = input("\nEnter your option: ")

        if option not in [str(num) for num in range(1,6)]:
            print("This option does not exist. Choose a number between 1 and 5.")
            continue
        break

construct_graph()