__author__="Chufan Xiao"

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter
def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(1,10)
    for eachNum in numbersWeHave:
        #print eachNum
        for furtherNum in numbersWeHave:
            # you could also literally add it *.1 and have it create
            # an actual float, but, since in the end we are going
            # to use it as a string, this way will work.
            print(str(eachNum)+'.'+str(furtherNum))
            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(furtherNum)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            print(eiarl)
            lineToWrite = str(eachNum)+'::'+eiarl+'\n'
            numberArrayExamples.write(lineToWrite)



#createExamples()
def recognizeNumber(filepath):
    match=[]
    loadExample=open("numArEx.txt","r").read()
    loadExample=loadExample.split("\n")

    testImage=Image.open(filepath)
    testImageArr=np.asarray(testImage)
    testImageArrList=testImageArr.tolist()
    testString=str(testImageArrList)
    for eachExample in loadExample:
        try:
            each_split=eachExample.split("::")
            each_num=each_split[0]
            each_pixels=each_split[1]

            eachPixel_testString=testString.split("],")
            each_piexl=each_pixels.split("],")

            i=0
            while i < len(each_piexl):
                curr_test=eachPixel_testString[i]
                curr_pixel=each_piexl[i]

                if curr_test==curr_pixel:
                    match.append(each_num)
                i+=1
        except Exception as e:
            print(str(e))

    print(match)
    print(Counter(match))
    counter=Counter(match)
    graphX=[]
    graphY=[]
    for item in counter:
        graphX.append(int(item))
        graphY.append(counter[item])
    result=Counter(match).most_common(1)[0][0]
    fig=plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3,colspan=4)

    ax1.imshow(testImageArr)
    print(graphX)
    print(graphY)
    ax2.bar(graphX,graphY,align="center")
    plt.ylim(400)
    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)
    plt.show()
    print(result)






if __name__=="__main__":
    createExamples()
    recognizeNumber("images/test.png")
