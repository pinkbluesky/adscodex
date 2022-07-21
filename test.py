# Run in adscodex directory
import subprocess
import os
import time

data_path = os.path.expanduser('~') + "/16kfilerand"
prefix_path = os.path.expanduser('~') + "/mfes/ads"

dna_path = os.path.expanduser('~') + "/dna.out" # + "/dna" + str(seed) + ".out"

def run(command):
    subprocess.run(command, shell=True) #, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def generate_data():
    run("dd if=/dev/urandom of={} bs=16k count=2".format(data_path))



def input_path():
    return prefix_path + ".in"


def output_path():
    return prefix_path + ".mfes"


def run_mfes(seed):
    # clear the file. run encoder
    run("> {}".format(dna_path))
    print("go run encode")
    run("go run encode/main.go -tbl tbl -printfmt 1 -rndmz -rndseed {} {} >> {}".format(seed, data_path, input_path()))
    print("mfes")
    run("mfes -material dna -multi {}".format(prefix_path))

    # read the output file
    with open(output_path()) as fp:
        for line in fp:
            if line[0] != "%":
                return float(line) # return the decimal value



def main():

    subprocess.run("echo running random seed tests...", shell=True)

    seeds = [50]
    mfes = []
    times = []

    for s in seeds:
        start = time.time()
        mfes.append(run_mfes(s))
        times.append(time.time() - start)
        
    for i in range(len(seeds)):
        print("seed {}: {} kcal/L, time elapsed: {} sec".format(seeds[i], mfes[i], times[i]))


if __name__ == "__main__":
    main()

