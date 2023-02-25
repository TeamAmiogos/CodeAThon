import sys

def SAI():
    return "Hello from Python!"

if __name__ == '__main__':
    function_name = sys.argv[1]
    if function_name == 'SAI':
        result = SAI()
        print(result)
