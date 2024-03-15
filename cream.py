import subprocess

def test():
    type = input("Enter test-type\nTests supported: mult, add, divide\n->")
    if type == "mult":
        file_name = "source\\true_gen_float_mult_tests.tsv"
    elif type == "add":
        file_name = "source\\true_gen_float_+-_tests.tsv"
    elif type == "divide":
        file_name = "source\\true_gen_float_div_tests.tsv"
    else:
        print("chleni?")
        return
    
    path = input("ENTER PATH TO EXE FILE:\n->") #change to your path
    test_f = open(file_name, "r")
    tests = test_f.readlines()

    count = 0
    passed = 0
    for test_id in range(0, len(tests)):
        arg = tests[test_id][:-1]
        arg = arg.split(',')
        if (len(arg) == 0):
            continue
        res = arg[-1]
        arg = arg[0].split()
        arg = [path] + arg
        output = subprocess.check_output(arg).decode("utf-8")
        count += 1
        if res.strip('\r\n ') != output.strip('\r\n '):
            print("FAILED test: ")
            for i in range(1, len(arg)):
                print(arg[i], end=" ")
            print("Expected:", res, end=" ")
            print("Actual:", output)
        else:
            passed += 1
            print("PASSED")

        if (count % 10000 == 0):
            print(str(count) + " tests pass")
    print(str(passed) + "/" + str(count) + "PASSED")
test()