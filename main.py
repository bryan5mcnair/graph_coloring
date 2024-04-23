import networkx as nx
import matplotlib.pyplot as plt
import os
import numpy as np
import matplotlib.patches as mpatches

# p = SymmetricFunctions(QQ).p()

def get_vertices(adj_list):
    return list(adj_list.keys())

def pretty_print_edges(edge_tuples):
    return [f"{v1}<-->{v2}" for v1, v2 in edge_tuples]

def draw_graph(graph, color_map, chromatic_polynomial, coloring_possible, color_num, is_valid_coloring, term_statement, colors):
    num_ways = eval(str(chromatic_polynomial).replace("x", str(color_num)))
    is_coloring_possible = f"Not able to color this graph with {color_num} colors" if not coloring_possible else f"There are {num_ways} ways to color this graph with {color_num} colors."
    nx.draw(graph, with_labels=True, font_weight='bold', node_color=color_map)
    plt.text(0, 0, f"Chromatic Polynomial: {chromatic_polynomial}", horizontalalignment='center', verticalalignment='center')
    plt.text(0, -0.1, is_coloring_possible, horizontalalignment='center', verticalalignment='center')
    plt.text(0, -0.2, is_valid_coloring, horizontalalignment='center', verticalalignment='center')
    plt.text(0, -0.3, term_statement, horizontalalignment='center', verticalalignment='center')
    
    handles = []

    for i, color in enumerate(colors):
        handles.append(mpatches.Patch(color=color, label=f"Color {i+1}"))
    
    plt.legend(handles=handles)

    plt.show()

def get_colors(n):
    colors = ["#808080"]
    for i in range(n):
        j = 0
        while True:
            r, g, b = tuple(list(np.random.choice(range(256), size=3)))
            color = "#{:02x}{:02x}{:02x}".format(r,g,b)
            if (color not in colors or j == 20) and color != "#808080":
                colors.append(color)
                break
            j += 1
    return colors

def is_valid_color_num(num, maxNum):
    return num.isdigit() and int(num) > 0 and int(num) <= maxNum

def update_graph_colors(graph, colors, coloring):
    color_count = dict()
    color_map = []
    for node in graph:
        if coloring[node] not in color_count:
            color_count[coloring[node]] = 1
        else:
            color_count[coloring[node]] += 1
        color_map.append(colors[coloring[node]])
    return (color_map, color_count)

def is_coloring_possible(chrom_poly, x):
    return eval(str(chrom_poly).replace("x", str(x))) > 0

def valid_coloring(adjList, coloring):
    for v1 in adjList:
        if coloring[v1] == 0:
            return "Not all the vertices are colored."
        for v2 in adjList[v1]:
            if coloring[v1] == coloring[v2[1]]:
                return "This is not a valid coloring of the graph"
    return "This is a valid coloring of the graph"

def pretty_print_colors(coloring):
    res = []
    for node in coloring:
        if coloring[node] != 0:
            res.append(f"vertex {node} is colored color {coloring[node]}")
    return ", ".join(res)

def construct_graph():
    plt.rcParams.update({'font.size': 14})

    graph = nx.Graph()
    vertices = dict()
    coloring = dict()

    e_list = []

    optionExists = True

    colors = []
    while True:
        color_num = input("How many colors do you want to use? ")
        if is_valid_color_num(color_num, float("inf")):
            color_num = int(color_num)
            colors = get_colors(color_num)
            break
        print("Try again. Not a valid input.")
    
    while True:
        os.system('cls')

        color_map, color_count = update_graph_colors(graph, colors, coloring)

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
        if list(color_count.keys()) != [0] and list(color_count.keys()) != []:
            print(f"Also, {pretty_print_colors(coloring)}.")

        option = input("\nEnter your option: ")

        if option not in [str(num) for num in range(1,6)]:
            optionExists = False
            continue
        optionExists = True
        
        option = int(option)
        if option == 1:
            while True:
                v = input("Enter the vertex name: ")
                v = v.lower().strip()
                
                if v == "":
                    print("\nTry again. Blank vertex is not allowed.")
                elif v not in vertices:
                    graph.add_node(v)
                    coloring[v] = 0 # set default node color to gray
                    vertices[v] = []
                    break
                else:
                    print(f"\nTry again. Vertex {v} is already created.")
        elif option == 2:
            while True:
                v1 = input("\nEnter the start vertex for the edge: ")
                v1 = v1.lower().strip()
                v2 = input("Enter the ending vertex for the edge: ")
                v2 = v2.lower().strip()

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
                askEdgeAgain = askEdgeAgain.strip()
                if askEdgeAgain.lower() not in ['y', 'yes']:
                    break
        elif option == 3:
            while True:
                v = input("\nEnter the vertex that you want to color: ")
                v = v.lower().strip()

                if v not in vertices:
                    print(f"\nTry again. Vertex {v} does not exist.")
                else:
                    color = input(f"From the {color_num} colors, choose a color between 1 and {color_num}, inclusive, to color vertex {v}: ")
                    color = color.strip()
                    if not is_valid_color_num(color, color_num):
                        print(f"\nTry again. This is not a valid color. Choose a color between 1 and {color_num}.")
                    else:
                        color = int(color)
                        coloring[v] = color
                        break
                askColorAgain = input("Do you want to continue with working with colors (Y/N)? ")
                askColorAgain = askColorAgain.strip()
                if askColorAgain.lower() not in ['y', 'yes']:
                    break
        elif option == 4:
            chrom_poly = nx.chromatic_polynomial(graph)
            coloring_possible = is_coloring_possible(chrom_poly, color_num)
            is_valid_coloring = valid_coloring(vertices, coloring)
            coefficient = 1
            terms = ""
            colored = True
            for color in color_count:
                if color == 0:
                    terms = "The term for the chromatic symmetric function is unable to be calculated so far."
                    coefficient = ""
                    colored = False
                    break
                else:
                    coefficient *= int(color_count[color])
                    terms += f"x_{color}"
            coefficient = "" if coefficient == 1 else str(coefficient)
            term = coefficient + terms
            if colored:
                term = f"The term of the chromatic symmetric function for this graph would be {term}."
            draw_graph(graph, color_map, chrom_poly, coloring_possible, color_num, is_valid_coloring, term, colors[1:])
        elif option == 5:
            print("The End :)")
            break



construct_graph()