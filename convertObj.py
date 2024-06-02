
import os

def initializeArray(arr, ):  # replace ["00", "00", "00"] to [00, 00, 00]
  for i in range(len(arr)):
    arr[i] = float(arr[i])

def makeNewNormals(newArr, oldArr, count):
  for i in range(len(newArr)):
    for j in range(3):
      #if count == 0: print(newArr[i][j], end=" -> ")
      newArr[i][j] = oldArr[newArr[i][j]].copy()
      #if count == 0: print(newArr[i][j])
      

def appendOToObj(filename):
  f = open(filename, "a")
  f.write("\no")
  f.close()

def removeOFromObj(filename): #code taken from https://stackoverflow.com/questions/1877999/delete-final-line-in-file-with-python
  with open(filename, "r+", encoding = "utf-8") as file:

    # Move the pointer (similar to a cursor in a text editor) to the end of the file
    file.seek(0, os.SEEK_END)

    # This code means the following code skips the very last character in the file -
    # i.e. in the case the last line is null we delete the last line
    # and the penultimate one
    pos = file.tell() - 1

    # Read each character in the file one at a time from the penultimate
    # character going backwards, searching for a newline character
    # If we find a new line, exit the search
    while pos > 0 and file.read(1) != "\n":
        pos -= 1
        file.seek(pos, os.SEEK_SET)

    # So long as we're not at the start of the file, delete all the characters ahead
    # of this position
    if pos > 0:
        file.seek(pos, os.SEEK_SET)
        file.truncate()

inputFile = "model/white-keys-3 copy.obj"
outputFile = "convertedKeys/test.txt"
varName = "whitekey"

appendOToObj(inputFile)

f = open(inputFile, "r")

keys = []

tempKey = []

vArr = []
vnArr = []
fArr = []
newNormalArr = []

vAccumulate = 0
vCount = 0
vnAccumulate = 0
vnCount = 0

for line in f:
  raw = line.strip().split(" ")

  arr = vArr


  if raw[0] == "v":     # store the vertices of a key in vArr
    vCount += 1     # count the total number of vertices
    arr = vArr

    raw.remove(raw[0])    # remove "v"
    initializeArray(raw)
    raw.append(1.0)       # -> [x, y, z, 1]

    arr.append(raw.copy())  #append array to vArr

  elif raw[0] == "vn":
    vnCount += 1
    arr = vnArr

    raw.remove(raw[0])
    initializeArray(raw)
    raw.append(0)

    arr.append(raw.copy())  #append array to vnArr

  elif raw[0] == "f":
    arr = fArr
    raw.remove(raw[0])
    vnormArr = []

    for i in range(len(raw)):      #for each "00//11"
      get = raw[i].split("//")    # get = ["00", "11"]
      raw[i] = get[0]             # replace "00//11" with "00"

      vnormArr.append(int(get[1]) - vnAccumulate - 1)

    newNormalArr.append(vnormArr.copy())
    vnormArr.clear()

    initializeArray(raw)          # replace "00" with 00

    #blender indices accumulate when there's a new object
    #the next two lines are for making the indices go back to 0 when there's a new key object
    for i in range(len(raw)):
      raw[i] = raw[i] - vAccumulate - 1 

    arr.append(raw.copy())  # append to fArr

  elif raw[0] == "o":
    vAccumulate += vCount   #add the vertice counter to the accumulator
    vCount = 0      # reset the vertice counter (because new key)
    vnAccumulate += vnCount
    vnCount = 0

    # makeNewNormals(newNormalArr, vnArr)

    tempKey.append(vArr.copy())     #values of one key
    tempKey.append(vnArr.copy())
    tempKey.append(fArr.copy())
    tempKey.append(newNormalArr.copy())

    keys.append(tempKey.copy())     #store current key in an array of keys

    tempKey.clear()
    vArr.clear()
    vnArr.clear()
    fArr.clear()
    newNormalArr.clear()

  else:
    continue

# for i in keys[1]:
#   for j in i:
#     print(j, end=",  ")
#   print("\n\n")

for key in keys:
  #duplicate shared vertices
  lookuptb = {}
  normalsfinal = []

  # 0 = vertices 1 = normals 2 = vertex indices 3 = normal indices 
  if (len(key[2]) == len(key[3])):
    for i in range(len(key[2])):
      for j in range(3):
        v = key[2][i][j]
        n = key[3][i][j]
        pair = [v,n]

        if v not in lookuptb:
          lookuptb[v] = n
          #print("lookuptb[",v,",",n,"] = ", key[1][n])
        else:
          #print(pair)
          key[0].append(key[0][int(v)].copy())
          newV = len(key[0])-1
          key[2][i][j] = newV
          #print(v," -> ",newV," = ",key[2][i][j])
          lookuptb[newV] = n

  numvert = len(key[0]) #for every vertex
  for i in range(numvert):
    #print(i,":",lookuptb[i], end=" >>> ")  
    normalsfinal.append(key[1][lookuptb[i]])  #append equivalent normal from lookuptable
    #print(normalsfinal[i])

  key[3] = normalsfinal

o = open(outputFile, "w")

count = 0
for key in keys:
  if key == keys[0]:
    continue

  for i in key:
    type = ""

    if i == key[0]:
      type += "Vertices"
    elif i == key[1]:
      type += "Normals"
    elif i == key[2]:
      type += "Indices"
    elif i == key[3]:
      type += "NewNormals"

    # o.write(f'var {varName}{type} = [\n')     # "var key#Type = ["
    o.write(f'var {varName}{count}{type} = [\n')     # ex. "var black0Indices = ["

    for group in i:                   
      for val in range(len(group)):
        if group == i[len(i)-1] and val == len(group)-1:
          o.write(f'{group[val]}')                    # "val" if last element
          continue 

        o.write(f'{group[val]}, ')                    # else "val, "

      o.write(f'\n') 

    o.write(f'];')                              # ];

    o.write(f'\n')
  count += 1

o.close()

f.close()

# print(newNormalArr)
removeOFromObj(inputFile)