#!/usr/bin/python

import argparse

class Node():
    def __init__(self, id, name, parent_id=None, parent=None, is_root=False):
        self.id = id
        self.name = name
        self.parent_id = parent_id
        self.parent = parent
        self.children = []
        self.land = []
        self.is_root = is_root

    def __str__(self):
        return 'Node: {}'.format(self.id)

    def __repr__(self):
        return 'Node: {}'.format(self.id)

    def get_descendants(self):
        descendants = []
        for child in self.children:
            descendants.append(child)
            descendants.extend(child.get_descendants())
        return descendants

    def get_root(self):
        if not self.is_root:
            return self.parent.get_root()
        else:
            return self

    def get_level(self, level=0):
        if not self.is_root:
            level += 1
            return self.parent.get_level(level)
        else:
            return level

    def get_all_land(self):
        descendants_land = self.land
        for node in self.get_descendants():
            descendants_land.extend(node.land)
        return descendants_land

    def print_node(self):
        return self.get_level()*' | ' + '{}; {}; owner of {} land parcels'.format(
            self.id,
            self.name,
            len(self.get_all_land())
        )
    def print_tree(self, mode='full_tree', nodes_to_print=[]):
        if mode == 'full_tree':
            current_node = ''
            if self.get_root().id == self.id:
                current_node = ' ***'
            print(self.get_root().print_node() + current_node)
            for node in self.get_root().get_descendants():
                if node.id == self.id:
                    current_node = ' ***'
                else:
                    current_node = ''
                print(node.print_node() + current_node)
        elif mode == 'expand':
            print(self.print_node() + ' ***')
            for node in self.get_descendants():
                if node.id == self.id:
                    current_node = ' ***'
                else:
                    current_node = ''
                print(node.print_node() + current_node)
        elif mode == 'from_root':
            if not self.is_root:
                nodes_to_print.append(self)
                return self.parent.print_tree(mode, nodes_to_print)
            else:
                print(self.get_root().print_node())
                nodes_to_print.reverse()
                for node in nodes_to_print:
                    if node == nodes_to_print[-1]:
                        print(node.print_node() + ' ***')
                    else:
                        print(node.print_node())
           
def main():
    mode = ''
    company_id = ''
    nodes = {}

    parser = argparse.ArgumentParser()
    parser.add_argument('company_id', type=str, help='id of company to find lands')
    parser.add_argument('-m', '--mode', type=str, choices=['full_tree', 'from_root', 'expand'], default='full_tree', help='land tree parsing mode')
    args = parser.parse_args()
    company_id = args.company_id
    mode = args.mode

    with open("./company_relations.csv") as csv:
        next(csv) # header
        for line in csv:
            id, name, parentId = line.strip().split(",")
            if parentId == '':
                nodes[id] = Node(id, name, is_root=True)
            else:
                nodes[id] = Node(id, name, parentId)
    for child_node in nodes:
        if nodes[child_node].parent_id:
            for parent_node in nodes:
                if nodes[parent_node].id == nodes[child_node].parent_id:
                    nodes[child_node].parent = nodes[parent_node]
                    nodes[parent_node].children.append(nodes[child_node])

    with open("./land_ownership.csv") as csv:
        next(csv) # header
        for line in csv:
            landId, companyId = line.strip().split(",")
            nodes[companyId].land.append(landId)

    print('--------------------')
    print('Company ID -', company_id)
    print('Tree parsing mode -', mode)
    print('--------------------')

    valid, message = validate(company_id, nodes)
    if not valid:
        print('***')
        print(message)
        print('***')
    else:
        nodes[company_id].print_tree(mode)

def validate(company_id, nodes):
    if not nodes.get(company_id, False):
        return False, 'There is no information for the selected company'
    return True, ''

if __name__ == "__main__":
    main()
