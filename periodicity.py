class SuperPeriod(object):
    pass

class Periodicity(SuperPeriod):
    def __str__(self):
        self.cata(ltm_cb = lambda: "LTM",
                  fy_cb = lambda: "FY",
                  fq_cb = lambda: "FQ",
                  fh = lambda: "FH")

    def __eq__(self, other):
        #if Periodicity not in other.__bases:
        #    raise 
        return self.cata(
            lambda: other.cata(lambda: True,
                               lambda: False,
                               lambda: False,
                               lambda: False),
            lambda: other.cata(lambda: False,
                               lambda: True,
                               lambda: False,
                               lambda: False),
            lambda: other.cata(lambda: False,
                               lambda: False,
                               lambda: True,
                               lambda: False),
            lambda: other.cata(lambda: False,
                               lambda: False,
                               lambda: False,
                               lambda: True)
            )

    def __hash__(self):
        return hash(str(self))

class LTM(Periodicity):
    def cata(self, ltm_cb, fy_cb, fq_cb, fh_cb):
        return ltm_cb()

class FY(Periodicity):
    def cata(self, ltm_cb, fy_cb, fq_cb, fh_cb):
        return fy_cb()

class FQ(Periodicity):
    def cata(self, ltm_cb, fy_cb, fq_cb, fh_cb):
         return fq_cb()

class FH(Periodicity):
    def cata(self, ltm_cb, fy_cb, fq_cb, fh_cb):
        return fh_cb()
