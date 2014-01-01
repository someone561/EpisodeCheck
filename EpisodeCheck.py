import sys
import os

from tvnamer import tvnamer_exceptions, utils

class Finder(object):
    def __init__(self, filenames):
        eps = set()
        for f in filenames:
            try:
                fp = utils.FileParser(f);
                ei = fp.parse();
                for e in ei.episodenumbers:
                    eps.add(e); 
            except tvnamer_exceptions.InvalidFilename:
                # Ignore invalid filenames in directory
                pass
        
        full_set = set(xrange(1, max(eps)))
        self.Missing = sorted(full_set - eps)

if __name__ == "__main__":    
    finder = Finder(os.listdir(sys.argv[1]));
    missing = finder.Missing
    
    print missing;