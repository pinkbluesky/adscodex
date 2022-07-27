# Run in adscodex directory
import subprocess
import os
import time

data_path = os.path.expanduser('~') + "/32kfilerand"
prefix_path = os.path.expanduser('~') + "/testing/test"

# dna_path = os.path.expanduser('~') + "/dna.out" # + "/dna" + str(seed) + ".out"

def run(command):
    subprocess.run(command, shell=True) #, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def generate_data():
    run("dd if=/dev/urandom of={} bs=16k count=2".format(data_path))



def input_path(seed):
    return prefix_path + str(seed) + ".in"


def output_path(seed):
    return prefix_path + str(seed) + ".mfes"  # ie. ~/testing/test50.mfes


def run_mfes(seed):
    print("random seed {}".format(seed))
    # clear the file. run encoder
    run("> {}".format(input_path(seed)))
    print("go run encode\n")
    run("go run encode/main.go -tbl tbl -printfmt 1 -rndmz -rndseed {} {} >> {}".format(seed, data_path, input_path(seed)))
    print("mfes... beginning timer\n")
    start = time.time()
    run("mfes -material dna -multi {}".format(prefix_path + str(seed)))
    mfe_time = time.time() - start

    return mfe_time

    # print("reading from {}".format(output_path(seed)))
    # read the output file
    # with open(output_path(seed)) as fp:
        # for line in fp:
            # if line[0] != "%":
                # return float(line), mfe_time # return energy value and time



def main():

    run("echo running random seed tests...")

    seeds = [1, 10, 50]
    mfes = []
    mfe_times = []
    times = []

    for s in seeds:
        start = time.time()
        # mfe_energy, mfe_time = run_mfes(s)
        mfe_time = run_mfes(s)
        # mfes.append(mfe_energy)
        mfe_times.append(mfe_time)
        times.append(time.time() - start)
        
    print("seed, total time elasped\n")
        
    for i in range(len(seeds)):
        # print("seed {}: {} kcal/L\ntime elapsed: {} sec, mfe time elapsed; {} sec".format(seeds[i], mfes[i], times[i], mfe_times[i]))
        print("{} {}".format(seeds[i], times[i]))

if __name__ == "__main__":
    main()

