def triple(n):
    return n * 3

def square(n):
    return n ** 2

def main():
    for i in range(1, 11):
        #if square(i) > triple(i):
           # break
        print(f'triple({i})=={triple(i)} square({i})=={square(i)}')

if __name__ == "__main__":
    main()
