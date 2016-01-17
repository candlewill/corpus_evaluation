import csv


def load_CVAT(sigma=1):
    texts, valence, arousal = [], [], []
    V_ratings=dict()
    A_ratings=dict()
    with open('./resources/full_ratings.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        for line in reader:
            key = line[0]       # id
            v = float(line[2])     # valence
            a = float(line[3])     # arousal


    return texts, valence, arousal


if __name__=='__main__':

    load_CVAT(sigma = 1)
