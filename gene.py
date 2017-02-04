class Gene(float):
    def __init__(self,val):
        float.__init__(self,val)
        print(self.real)



#class Gene(object) :
#    def __init__(self, val) :
#        self._val = float(val)
#        print self._val
#
#    def __add__(self, val) :
#        if type(val) == Gene :
#            return Gene(self._val + val._val)
#        return self._val + val
#
#    def __radd__(self, val) :
#        self._val += val
#        return self
#
#    def __mul__(self, val) :
#        if type(val) == Gene :
#            return Gene(self._val * val._val)
#        return self._val * val
#
#    def __rmul__(self, val) :
#        self._val *= val
#        return self
#
#    def __neg__(self) :
#        self._val *= -1
#        return self
#
#    def __sub__(self, val) :
#        if type(val) == Gene :
#            return Gene(self._val - val._val)
#        return self._val - val
#
#    def __rsub__(self, val) :
#        self._val -= val
#        return self
#
#    def __float__(self):
#        return self._val
#
#    def __str__(self) :
#        return str(self._val)
#
#    def __repr__(self) :
#        return str(self._val)
#
