def read(sample):
    with open('samples/' + str(sample), 'r') as file:
        labels = []
        seismograms = []

        for line in file:
            parts = line.strip().split(' - ')

            label = int(parts[1])
            labels.append(label)

            seismogram = [int(x) for x in parts[0].strip('[]').split(', ')]
            seismograms.append(seismogram)

        return [seismograms, labels]