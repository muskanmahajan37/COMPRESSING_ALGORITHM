import zlib,sys,base64,time,os



f =open('temp.txt','rb')
text=f.read()
file_size=sys.getsizeof(text)
print("--------------------------")
print("file size is : ",file_size)
print("--------------------------")


compress = zlib.compress(text,9)
g = open('compressed.txt','wb')
g.write(compress)
g.close()
comp_size=sys.getsizeof('compressed.txt')
f.close()
print("compressed file is: ",comp_size)
print("-------------------------------")

if int(comp_size) >= int (file_size):
    os.remove("compressed.txt")
    print("inefficient compression removing the compressed file!!!")
    print("---------------------------------------------------------")
    compression_ratio = int(comp_size)/int(file_size)
    if compression_ratio > 1:
        print("compressed file increased in size")
        print("---------------------------------")

else:
    comp_ratio = int(comp_size)/int(file_size)
    print("compression ratio is : ",comp_ratio)
    print("-----------------------------------")
    h = open('compressed.txt','rb')
    decomp=h.read()
    decompress = zlib.decompress(decomp)
    i = open('decompressed.txt','wb')
    i.write(decompress)
    i.close()
    h.close()
    decomp_size=sys.getsizeof(decompress)
    print("decompressed file size is: ",decomp_size)
    print("-----------------------------------")
    if int(file_size) != int(decomp_size):
        print("original file size is not same as decompressed file!!!")
        print("-----------------------------------------------------")
        os.remove("decompressed.txt")