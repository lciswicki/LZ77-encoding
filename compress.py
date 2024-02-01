from LZSS import LZ77_compressor
import sys


input_path = sys.argv[1]
output_path = 'compressed.txt'
comp = LZ77_compressor()
comp.Compress(input_path, output_path)