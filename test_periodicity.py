from periodicity import Periodicity, LTM, FY, FQ, FH

types = LTM, FY, FQ, FH

def test_equality_inequality_within_periodicities():
    for index, t in enumerate(types):
        assert t() == types[index]()
        for t2 in types[index+1:]:
            print t2
            print index
            assert t() != t2()


def test_against_non_periodicities():
    print(LTM.__bases__)
    if Periodicity in LTM.__bases__:
        print(LTM.__bases__) 
    #assert 0 == types[0]()
