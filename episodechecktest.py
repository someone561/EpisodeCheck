import unittest
import episodecheck


class Test(unittest.TestCase):


    def testFileNameParse(self):
        p1 = episodecheck.Finder(["ABC S03E1.avi"]);
        self.assertEqual(p1.Missing, []);
        p2 = episodecheck.Finder(["ABC S03E01.avi"]);
        self.assertEqual(p2.Missing, []);
        p3 = episodecheck.Finder(["ABC S03E01-02.avi"]);
        self.assertEqual(p3.Missing, []);        
        p4 = episodecheck.Finder(["ABC S03E01-02.avi", "ABC S03E05.avi"]);
        self.assertEqual(p4.Missing, [3,4]);
        p5 = episodecheck.Finder(["ABC S03E10.avi"]);
        self.assertEqual(p5.Missing, [1,2,3,4,5,6,7,8,9]);

if __name__ == "__main__":
    unittest.main()