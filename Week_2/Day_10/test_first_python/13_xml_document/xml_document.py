class XMLDocument:
    
    def __init__(self, indents=False):
        self.indents = indents
        
    def indent(self, spaces):
        if self.indents:
            return " "*spaces
        else:
            return ""
            
    def newline_ifnec(self):         
        if self.indents:            
            return "\n" 
        else:            
            return  ""     

    def say(self, thing, options_hash, spaces=0, function=None):
        if options_hash == {} and function is None:
            return self.indent(spaces) + "<{thing}/>".format(thing=thing) + self.newline_ifnec()
        elif function is not None:
            def argument_accessor(*args, **kwargs):
                text = function(*args, **kwargs)
                return (self.indent(spaces) + "<{thing}>".format(thing=thing) +
                    self.newline_ifnec() + "{text}".format(text=text) + self.indent(spaces) + 
                    "</{thing}>".format(thing=thing)  +  self.newline_ifnec() )
            return argument_accessor
        else:
            name = options_hash["name"]
            return self.indent(spaces) + "<{thing} name='{name}'/>".format(thing=thing, name=name) + self.newline_ifnec()
            
    def hello(self, options_hash={}, function=None):
        if function is not None:
            def argument_accessor(*args, **kwargs):
                return self.say("hello", options_hash, function=function)(*args, **kwargs)
            return argument_accessor
        else:
            return self.say("hello", options_hash)        
            
    def goodbye(self, options_hash={}, function=None):
        if function is not None:
            def argument_accessor(*args, **kwargs):
                return self.say("goodbye", options_hash, 2, function)(*args, **kwargs)
            return argument_accessor
        else:
            return self.say("goodbye", options_hash, 2) 
            
    def come_back(self, options_hash={}, function=None):
        if function is not None:
            def argument_accessor(*args, **kwargs):
                return self.say("come_back", options_hash, 4, function)(*args, **kwargs)
            return argument_accessor
        else:
            return self.say("come_back", options_hash, 4)
            
    def ok_fine(self, options_hash={}):
        def f():
            return self.indent(6) + "<ok_fine {0}='{1}'/>".format(options_hash.keys()[0], options_hash[options_hash.keys()[0]]) + self.newline_ifnec()
        return f
        
    def send(self, string):
        return "<{string}/>".format(string=string) 
                
                
                
                
                
                
                
                
                
                
                
                
                
        
        
            
            