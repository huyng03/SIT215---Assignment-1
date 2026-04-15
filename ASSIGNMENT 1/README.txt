SIT215: Computational Intelligence
Assignment 1: Problem Solving

Student Name: Tien Huy Nguyen
Student ID: 223009962

Source notebook: s223009962.ipynb

Overview
This README summarises the work in s223009962.ipynb. The notebook models a road network in Hanoi, builds a weighted state-space graph, runs A* search, compares it against Dijkstra's algorithm, and compares Manhattan and Euclidean heuristics.

Project files
- s223009962.ipynb: main notebook
- landmarks_path.py: landmark and path dataset
- GoogleMaps.png: map image used for visualisation

Python libraries used
- json
- pathlib
- importlib
- matplotlib
- networkx
- Pillow
- math
- queue
- time
- pandas

How to run
1. Open s223009962.ipynb in Jupyter Notebook or JupyterLab.
2. Make sure the required Python packages are installed.
3. Confirm the notebook can find the map image file before running all cells.
4. Run the notebook from top to bottom.

Run notes
- The notebook loads landmark and path data from landmarks_path.py.
- The current folder contains GoogleMaps.png, but the notebook's map path may need to be adjusted if you rerun it in a different environment.
- The graph image is saved to ../Report/figures/state_space_graph.png in the notebook, so that folder must exist if you want the save step to succeed.

Activity 1: Problem Formulation
The notebook builds a weighted graph from the landmark dataset. Path cost is calculated with:

weight = (1 + risk + traffic) * (alpha * distance + beta * time)

where:
- alpha = 2.3
- beta = 4.6

Recorded graph summary from the notebook
- Directed routes: 31
- Undirected routes: 6
- Total paths in dataset: 37
- Weakly connected: True
- Strongly connected: True
- Strongly connected component: nodes 1 to 21

Activity 2: A* Search Algorithm
The notebook implements A* with a Euclidean-distance heuristic based on landmark coordinates.

Recorded example result
- Start node: 3
- Goal node: 1
- Best path: [3, 16, 17, 2, 9, 1]
- Total estimated cost: 49.10

Activity 3: Uninformed Search (Dijkstra)
The notebook compares A* against Dijkstra on three test cases.

Test cases
- Case 1: 3 -> 1
- Case 2: 2 -> 5
- Case 3: 1 -> 4

Recorded notebook results
- Case 1
  A* path: [3, 16, 17, 2, 9, 1], cost 49.10, nodes expanded 6
  Dijkstra path: [3, 16, 17, 2, 9, 1], reported cost 0.00, nodes expanded 18
- Case 2
  A* path: [2, 9, 5], cost 11.67, nodes expanded 3
  Dijkstra path: [2, 9, 5], reported cost 0.00, nodes expanded 9
- Case 3
  A* path: [1, 10, 12, 7, 9, 5, 2, 4], cost 52.28, nodes expanded 8
  Dijkstra path: [1, 10, 12, 7, 9, 5, 2, 4], reported cost 0.00, nodes expanded 19

Activity 4: Heuristic Comparison
The notebook compares Manhattan distance against Euclidean distance inside A*.

Recorded notebook results
- Case 1: Manhattan nodes 18, runtime 0.0501 ms; Euclidean nodes 18, runtime 0.0331 ms
- Case 2: Manhattan nodes 9, runtime 0.0200 ms; Euclidean nodes 9, runtime 0.0179 ms
- Case 3: Manhattan nodes 19, runtime 0.0319 ms; Euclidean nodes 19, runtime 0.0300 ms

Summary
- The notebook models a connected graph with 21 landmarks and 37 paths.
- A* successfully finds paths for all three evaluation cases.
- Dijkstra returns the same routes in the notebook output, with more node expansions.
- Manhattan and Euclidean heuristics both produce valid guided search in the recorded runs.
- The notebook also includes a state-space graph visualisation of the network.

Notes
- This README is a text summary of the notebook, not a full cell-by-cell export.
- Embedded notebook figures are not reproduced here.
