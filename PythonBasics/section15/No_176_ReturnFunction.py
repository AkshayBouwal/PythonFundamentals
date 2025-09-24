
def Outer():

    def Inner():
        print("Hello To Inner")

    return Inner

if __name__ == "__main__":

     f= Outer()
     f()

