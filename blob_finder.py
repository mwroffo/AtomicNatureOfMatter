import luminance
import stdarray
import stdio
import sys
from blob import Blob
from picture import Picture

class BlobFinder:
    """
    A data type for identifying blobs in a picture.
    """
    # think of the blob like a 2D jagged matrix.

    def __init__(self, pic, tau):
        """
        Constructs a blob finder to find blobs in the picture pic, using
        a luminance threshold tau.
        """

        # Initialize an empty list for the blobs in pic.
        self._blobs = []

        # Create a 2D list of booleans called marked, having the same
        # dimensions as pic.
        marked = stdarray.create2D(pic.width(), pic.height(), False)

        # Enumerate the pixels of pic, and for each pixel (i, j):
        # 1. Create a Blob object called blob.
        # 2. Call _findBlob() with the right arguments.
        # 3. Add blob to _blobs if it has a non-zero mass.
        for i in range(pic.width()):
            for j in range(pic.height()):
                blob = Blob()
                self._findBlob(pic, tau, i, j, marked, blob)
                if blob.mass() > 0:
                    self._blobs.append(blob)

    def _findBlob(self, pic, tau, i, j, marked, blob):
        """
        Identifies a blob using depth-first search. The parameters are
        the picture (pic), luminance threshold (tau), pixel column (i),
        pixel row (j), 2D boolean matrix (marked), and the blob being
        identified (blob).
        """

        # Base case: return if pixel (i, j) is out of bounds, or if is
        # is marked, or if its luminance is less than tau.
        if i >= pic.width() or j >= pic.height() \
            or i < 0 or j < 0:
            return

        if marked[i][j]:
            return

        if luminance.luminance(pic.get(i, j)) < tau:
            return

        # Mark the pixel.
        marked[i][j] = True
        # Add the pixel to blob.
        blob.add(i, j)

        # Recursively call _findBlob() on the N, E, W, S pixels.
        self._findBlob(pic, tau, i, j + 1, marked, blob)  # N
        self._findBlob(pic, tau, i + 1, j, marked, blob)  # E
        self._findBlob(pic, tau, i - 1, j, marked, blob)  # W
        self._findBlob(pic, tau, i, j - 1, marked, blob)  # S

    def getBeads(self, P):
        """
        Returns a list of all beads with >= P pixels.
        """
        beads = []
        for i in range(len(self._blobs)):
            if self._blobs[i].mass() >= P:
                beads.append(self._blobs[i])
        return beads


# Takes an integer P, a float tau, and the name of a JPEG file as
# command-line arguments; writes out all of the beads with at least P
# pixels; and then writes out all of the blobs (beads with at least 1 pixel).
def _main():
    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    pic = Picture(sys.argv[3])
    # create the BlobFinder:
    Finder = BlobFinder(pic, tau)
    # print all the beads:
    stdio.writef('%d Beads:\n', len(Finder.getBeads(P)))
    for i in range(len(Finder.getBeads(P))):
        stdio.writeln(Finder.getBeads(P)[i])
    # print all the blobs:
    stdio.writef('%d Blobs:\n', len(Finder.getBeads(1)))
    for i in range(len(Finder.getBeads(1))):
        stdio.writeln(Finder.getBeads(1)[i])

if __name__ == '__main__':
    _main()
