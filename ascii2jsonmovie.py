import codecs
jsonFile = open("starwars.json", "w", encoding='utf-8')
asciiFile = open("starwars.txt", "r")
asciiLines = asciiFile.readlines()
asciiFile.close()
lineCount = 0
jsonFile.write("[\n")
frame = []
for asciiLine in asciiLines:

    asciiLine = asciiLine.replace("\n", "").ljust(67, " ").replace(
        "\\", "\\\\").replace('"', '\\"')

    lineCount += 1
    if(lineCount == 1):
        frame.append('{\n')
        frame.append('\t"sleeptime":'+asciiLine.strip()+',\n')
    elif(lineCount < 14):
        frame.append('\t"line'+str(lineCount-1) +
                     '":"'+asciiLine+'",\n')
    else:
        frame.append('\t"line'+str(lineCount-1) +
                     '":"'+asciiLine+'"\n')
    if(lineCount == 14):
        frame.append('},\n')
        lineCount = 0
        jsonFile.writelines(frame)
        frame = []
frame = []
frame.append('{\n')
frame.append('\t"sleeptime":1,\n')
for i in range(1, 13):
    frame.append('\t"line'+str(i)+'":"",\n')
frame.append('\t"line13":""\n')
frame.append('}')
jsonFile.writelines(frame)
jsonFile.write("]\n")
