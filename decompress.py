from LZSS import LZ77_compressor
import sys


input_path = sys.argv[1]
output_path = 'decompressed.txt'
comp = LZ77_compressor()
comp.Decompress(input_path, output_path)