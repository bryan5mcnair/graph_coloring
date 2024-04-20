import networkx as nx
import matplotlib.pyplot as plt
import os

def get_vertices(adj_list):
    return list(adj_list.keys())

def pretty_print_edges(edge_tuples):
    return [f"{v1}<-->{v2}" for v1, v2 in edge_tuples]

def construct_graph():
    graph = nx.Graph()
    vertices = dict()
    e_list = []

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

        v_list = get_vertices(vertices)

        if v_list != []:
            print(f"\nCurrently, you created the vertices {', '.join(v_list)}.")
        if e_list != []:
            print(f"Also, you created the edges {', '.join(pretty_print_edges(e_list))}.")

        option = input("\nEnter your option: ")

        if option not in [str(num) for num in range(1,6)]:
            optionExists = False
            continue
        optionExists = True
        
        option = int(option)
        if option == 1:
            while True:
                v = input("Enter the vertex name: ")
                v = v.lower()
                graph.add_node(v)
                if v not in vertices:
                    vertices[v] = []
                    break
                else:
                    print(f"\nTry again. Vertex {v} is already created.")
        elif option == 2:
            while True:
                v1 = input("\nEnter the start vertex for the edge: ")
                v1 = v1.lower()
                v2 = input("Enter the ending vertex for the edge: ")
                v2 = v2.lower()

                if v1 == v2:
                    print("\nTry again. The start vertex can't equal the end vertex.")
                elif v1 not in v_list or v2 not in v_list:
                    print("\nTry again. Both vertices need to exist. Make sure the vertices are added or typed correctly.")
                elif (v1, v2) in e_list or (v2, v1) in e_list:
                    print("\nTry again. This edge has already been created.")
                else:
                    graph.add_edge(v1, v2)
                    vertices[v1].append((v1, v2))
                    vertices[v2].append((v2, v1))
                    e_list.append((v1,v2))
                    break
                askEdgeAgain = input("Do you want to continue with working with edges (Y/N)? ")
                if askEdgeAgain.lower() not in ['y', 'yes']:
                    break


construct_graph()