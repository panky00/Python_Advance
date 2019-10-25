import test_argv
import sys



if __name__ == "__main__":
    input_file = sys.argv[1]
    print('input file is: %s' %input_file)
    output_file = sys.argv[2]
    print('output file is: %s' %output_file)
    test_argv.jsontocsv(input_file,output_file)