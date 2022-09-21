class Shark:
#defines the class name
    def __init__(self, name):
        self.name = name
#Uses the init method to give self the name attribute
    def swim(self):
        print(self.name + " is swimming.")
#create the method swim which uses concatenation to print the name of the current shark object along with the text "is swimming"
    def be_awesome(self):
        print(self.name + " is being awesome.")
#create the method be_awesome which uses concatenation to print the name of the current shark object along with the text "is swimming"
def main():
#defines the main function for this program and dictates what will be outputed 
    sammy = Shark("Sammy")
#create object Sammy
    sammy.be_awesome()
#gives the object Sammy the be_awesome method which outputs Sammy is being awesome
    stevie = Shark("Stevie")
#create object Stevie
    stevie.swim()
#gives the object stevie the swim method which outputs Stevie is swimming
    joseph = Shark("Joseph")
#create object Joseph
    joseph.be_awesome()
#gives the object joseph the be_awesome method which outputs Joseph is being awesome
    joseph.swim()
#gives the object joseph the swim method which outputs Joseph is swimming

if __name__ == "__main__":
  main()
    