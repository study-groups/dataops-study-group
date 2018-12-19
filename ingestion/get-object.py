import sys
import time
id=0              # first token of each row is a an object id
prevId=0          # variable used to determine when id changes
index={}          # id:[startLine,endLine]
offset=0          # number of bytes from beginning of file
line_offset=[]    # ordered list of start of each line, in bytes from start
numOfObj=0        # many lines can have the same object id

class Names:
    startByte=3;
    numBytes=4;
    pass;

def idToOffset(id=13, indexfile="index.csv"):
  """Returns a tuple of offset and len in bytes."""
  with open(indexfile, 'r') as f:
    labels=f.readline().split(',');
    for i,line in enumerate(f):
      tokens=line.split(',')     # each line of comma separated file  id,start,end,byteoffset,bytelen
      if int(tokens[0])==id:
        f.close() 
        return (int(tokens[Names.startByte]), int(tokens[Names.numBytes]))
  f.close()

def offsetToText(posAndLen):
    """Takes a tuple of position and length in bytes."""
    with open("./test_set.csv", 'r') as f:
        f.seek(posAndLen[0])
        data = f.read(posAndLen[1])
    f.close()
    return data

def textToList(data):
    """Takes csv data with newlines and returns array of strings via split."""
    samples=data.split('\n');
    return samples;

# example getting first object
obj14=textToList(offsetToText(idToOffset(14)))
# example getting last object
start=time.time()
lastObj=textToList(offsetToText(idToOffset(104853738)))
print(lastObj)
end=time.time()
print("Took {0: .2f}s to extract last object samples.".format(end-start))
