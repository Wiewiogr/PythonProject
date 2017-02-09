class Gene(float):
    def __new__(self,val,origin):
        return float.__new__(self,val)

    def __init__(self,val, origin):
        float.__init__(self,val)
        self.origin = origin

    def __copy__(self):
            return self

    def __deepcopy__(self, memo):
            return self
