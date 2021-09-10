#!/usr/bin/env python3

import fileinput
import random

import graph_tools as gt


def main():
    g = gt.Graph(directed=False)
    g.import_dot(fileinput.input())
    nodes = g.vertices()
    t = 1000
    seed_results = []
    friends_results = []
    for _ in range(t):
        # random
        seed = random.choice(nodes)
        seed_degree = g.degree(seed)
        seed_results.append(seed_degree)

        # random with neighbor
        friends = g.neighbors(seed)
        firends_degree = [g.degree(v) for v in friends]
        average_firends_degree = sum(firends_degree) / len(firends_degree)
        friends_results.append(average_firends_degree)

    print('random:', sum(seed_results) / len(seed_results))
    print('random neighbor:', sum(friends_results) / len(friends_results))


if __name__ == "__main__":
    main()
