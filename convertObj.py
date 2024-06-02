from convertObjFuncs import *

inputFile = "model/buttons.obj"
outputFile = "convertedKeys/buttons.txt"
varName = "button"

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

    for i in range(len(raw)):      #for each "00//11"
      get = raw[i].split("//")    # get = ["00", "11"]
      raw[i] = get[0]             # replace "00//11" with "00"

      # newNormalArr.append(int(get[1]) - vnAccumulate - 1)
    
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
    # tempKey.append(newNormalArr.copy())

    keys.append(tempKey.copy())     #store current key in an array of keys

    tempKey.clear()
    vArr.clear()
    vnArr.clear()
    fArr.clear()
    # newNormalArr.clear()

  else:
    continue

f.close()

keys.pop(0)

fixNormals(keys)

# o = open(outputFile, "w")

# count = 0
# for key in keys:
#   if key == keys[0]:
#     continue

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