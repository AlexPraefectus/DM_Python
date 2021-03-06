from itertools import cycle, chain
from random import shuffle


class RelationMaker:
    """making relations with given variant
    aSb if a is mother of b
    aRb if a is mother-in-law of b
    """

    def __init__(self, set_a, set_b):
        self.set_a = set_a
        self.set_b = set_b
        self.set_a_operand_for_s = self.set_a.copy()
        self.set_b_operand_for_s = self.set_b.copy()
        self.set_a_operand_for_r = self.set_a.copy()
        self.set_b_operand_for_r = self.set_b.copy()
        self.s_relation = set()
        self.r_relation = set()
        self.intersection = set()
        self.difference = set()
        self.union = set()
        self.difference_with_u = set()
        self.reversed = set()

    def delete_impossible_mother_relation(self):
        """male can't be mother or mother-in-law"""
        for i in self.set_a:
            if i.GENDER == 'male':
                self.set_a_operand_for_s.discard(i)

    def delete_impossible_for_mother_in_law_relation(self):
        """
        male can't be mother or mother-in-law
        task was given in ukrainian
        marrieds have different terms for parents in law so in this task female can't have mother in law
        """
        for i in self.set_a:
            if i.GENDER == 'male':
                self.set_a_operand_for_r.discard(i)
        for i in self.set_b:
            if i.GENDER == 'female':
                self.set_b_operand_for_r.discard(i)

    def form_mother_child_relation(self):
        for i in zip(cycle(self.set_a_operand_for_s), self.set_b_operand_for_s):
            if i[0].name != i[1].name:
                self.s_relation.add((i[0].name, i[1].name))

    def form_mother_in_law_relation(self):
        for i in self.set_b_operand_for_r:
            for j in set(list(self.set_a_operand_for_r)):
                if (j.name, i.name) not in self.s_relation:
                    self.r_relation.add((j.name, i.name))
                    self.set_a_operand_for_r = list(self.set_a_operand_for_r)
                    shuffle(self.set_a_operand_for_r)
                    self.set_a_operand_for_r = set(self.set_a_operand_for_r)
                    break

    def relation_intersection(self):
        if self.r_relation and self.s_relation:
            self.intersection = self.r_relation.intersection(self.s_relation)
        return self.intersection

    def relation_union(self):
        if self.s_relation and self.r_relation:
            self.union = self.r_relation.union(self.s_relation)
        return self.union

    def relation_difference(self):
        if self.s_relation and self.r_relation:
            self.difference = self.r_relation - self.s_relation
        return self.difference

    def relation_difference_with_u(self):
        if self.s_relation and self.r_relation:
            universal = [[(i.name, j.name) for i in self.set_a] for j in self.set_b]
            universal = set(chain(*universal))
            self.difference_with_u = universal - self.r_relation
        return self.difference_with_u

    def reversed_r_relation(self):
        if self.r_relation:
            self.reversed = {(i[1], i[0]) for i in self.r_relation}
        return self.reversed
