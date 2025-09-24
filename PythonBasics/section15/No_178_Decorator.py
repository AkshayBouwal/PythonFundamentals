def get_counter(f):

    def counter():
        print("+" * 10)
        f()
        print("+" * 10)

    return counter

@get_counter
def display():
    print("Welcome")

if __name__ == "__main__":

    # c1 = get_counter(display)
    # c1()

    # display = get_counter(display)
    # display()

    display()
