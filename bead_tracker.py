import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture
from argparse import ArgumentParser

# Takes an integer P, a float tau, a float delta, and a sequence of JPEG
# filenames as command-line arguments; identifies the beads in each JPEG
# image using BlobFinder; and writes out (one per line, formatted with 4
# decimal places to the right of decimal point) the radial distance that
# each bead moves from one frame to the next (assuming it is no more than
# delta).
def main():
    ap = ArgumentParser()
    ap.add_argument('P')

    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    pic = Picture(sys.argv[4])
    prevBeads = BlobFinder(pic, tau).getBeads(P)
    # for every frame:
    for i in sys.argv[5:]:
        currBeads = BlobFinder(Picture(i), tau).getBeads(P)
        # for every bead in that frame:
        for currBead in range(len(currBeads)):
            # intialize shortest_dist with largest possible dimension:
            shortest_dist = max([pic.width(), pic.height()])
            # search for currBead closest to prevBead:
            for v in range(min([len(currBeads), len(prevBeads)])):
                d = prevBeads[v].distanceTo(currBeads[currBead])
                if d < shortest_dist:
                    shortest_dist = d
            # confirm that displacement is within delta:
            if shortest_dist <= delta:
                # if yes, then show the distance:
                stdio.writef('%.4f\n', shortest_dist)

        stdio.writeln()
        prevBeads = currBeads

if __name__ == '__main__':
    main()
