from convertObjFuncs import *

inputFile = "model/test.obj"
outputFile = "convertedKeys/test.txt"
varName = "test"

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
    initializeArray(raw, "float")
    raw.append(1.0)       # -> [x, y, z, 1]

    arr.append(raw.copy())  #append array to vArr

  elif raw[0] == "vn":
    vnCount += 1
    arr = vnArr

    raw.remove(raw[0])
    initializeArray(raw, "float")
    raw.append(0)

    arr.append(raw.copy())  #append array to vnArr

  elif raw[0] == "f":
    arr = fArr
    raw.remove(raw[0])

    for i in range(len(raw)):      #for each "00//11"
      get = raw[i].split("//")    # get = ["00", "11"]
      raw[i] = get[0]             # replace "00//11" with "00"

      # newNormalArr.append(int(get[1]) - vnAccumulate - 1)
    
    initializeArray(raw, "int")          # replace "00" with 00

    # print(raw)

    #blender indices accumulate when there's a new object
    #the next two lines are for making the indices go back to 0 when there's a new key object
    # for i in range(len(raw)):
    #   raw[i] = raw[i] - vAccumulate - 1 

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
    # tempKey.append(newNormalArr.copy())

    keys.append(tempKey.copy())     #store current key in an array of keys


    tempKey.clear()
    vArr.clear()
    vnArr.clear()
    fArr.clear()

    print("appended")
    # newNormalArr.clear()

  else:
    continue

f.close()
# print(keys[0][2])

# print((keys[0][2]))
# keys.pop(0)

# print("in try: " + str(len(keys)))

# print(f'len of vertices: {len(keys[1][0])}')

# for key in keys:
#   print("key")
#   for array in key:
#     print("array")
#     for coord in key:
#       type = "coord"
#       # if coord == array[0]: type = "vertices:"
#       # elif coord == array[1]: type = "normals"
#       # elif coord == array[2]: type = "indices"
#       print(f"{type}:")
#       print(coord)
print(f'len in try: {len(keys)}')
fixNormals(keys)

# o = open(outputFile, "w")

# count = 0
# for key in keys:
#   # if key == keys[0]:
#   #   continue

#   for i in key:
#     type = ""

#     if i == key[0]:
#       type += "Vertices"
#     elif i == key[1]:
#       type += "Normals"
#     elif i == key[2]:
#       type += "Indices"
#     elif i == key[3]:
#       type += "NewNormals"

#     # o.write(f'var {varName}{type} = [\n')     # "var key#Type = ["
#     o.write(f'var {varName}{count}{type} = [\n')     # ex. "var black0Indices = ["

#     for group in i:                   
#       for val in range(len(group)):
#         if group == i[len(i)-1] and val == len(group)-1:
#           o.write(f'{group[val]}')                    # "val" if last element
#           continue 

#         o.write(f'{group[val]}, ')                    # else "val, "

#       o.write(f'\n') 

#     o.write(f'];')                              # ];

#     o.write(f'\n')
#   count += 1

# o.close()


# print(newNormalArr)
removeOFromObj(inputFile)