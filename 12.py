from utils import slurp, unique, unpack
from collections import defaultdict


def all_paths(graph, start, limit):
    def traverse(graph, node, path, paths, visits, limit):
        if node == "end":
            path.append(node)
            paths.append(tuple(path))
        elif node in visits and limit in visits.values():
            pass
        else:
            path.append(node)
            if node == node.lower():
                visits[node] += 1
            for child in sorted(graph[node]):
                if child != "start":
                    traverse(graph, child, path.copy(), paths, visits.copy(), limit)

    paths = []
    traverse(graph, start, [], paths, defaultdict(int), limit)
    paths = unique(paths)
    return paths


def part1(data):
    graph = defaultdict(list)
    for p in unpack(data):
        from_, to_ = p.split("-")
        graph[from_].append(to_)
        graph[to_].append(from_)
    return len(all_paths(graph, "start", 1))


def part2(data):
    graph = defaultdict(list)
    for p in unpack(data):
        from_, to_ = p.split("-")
        graph[from_].append(to_)
        graph[to_].append(from_)
    return len(all_paths(graph, "start", 2))


testdata = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""
filedata = slurp("12.txt")

print("#--- Day 12: Passage Pathing: part1:", end=" ")
assert part1(testdata) == 10
print(part1(filedata))

print("#--- Day 12: Passage Pathing: part2:", end=" ")
assert part2(testdata) == 36
print(part2(filedata))
