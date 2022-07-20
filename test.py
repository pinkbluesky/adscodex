# Run in adscodex directory
import subprocess
import os

data_path = os.path.expanduser('~') + "/1kfilerand"
prefix_path = os.path.expanduser('~') + "/mfes/ads"

def dna_path(seed):
    # return a path to the encoded dna file that includes the random seed used
    return os.path.expanduser('~') + "/dna" + str(seed) + ".out"

def run(command):
    subprocess.run(command, shell=True) #, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def generate_data():
    run("dd if=/dev/urandom of={} bs=16k count=2".format(data_path))



def input_path():
    return prefix_path + ".in"


def output_path():
    return prefix_path + ".mfes"


def run_mfes(seed):
    print(dna_path(seed) + "\n")
    # clear the file. run encoder
    run("> {}".format(dna_path(seed)))
    run("go run encode/main.go -tbl tbl -printfmt 1 -rndseed {} {} >> {}".format(seed, data_path, dna_path(seed)))
    run("mv {} {}".format(dna_path(seed), input_path())) # copy output file into suitable location
    run("mfes -material dna -multi {}".format(prefix_path))

    # read the output file
    with open(output_path()) as fp:
        for line in fp:
            if line[0] != "%":
                return float(line) # return the decimal value



def main():

    subprocess.run("echo running random seed tests...", shell=True)

    seeds = [50, 1111]
    mfes = []

    for s in seeds:
        mfes.append(run_mfes(s))
        
    for i in range(len(seeds)):
        print("seed {}: {} kcal/L".format(seeds[i], mfes[i]))


if __name__ == "__main__":
    main()

