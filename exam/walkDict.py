#编写提取dict嵌套的函数，提取出的dict都赋给一个名字
class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value
    def walk(self):
        for key, value in self.items():
            if isinstance(value, Vividict):
                for tup in value.walk():
                    yield (key,) + tup
            else:
                yield key, value
    def walkDict(self, dicts):
        for key, dict in dicts.items():
            if type(dict).__name__ == 'dict':
                print(key, dict)
                Vividict.walkDict(self,dict)


if __name__ == "__main__":
    dicts = {'PDC1279A_vs_PDC1279': {'UTR3': 9,
                             'UTR5': 4,
                             'downstream': 5,
                             'exonic': 149,
                             'intergenic': 170,
                             'intronic': 163,
                             'ncRNA_exonic': 17,
                             'ncRNA_intronic': 23,
                             'splicing': 2,
                             'upstream;downstream': 2},
             'PDC1279C_vs_PDC1279': {'UTR3': 11,
                             'UTR5': {
                                 'a':2,
                                 'b':{
                                     'c':3
                                 }
                             },
                             'downstream': 1,
                             'exonic': 174,
                             'intergenic': 189,
                             'intronic': 172,
                             'ncRNA_exonic': 24,
                             'ncRNA_intronic': 36,
                             'splicing': 4,
                             'upstream': 2,
                             'upstream;downstream': 2}}

    test_dicts={'A': {
                    'a':2,
                    'b':{
                        'c':3
                        },
                    'bb':{
                        'cc':4,
                        'dd':5
                    }
                    },
        'B':{
                    'd':2,
                    'e':{
                        'f':3
                        }
                    }
                }
    viviDict = Vividict(test_dicts)
    print(viviDict.walk())
    for tup in viviDict.walk():
        print(tup)
    if test_dicts != None and type(test_dicts).__name__ == 'dict':
        print('whole dict:')
        print(test_dicts)
    viviDict.walkDict(test_dicts)