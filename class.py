class Name():
    
    not_allowed=["shit", "fuck"]
    def __init__(self, name):
        self.name= name
        
    def cones(self):
        if self.name in Name.not_allowed :
            raise ValueError("name not allowed") 
        else:
            return f"{self.name}"
        
        
nada =Name("shit")        
print(nada.cones())