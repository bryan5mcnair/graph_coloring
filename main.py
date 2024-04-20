import networkx as nx
import matplotlib.pyplot as plt
import os

def get_vertices(adj_list):
    return list(adj_list.keys())

def construct_graph():
    graph = nx.Graph()
    vertices = dict()

    optionExists = True

    while True:
        os.system('cls')
        if not optionExists:
            print(f"The option you chose does not exist. Choose a number between 1 and 5.\n")
        else:
            print("Choose an option between 1 and 5.\n")
        print("Option 1. Add vertex")
        print("Option 2. Add edge")
        print("Option 3. Color vertex")
        print("Option 4. Draw graph")
        print("Option 5. Quit")

        if get_vertices(vertices) != []:
            print(f"\nCurrently, you have the vertices {', '.join(get_vertices(vertices))}")

        option = input("\nEnter your option: ")

        if option not in [str(num) for num in range(1,6)]:
            optionExists = False
            continue
        optionExists = True
        
        option = int(option)
        if option == 1:
            while True:
                v = input("Enter the vertex name: ")
                graph.add_node(v)
                if v not in vertices:
                    vertices[v] = []
                    break
                else:
                    print(f"\nTry again. Vertex {v} is already created.")


construct_graph()