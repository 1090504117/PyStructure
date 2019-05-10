# -*- coding: UTF-8 -*-

def DeepthFirstSearchPath1(G , s, S=None):
    if S is None:
        S = set()
    S.add(s)
    for u in G[s]:
        if u in S:
            continue
        DeepthFirstSearchPath1(G, u, S)
    return S

def DeepthFirstSearchPath2(G , s):
    S,Q = set(),[]
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        Q.extend(G[u])
    return S


def Test():
    graph = {}

    graph['a'] = {'b', 'c', 'd', 'e', 'f'}
    graph['b'] = {'c', 'e'}
    graph['c'] = {'d'}
    graph['d'] = {'e'}
    graph['e'] = {'f'}
    graph['f'] = {'c', 'g', 'h'}
    graph['g'] = {'f', 'h'}
    graph['h'] = {'f', 'g'}

    S = DeepthFirstSearchPath1(graph, 'a')
    print S

    S = DeepthFirstSearchPath2(graph, 'a')
    print S

