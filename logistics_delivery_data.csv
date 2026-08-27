"""
Project 4: Route Optimization
Simple nearest-neighbor heuristic.
"""

import numpy as np

# Depot = point 0; remaining points are delivery locations.
coords = np.array([
    [0,0], [3,8], [7,2], [12,9], [5,14], [16,4], [20,11],
    [24,3], [28,13], [18,17], [10,20], [2,18], [25,20]
], dtype=float)

def route_distance(route):
    total = 0.0
    for a, b in zip(route[:-1], route[1:]):
        total += np.linalg.norm(coords[b] - coords[a])
    return total

# Baseline: fixed sequential order
baseline = [0] + list(range(1, len(coords))) + [0]

# Nearest-neighbor heuristic
unvisited = set(range(1, len(coords)))
current = 0
nn_route = [0]

while unvisited:
    nxt = min(
        unvisited,
        key=lambda j: np.linalg.norm(coords[current] - coords[j])
    )
    nn_route.append(nxt)
    unvisited.remove(nxt)
    current = nxt

nn_route.append(0)

baseline_distance = route_distance(baseline)
nn_distance = route_distance(nn_route)
savings = (baseline_distance - nn_distance) / baseline_distance * 100

print("Baseline route:", baseline)
print("Nearest-neighbor route:", nn_route)
print(f"Baseline distance: {baseline_distance:.2f}")
print(f"Optimized distance: {nn_distance:.2f}")
print(f"Distance reduction: {savings:.1f}%")
