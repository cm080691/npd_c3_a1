class Your_Dict(dict):

    def __setattr__(self, attr, value):
        self[attr] = value


    def __getattr__(self, attr):
        return self.get(attr)
