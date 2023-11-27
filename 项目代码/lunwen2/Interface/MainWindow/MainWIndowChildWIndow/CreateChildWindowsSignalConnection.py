# import os
import sys
# sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "…/")))
sys.path.append(r'D:\pycharxiangmu\lunwen2\LANscanning')
import MainFile
class ChildSignalConnection():
    def CSCsearch(self):
        return self.searchAction.triggered.connect(MainFile.StartSearch)
# def ceshi():
#     print(os.path.abspath(os.path.join(os.getcwd(), "…/")))
#
# if __name__ == '__main__':
#     ceshi()