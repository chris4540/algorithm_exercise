import sys
import csv


def argparser():
    # Check for correct number of args
    if len(sys.argv) > 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    db_file = sys.argv[1]
    seq_file = sys.argv[2]
    return db_file, seq_file


def get_STR(seq, motifs):
    """
    Obtain the Short Tandem Repeats

    Args:
        seq (string): a sequence of DNA
        motifs (string): a peice of DNA pattern

    Return:
        a number of which the longest run of consecutive repeats the STR
        in the DNA sequence

    Example:
    >>> get_STR('AGATAGAT', 'AGAT')
    2
    >>> get_STR('AGATxxAGAT', 'AGAT')
    1
    >>> get_STR('xxAGATAGATxx', 'AGAT')
    2

    See also:
        https://isogg.org/wiki/Short_tandem_repeat
    """
    ret = 0

    i = 0
    while i < len(seq):
        if seq[i:i+len(motifs)] == motifs:
            consecutive_rep = 0
            # start checking consecutive repeats
            for j in range(i, len(seq), len(motifs)):
                if seq[j:j+len(motifs)] == motifs:
                    consecutive_rep += 1
                else:
                    break
            # ----------------------------------
            if consecutive_rep > ret:
                ret = consecutive_rep
                i = j+len(motifs)
        # For updated case, we go to the end of last matched pattern
        # Therefore, we have to step forward
        i += 1
    return ret


if __name__ == '__main__':
    pass
    # argument parse
    db_file, seq_file = argparser()

    # read the db and build db as dictionary
    db = dict()  # db[name][pattern] := freq
    with open(db_file, mode='r') as f:
        reader = csv.reader(f)
        header = None
        for row in reader:
            if header is None:
                header = row
                patterns = row[1:]
            else:
                name = row[0]
                db[name] = dict()
                for i, p in enumerate(patterns):
                    db[name][p] = int(row[i+1])
    # --------------------------------------------------
    # checking
    match_freq = {p: 0 for p in patterns}  # match_freq[pattern] = freq

    # you may implment byte-by-byte matching when having memory problem
    with open(seq_file, 'r') as f:
        seq = f.readline().rstrip()

    # For each of the STRs (from the first line of the CSV file),
    # your program should compute the longest run of consecutive repeats
    # of the STR in the DNA sequence to identify.
    for p in patterns:
        str_cnt = get_STR(seq, p)
        match_freq[p] = str_cnt
    # ------------------------------------
    # match frequecy
    for name, freqs in db.items():
        matched = True  # assume to be true
        # match pattern freq one-by-one, break if one pattern not right
        for p in patterns:
            if freqs[p] != match_freq[p]:
                matched = False
                break
        if matched:
            print(name)
            sys.exit(0)
    # -----------------------------------
    # if go to this stage, probably no matched
    print("No match")
