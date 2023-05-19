import os
from bitStream import BitStream
from huffmanTree import HuffmanTree
from huffmanTree import HuffmanTree_Buffer


class Encoder:
    def __init__(self,block_size=1,Buffer = False):
        if not Buffer:
            self.tree = HuffmanTree(block_size)
        else:
            self.tree = HuffmanTree_Buffer(block_size)

    def encodeFile(self, fileName, outFileName):
        if not os.path.exists(fileName):
            print('File doesnt exist.')
            return
        readFile = open(fileName, 'rb')
        writeFile = BitStream(outFileName, 'wb')
        # the size of file
        writeFile.write('{0:032b}'.format(os.stat(fileName).st_size))
        while True:
            code = self.tree.encode(readFile)
            if not code:
                break
            writeFile.write(code)

        # self.tree.printTree()
        readFile.close()
        writeFile.close()

if __name__ == '__main__':
    encoder = Encoder()
    encoder.encodeFile('./test_txt.txt', './code_test.txt')
