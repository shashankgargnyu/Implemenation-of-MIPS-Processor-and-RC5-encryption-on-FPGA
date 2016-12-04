import sys


def get_hex(value):
    str_init = "00000000"
    hex_ins = str_init + value
    return hex_ins[-8:]


if __name__ == '__main__':

    if sys.argv.__len__() != 3:
        raise ValueError("Please provide valid input/output filename")

    else:

        read_file = sys.argv[1]
        write_file = sys.argv[2]
        read_from = open(read_file)
        write_to = open(write_file, 'w')
        ins_num = 0
        print "Enter 1 for hex or 2 for binary : "
        x = raw_input()
        print x
        if x == '1':

            for f in read_from:
                ins_mem = ""
                ins_hex=""
                ins = f.split('\n')[0]
                ins_num += 1

                if f == '\n' or f == ' ':
                    ins_mem = "X\"00000000\","
                    print ins_num, ins_mem
                    write_to.write(ins_mem)

                else:
                    ins_hex = get_hex(format(int(ins, 2), 'x'))
                    ins_mem += "X\"" + ins_hex + "\","
                    if ins_num % 7 == 0:
                        ins_mem += "\n"

                    write_to.write(ins_mem)
                    print ins_num, ins_mem

        elif x == '2':
            for f in read_from:
                ins_mem = ""
                ins = f.split('\n')[0]
                ins_num += 1

                if f == '\n' or f == ' ':
                    ins_mem = "\"00000000000000000000000000000000\","
                    print ins_num, ins_mem
                    write_to.write(ins_mem)

                else:
                    ins_mem += "\"" + ins + "\","
                    if ins_num % 3 == 0:
                        ins_mem += "\n"

                    write_to.write(ins_mem)
                    print ins_num, ins_mem
        else:
            print "Please Enter valid input"

    read_from.close()
    write_to.close()