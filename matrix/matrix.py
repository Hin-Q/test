import copy


class Matrix:

    def __init__(self, list1, a, b):
        # self.list = []
        # self.a = a
        # self.b = b
        l = []
        count = 0
        for j in range(0, a):
            l.append([])
            if a * b > len(list1) and count == len(list1):
                for k in range(0, b):
                    l[j].append(0)
            for i in list1[(b * j):b * (j + 1)]:
                l[j].append(i)
                count = count + 1
                if len(l[j]) < b and count == len(list1):
                    for k in range(0, b - len(l[j])):
                        l[j].append(0)
        self.list = l

    def __str__(self):
        str1 = ''
        for i in self.list:
            for j in i:
                str1 = str1 + str(j) + "    "
            str1 = str1 + '\n'
        return str1

    def __add__(self, other):
        list1 = copy.deepcopy(self.list)
        count1 = 0
        for i in other.list:
            count2 = 0
            for j in i:
                list1[count1][count2] = self.list[count1][count2] + j
                count2 = count2 + 1
            count1 = count1 + 1
        return list1

    def __sub__(self, other):
        list1 = copy.deepcopy(self.list)
        count1 = 0
        for i in other.list:
            count2 = 0
            for j in i:
                list1[count1][count2] = self.list[count1][count2] + (-j)
                count2 = count2 + 1
            count1 = count1 + 1
        return list1

    def __eq__(self, other):
        count1 = 0
        for i in other.list:
            count2 = 0
            for j in i:
                if self.list[count1][count2] != j:
                    return False
                count2 = count2 + 1
            count1 = count1 + 1
        return True


p1 = Matrix([1, 2, 3, 4, 5, 6], 7, 4)
p2 = Matrix([1, 2, 9, 4, 5, 6], 7, 4)
print(p1)
print(p2)
p3 = p1 + p2
print(p3)
print(p1 + p2)
print(p1 - p2)
print(p1 == p2)
