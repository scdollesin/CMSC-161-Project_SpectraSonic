import os
from math import sqrt

VERTICES = 0
NORMALS = 1
INDICES = 2

def initializeArray(arr, toWhat):  # replace ["00", "00", "00"] to [00, 00, 00]
  if toWhat == "float":
    for i in range(len(arr)):
      arr[i] = float(arr[i])
  elif toWhat == "int":
    for i in range(len(arr)):
      arr[i] = int(arr[i])
    

def makeNewNormals(newArr, oldArr):
  for i in range(len(newArr)):
    newArr[i] = oldArr[newArr[i]].copy()

def appendOToObj(filename):
  f = open(filename, "a")
  f.write("o")
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

def vectorSubtraction(p0, p1):
  arr = []
  arr.append(p1[0]-p0[0])
  arr.append(p1[1]-p0[1])
  arr.append(p1[2]-p0[2])

  return(arr.copy())

def vectorCrossProduct(v1, v2):
  arr = []
  arr.append(v1[1]*v2[2] - v2[1]*v1[2])
  arr.append(v1[2]*v2[0] - v2[2]*v1[0])
  arr.append(v1[0]*v2[1] - v2[0]*v1[1])

  return(arr.copy())

def computeNormal(triangle):
  p0 = triangle[0]
  p1 = triangle[1]
  p2 = triangle[2]

  v1 = vectorSubtraction(p0, p1)
  v2 = vectorSubtraction(p0,p2)


  N = vectorCrossProduct(v1,v2)
  print(f'v1: {v1}, v2: {v2}, N: {N}')
  length = sqrt(N[0]**2 + N[1]**2 + N[2]**2)

  N[0] = N[0]/length
  N[1] = N[1]/length
  N[2] = N[2]/length

  return N


# di gumagana huhu
def fixNormals(keys):
  print("in fix")
  # for key in keys:
  #   if key == key[0]:
  #     continue
  # keys = container
  # key = isang key
  # key[n] = vertices/normals/indices
  # key[n][n] = (x,y,z)
  # key[n][n][n] = x|y|z

  normalsDict = {}
  normalArray = []
  allN = []

  print(f'len in fix: {len(keys)}')

  for key in keys:
    for indexGroup in key[INDICES]:
      # print(indexGroup[0])    //indices use as index for VERTICES
      # print(key[VERTICES][indexGroup[0]])
      # print(key[VERTICES][indexGroup[1]])
      # print(key[VERTICES][indexGroup[2]])


      # tempN = (computeNormal([key[VERTICES][indexGroup[0]], key[VERTICES][indexGroup[1]], key[VERTICES][indexGroup[2]] ]))

      # if indexGroup[0] in normalsDict.keys():
      #   if normalsDict[indexGroup[0]] != tempN:
      #     #duplicate in VERTICES

      #     #update the index in INDICES

      #     #save in dict with new index

      #     pass
      # else:
      #   normalsDict[indexGroup[0]] = tempN
          
      tempN = (computeNormal([key[VERTICES][indexGroup[1]], key[VERTICES][indexGroup[2]], key[VERTICES][indexGroup[0]] ]))

      print(f'{indexGroup[0]}, {indexGroup[1]},{indexGroup[2]}')
      print(f'{indexGroup[1]}: {tempN}')

      # if indexGroup[1] in normalsDict.keys():
      #   if normalsDict[indexGroup[1]] != tempN:
      #     #duplicate in VERTICES

      #     #update the index in INDICES

      #     #save in dict with new index

      #     pass
      # else:
      #   normalsDict[indexGroup[1]] = tempN

      # tempN = (computeNormal([key[VERTICES][indexGroup[2]], key[VERTICES][indexGroup[0]], key[VERTICES][indexGroup[1]] ]))

      # if indexGroup[2] in normalsDict.keys():
      #   if normalsDict[indexGroup[2]] != tempN:
      #     #duplicate in VERTICES

      #     #update the index in INDICES

      #     #save in dict with new index

      #     pass
      # else:
      #   normalsDict[indexGroup[2]] = tempN
      # print(f'first coord = {key[VERTICES][coord[0]]}')
      # tempN = computeNormal(key[VERTICES][coord[0]])

  print(normalsDict)
  # for i in range(len(key[INDICES])-1):
  #   vIndices = key[INDICES][i]
  #   currTriangle = []
    