
def namedtuple(name, fields):
    def init(self, *vals):
        for i,val in enumerate(vals):
            self.__setattr__(fields[i], val)

    return type(name, (), {'__init__':init})


