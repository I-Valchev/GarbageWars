import urllib2
import urllib
import threading
from collections import defaultdict

HOST_URL="http://172.16.18.230:8080"
OBJECTS_API="/api/sector/%d/objects"
ROOTS_API="/api/sector/%d/roots"
TRAJECTORY_AP="/api/sector/%d/company/Bobi&IvoFailMasters/trajectory"

def get_objects(sector):
    url=HOST_URL+OBJECTS_API % sector
    res=urllib2.urlopen(url)
    edges={}
    for line in res.readlines():

        key=int(line.strip().split(' ')[0])
        value=int(line.strip().split(' ')[1])

        if key is not value:
            if key in edges:
                edges[key].add(value)
            else:
                edges[key]=set([value])
    return edges

def get_roots(sector):
    url=HOST_URL+ROOTS_API % sector

    res=urllib2.urlopen(url)
    nodes=[]
    for line in res.readlines():
        nodes.append(int(line.strip()))
    return nodes

def DFS(G,v,seen=None,path=None):
    if seen is None: seen = []
    if path is None: path = [v]

    seen.append(v)

    paths = []
    if G.has_key(v):
        for t in G[v]:
            if t not in seen:
                t_path = path + [t]
                paths.append(tuple(t_path))
                paths.extend(DFS(G, t, seen, t_path))
    return paths

def get_objects(sector):
    url=HOST_URL+OBJECTS_API % sector
    res=urllib2.urlopen(url)
    edges={}
    for line in res.readlines():

        key=int(line.strip().split(' ')[0])
        value=int(line.strip().split(' ')[1])

        if key is not value:
            if key in edges:
                edges[key].add(value)
            else:
                edges[key]=set([value])
    return edges

def get_roots(sector):
    url=HOST_URL+ROOTS_API % sector

    res=urllib2.urlopen(url)
    nodes=[]
    for line in res.readlines():
        nodes.append(int(line.strip()))
    return nodes   

def remove_edge_from_objects(edge, objects):
    for iterate_edge in objects:
        if edge in objects[iterate_edge]:
            objects[iterate_edge].remove(edge)

def remove_all_subsequent_objects(root, objects):    
    if objects.has_key(root):
        while root in objects and objects[root]:
            child = objects[root].pop()
            remove_all_subsequent_objects(child, objects)
        if objects.has_key(root):
            remove_edge_from_objects(root, objects)
            del objects[root]
    else:
        remove_edge_from_objects(root, objects)

def remove_not_permitted_elements(objects, roots):
    for root in roots:
        remove_all_subsequent_objects(root, objects)
    return objects

def trajectory(sector,path):
    url=HOST_URL+TRAJECTORY_AP % sector
    path={'trajectory': path}
    data = urllib.urlencode(path)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    return response.read()

def find_best_path(cleared_edges):
    best_path = list()
    i = True
    for edge in cleared_edges:
        all_paths = DFS(cleared_edges, edge)
        if all_paths:
            max_path  = max(all_paths, key=lambda l: len(l))
            if i:
                i = False
                best_path = max_path

            if best_path < max_path:
                best_path = max_path

    return best_path

def convert_to_string_path(path):
    return ' '.join(str(element) for element in path)

class SectorCleaner(threading.Thread):
    def __init__(self, threadID, name, sector):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.sector = sector
    def run(self):
        while True:
            self.run_sector(self.sector)

    def run_sector(self, sector):
        print "Getting edges and roots"
        edges = get_objects(self.sector)
        roots = get_roots(self.sector)
        print "Clearing edges"
        cleared_edges = remove_not_permitted_elements(edges, roots)
        check_edges = cleared_edges

        best_path = find_best_path(cleared_edges)
        print "Best path so far: " + str(best_path)
        while cleared_edges:
            best_paths = []
            while best_path:
                best_paths.append(best_path)
                cleared_edges = remove_not_permitted_elements(cleared_edges, best_path)
                best_path = find_best_path(cleared_edges)
                print "New best path: " + str(best_path)

            if best_paths:
                print "Sending" +  "=" + convert_to_string_path(max(best_paths, key=len)) + "="
                trajectory(self.sector, convert_to_string_path(max(best_paths, key=len)))
                if best_path in best_paths:
                    best_paths.remove(best_path)
            else:
                break


thread1 = SectorCleaner(1, "1st sector", 1)
thread2 = SectorCleaner(2, "1st sector", 2)
thread3 = SectorCleaner(3, "1st sector", 3)
thread4 = SectorCleaner(4, "1st sector", 4)
thread5 = SectorCleaner(5, "1st sector", 5)
thread6 = SectorCleaner(6, "1st sector", 6)
thread7 = SectorCleaner(7, "1st sector", 7)
thread8 = SectorCleaner(8, "1st sector", 8)
thread9 = SectorCleaner(9, "1st sector", 9)
thread10 = SectorCleaner(10, "1st sector", 10)


thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()