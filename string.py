class MyString:
    def __init__(self,string):
        self.string = string
    def stringComment(self):
        print(f"{self.string}")
    def slicingString(self):
        print(f"{self.string[:]}") ## All String
        print(f"{self.string[6:]}") ## All String
        print(f"{self.string[6:10]}") ## All String
        print(f"{self.string[:10]}") ## All String
        print(f"{self.string[-len(self.string):]}") ## All String        
obj = MyString('laxman Kendre')
obj.slicingString()

