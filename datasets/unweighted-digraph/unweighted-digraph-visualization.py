#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
import networkx as nx
import matplotlib.pyplot as plt

"""
Visualize the files generated by unweighted-digraph.generator.py
"""

def args_parser():
    parser = argparse.ArgumentParser(prog="Unweighted DiGraph Visualization")
    parser.add_argument("file_path", help="the file generated by unweighted-digraph.generator.py")
    args = parser.parse_args()

    if not os.path.isfile(args.file_path):
        print("[ERROR] it's not a file, please specify a right file path.")
        exit(1)

    return args.file_path

def show(graph, file_path, index=None):
    title = "{} [{}]".format(file_path, index) if index else file_path
    plt.title(title)
    pos = nx.spring_layout(graph, iterations=50)
    nx.draw(graph, pos=pos, node_color='b', edge_color='y', with_labels=True, font_weight='bold')
    plt.show()

def visualize_multiple_graphs(file_path):
    graphs = []
    with open(file_path) as file:
        lines = file.readlines()
        graph = None
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            
            info = line.split()
            if info[0] == 't':
                if graph:
                    graphs.append(graph)
                
                graph = nx.DiGraph() # create a directed graph

            elif info[0] == 'v' and len(info) == 2:
                graph.add_node(info[1])
            elif info[0] == 'e' and len(info) == 3:
                graph.add_edge(info[1], info[2])
            else:
                raise EOFError
    
    while True:
        print("Total {} graphs can be visualized, enter graph index(start from 0) to show or  'N' to exit.".format(len(graphs)))
        order = input()
        if str.upper(order) == 'N':
            break
        elif str.isdigit(order):
            index = int(order)
            if index < len(graphs):
                show(graphs[index], file_path, index) 
            else:
                print('Out of the graph index, it must be less than {}'.format(len(graphs)))
        else:
            print("Unrecognizable order, please re-input")


def visualize_single_graph(file_path): 
    graph = nx.DiGraph()
    with open(file_path) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith('#'):
                continue

            info = line.split() 
            if len(info) == 2:
                v1 = int(info[0])
                v2 = int(info[1])
                graph.add_node(v1)
                graph.add_node(v2)
                graph.add_edge(v1, v2)
            else:
                raise EOFError 

    show(graph, file_path)

if __name__ == "__main__":
    file_path = args_parser()
    with open(file_path) as f:
        first = f.readline()
        if first.startswith('t'):
            visualize_multiple_graphs(file_path)
        elif first.startswith('#'):
            visualize_single_graph(file_path)
        else:
            raise IOError("Wrong file, it's not the file generated by unweighted-digraph.generator.py")
        