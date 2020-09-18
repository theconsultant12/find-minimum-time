class Compound:
    def __init__(self, name, smile, weight):
        self.smile = smile
        self.weight = weight
        self.name = name
        self.ph = 0
    def print_compound(self):
        print(self.name, " ", self.smile, " ", self.weight, "\n")


def load_compounds(filename, compound_lists):
    import csv
    with open(filename, 'r') as readfile:
        reading_in = csv.reader(readfile)
        for line in reading_in:
            compound_lists[i] = Compound(line[1],line[2],line[3])
            i += 1

def calculatesimilarity(compound_lists, i, j):

    templist1 = compound_lists[i].hashcode.split(' ')
    templist2 = compound_lists[j].hashcode.split(' ')

    common_hash = 0
    hashcodecount_1 = 0
    hashcodecount_2 = 0


    for hash in templist1:
        hashcodecount_1 += 1
        for hsh in templist2:
            hashcodecount_2 +=2
            if hsh == hash:
                common_hash += 1
    return common_hash/(hashcodecount_1+hashcodecount_2-common_hash)

compound_lists = ()
load_compounds("book 1.csv", compound_lists)
similarity = calculatesimilarity(compound_lists, index1, index2)

        
