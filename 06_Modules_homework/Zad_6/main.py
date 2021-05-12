import Testing_instance_generator as Ig

rand_instance = Ig.instance_generator()
print(f"Randomly generated instance: {rand_instance}")

max_seq = ''
repeated = []
temp_seq = []

for i in range(len(rand_instance) - 1):
    if rand_instance[i] == rand_instance[i + 1]:
        x = i
        while rand_instance[x] == rand_instance[x + 1]:
            temp_seq.append(rand_instance[x])
            x += 1
        temp_seq.append(rand_instance[x])
        if len(temp_seq) > len(max_seq):
            max_seq = ''.join(temp_seq)

        temp_seq = []

print(f"Longest seq: '{max_seq}' and has length of {len(max_seq)}")
