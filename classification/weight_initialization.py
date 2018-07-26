# Read and return the weights produced by training.py for the X matching synapses
def learned_weights_x():
    ans = []
    with open('weights.txt', 'r') as weight_file:
        lines = weight_file.readlines()
        for i in lines[0].split('\t'):
            ans.append(float(i))
    return ans

# Read and return the weights produced by training.py for the O matching synapses
def learned_weights_o():
    ans = []

    with open('weights.txt', 'r') as weight_file:
        lines = weight_file.readlines()
        for i in lines[1].split('\t'):
            ans.append(float(i))
    return ans

def learned_weights_synapse(id):
    ans = []
    with open('weights.txt', 'r') as weight_file:
        lines = weight_file.readlines()
        if (len(lines) <= id):
            return ans
        for i in lines[id].split('\t'):
            ans.append(float(i))
    return ans

# Just show that we read the weights and processed them into a sequence to feed to the classification
if __name__ == '__main__':
    a = learned_weights_x()
    print(a)
