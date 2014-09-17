class Friend:
    def greeting(self, friend=None):
        if friend is None:
            return "Hello!"
        else:
            return "Hello" + ", {0}".format(friend) + "!"