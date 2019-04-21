# coding: utf-8

'''
luci project final codes

nithin pb
Cochin University of Sciecne and Technolgy
department of electronics

fabric.py

fabric motion control for servos
'''



import lucisight
import bezerCurver
import luciserial


'''
class fabrik:

    def __init__(self):
        self.fabbez=0.0
        self.previosx=90
        self.previosy=30
        self.previosy1=30
        self.previosh=30
        self.ff=0
        print("init")
        
    def update_value(self,xaxis,yaxis,lenx):
        self.xaxis=xaxis
        self.yaxis=yaxis
        self.lenx=lenx
        fabbez=bezerCurver.bezer(self.xaxis,self.yaxis)
        self.fabbez=fabbez

    def fablength(self): # length approximating function
        switcher = { 
        200: 0,
        199: 1,
        198: 1,
        197: 2,
        196: 3,
        195: 3,
        194: 4,
        193: 4,
        192: 5,
        191: 6,
        190: 6,
        189: 7,
        188: 7,
        187: 8,
        186: 9,
        185: 9,
        184: 10,
        183: 10,
        182: 11,
        181: 12,
        180: 12,
        179: 13,
        178: 13,
        177: 14,
        176: 15,
        175: 15,
        174: 16,
        173: 16,
        172: 17,
        171: 18,
        170: 18,
        169: 19,
        168: 19,
        167: 20,
        166: 21,
        165: 21,
        164: 22,
        163: 22,
        162: 23,
        161: 24,
        160: 24,
        159: 25,
        158: 25,
        157: 26,
        156: 27,
        155: 27,
        154: 28,
        153: 28,
        152: 29,
        151: 30,
        150: 30,
        149: 31,
        148: 31,
        147: 32,
        146: 33,
        145: 33,
        144: 34,
        143: 34,
        142: 35,
        141: 36,
        140: 36,
        139: 37,
        138: 37,
        137: 38,
        136: 39,
        135: 39,
        134: 40,
        133: 40,
        132: 41,
        131: 42,
        130: 42,
        129: 43,
        128: 43,
        127: 44,
        126: 45,
        125: 45,
        124: 46,
        123: 46,
        122: 47,
        121: 48,
        120: 48,
        119: 49,
        118: 49,
        117: 50,
        116: 51,
        115: 51,
        114: 52,
        113: 52,
        112: 53,
        111: 54,
        110: 54,
        109: 55,
        108: 55,
        107: 56,
        106: 57,
        105: 57,
        104: 58,
        103: 58,
        102: 59,
        101: 60,
        100: 60,
        99: 61,
        98: 61,
        97: 62,
        96: 63,
        95: 63,
        94: 64,
        93: 64,
        92: 65,
        91: 66,
        90: 66,
        89: 67,
        88: 67,
        87: 68,
        86: 69,
        85: 69,
        84: 70,
        83: 70,
        82: 71,
        81: 72,
        80: 72,
        79: 73,
        78: 73,
        77: 74,
        76: 75,
        75: 75,
        74: 76,
        73: 76,
        72: 77,
        71: 78,
        70: 78,
        69: 79,
        68: 79,
        67: 80,
        66: 81,
        65: 81,
        64: 82,
        63: 82,
        62: 83,
        61: 84,
        60: 84,
        59: 85,
        58: 85,
        57: 86,
        56: 87,
        55: 87,
        54: 88,
        53: 88,
        52: 89,
        51: 90,
        50: 90,
        49: 91,
        48: 91,
        47: 92,
        46: 93,
        45: 93,
        44: 94,
        43: 94,
        42: 95,
        41: 96,
        40: 96,
        39: 97,
        38: 97,
        37: 98,
        36: 99,
        35: 99,
        34: 100,
        33: 100,
        32: 101,
        31: 102,
        30: 102,
        29: 103,
        28: 103,
        27: 104,
        26: 105,
        25: 105,
        24: 106,
        23: 106,
        22: 107,
        21: 108,
        20: 108,
        19: 109,
        18: 109,
        17: 110,
        16: 111,
        15: 111,
        14: 112,
        13: 112,
        12: 113,
        11: 114,
        10: 114,
        9: 115,
        8: 115,
        7: 116,
        6: 117,
        5: 117,
        4: 118,
        3: 118,
        2: 119,
        1: 120,
        } 
        return switcher.get(self.lenx, 70) 

    def fabfull(self):
        #the fabric forward and backward iterations goes here!!!
        Position=self.fablength()
        #print(self.value)
        print(str(Position)+"cm")
        print("[INFO] data sent form fabrik module.")
        #access  x and y values like this self.fabbez[0],self.fabbez[1]
        if (self.fabbez[0]>160):
            newXpos=self.previosx-2
        elif(self.fabbez[0]<160):
            newXpos=self.previosx+2
        if(self.fabbez[1]>120):
            newYposition=self.previosy+2
            newYposition1=self.previosy1+1
        elif(self.fabbez[1]<120):
            newYposition=self.previosy-2
            newYposition1=self.previosy1-1
        if(Position>80):
            newHpos=self.previosh+2
        elif(Position<82):
            newHpos=self.previosh-2

        ff=0


        try:
            previosx=newXpos
            previosy=newYposition
            previosy1=newYposition1
            previosh=newHpos
            data="X{0:d}Y{1:d}H{2:d}L{3:d}F{4:d}".format(newXpos, newYposition, newYposition1, newHpos, ff)
            ff=ff+1
            print(previosx,previosy,previosy1,previosh)
            print(data)
            luciserial.servorotate2(data)
        except:
            print("[INFO] error in communication ")'''


def fablength(lenx): # length approximating function
        switcher = { 
        200: 0,
        199: 1,
        198: 1,
        197: 2,
        196: 3,
        195: 3,
        194: 4,
        193: 4,
        192: 5,
        191: 6,
        190: 6,
        189: 7,
        188: 7,
        187: 8,
        186: 9,
        185: 9,
        184: 10,
        183: 10,
        182: 11,
        181: 12,
        180: 12,
        179: 13,
        178: 13,
        177: 14,
        176: 15,
        175: 15,
        174: 16,
        173: 16,
        172: 17,
        171: 18,
        170: 18,
        169: 19,
        168: 19,
        167: 20,
        166: 21,
        165: 21,
        164: 22,
        163: 22,
        162: 23,
        161: 24,
        160: 24,
        159: 25,
        158: 25,
        157: 26,
        156: 27,
        155: 27,
        154: 28,
        153: 28,
        152: 29,
        151: 30,
        150: 30,
        149: 31,
        148: 31,
        147: 32,
        146: 33,
        145: 33,
        144: 34,
        143: 34,
        142: 35,
        141: 36,
        140: 36,
        139: 37,
        138: 37,
        137: 38,
        136: 39,
        135: 39,
        134: 40,
        133: 40,
        132: 41,
        131: 42,
        130: 42,
        129: 43,
        128: 43,
        127: 44,
        126: 45,
        125: 45,
        124: 46,
        123: 46,
        122: 47,
        121: 48,
        120: 48,
        119: 49,
        118: 49,
        117: 50,
        116: 51,
        115: 51,
        114: 52,
        113: 52,
        112: 53,
        111: 54,
        110: 54,
        109: 55,
        108: 55,
        107: 56,
        106: 57,
        105: 57,
        104: 58,
        103: 58,
        102: 59,
        101: 60,
        100: 60,
        99: 61,
        98: 61,
        97: 62,
        96: 63,
        95: 63,
        94: 64,
        93: 64,
        92: 65,
        91: 66,
        90: 66,
        89: 67,
        88: 67,
        87: 68,
        86: 69,
        85: 69,
        84: 70,
        83: 70,
        82: 71,
        81: 72,
        80: 72,
        79: 73,
        78: 73,
        77: 74,
        76: 75,
        75: 75,
        74: 76,
        73: 76,
        72: 77,
        71: 78,
        70: 78,
        69: 79,
        68: 79,
        67: 80,
        66: 81,
        65: 81,
        64: 82,
        63: 82,
        62: 83,
        61: 84,
        60: 84,
        59: 85,
        58: 85,
        57: 86,
        56: 87,
        55: 87,
        54: 88,
        53: 88,
        52: 89,
        51: 90,
        50: 90,
        49: 91,
        48: 91,
        47: 92,
        46: 93,
        45: 93,
        44: 94,
        43: 94,
        42: 95,
        41: 96,
        40: 96,
        39: 97,
        38: 97,
        37: 98,
        36: 99,
        35: 99,
        34: 100,
        33: 100,
        32: 101,
        31: 102,
        30: 102,
        29: 103,
        28: 103,
        27: 104,
        26: 105,
        25: 105,
        24: 106,
        23: 106,
        22: 107,
        21: 108,
        20: 108,
        19: 109,
        18: 109,
        17: 110,
        16: 111,
        15: 111,
        14: 112,
        13: 112,
        12: 113,
        11: 114,
        10: 114,
        9: 115,
        8: 115,
        7: 116,
        6: 117,
        5: 117,
        4: 118,
        3: 118,
        2: 119,
        1: 120,
        } 
        return switcher.get(lenx, 70)
def updateValues(xaxis,yaxis,distance):
    global previosx,previosy,previosy1,previosh,xprevios
    global fabbeznew
    fabbez=bezerCurver.bezer(xaxis,yaxis)
        #the fabric forward and backward iterations goes here!!!
    Position=distance
    #print(self.value)
    print(str(distance)+"cm")
    print("[INFO] data sent form fabrik module.")
    #access  x and y values like this self.fabbez[0],self.fabbez[1]

    xcurrent=fabbez[0]
    ycurrent=fabbez[1]
    distance




    if((xcurrent-3)<xprevios):
        #print("bigger")
        xprevios=xcurrent
    elif((xcurrent+3)>xprevios):
        #print("smaller")
        xprevios=xcurrent
    elif(xcurrent==xprevios):
        #print("equal")
        xprevios=xcurrent
    '''if (fabbez[0]>160):
        if (fabbeznew!=fabbez[0]):
            newXpos=previosx-2
        else:
            newXpos=previosx
        fabbeznew=fabbez[0]
    elif(fabbez[0]<160):
        if (fabbeznew!=fabbez[0]):
            newXpos=previosx+2
        else:
            newXpos=previosx
        fabbeznew=fabbez[0]
    if(fabbez[1]>120):
        if (fabbeznew!=fabbez[0]):
            newYposition=previosy+2
            newYposition1=previosy1+1
        else:
            newYposition=previosy
            newYposition1=previosy1
        fabbeznew=fabbez[1]
    elif(fabbez[1]<120):
        if (fabbeznew!=fabbez[0]):
            newYposition=previosy-2
            newYposition1=previosy1-1
        else:
            newYposition=previosy
            newYposition1=previosy1
        fabbeznew=fabbez[0]
        
    if(Position>80):
        newHpos=previosh+2
    elif(Position<82):
        newHpos=previosh-2
    ff=0
    try:
        previosx=newXpos
        previosy=newYposition
        previosy1=newYposition1
        previosh=newHpos
        data="X{0:d}Y{1:d}H{2:d}L{3:d}F{4:d}".format(newXpos, newYposition, newYposition1, newHpos, ff)
        ff=ff+1
        luciserial.servorotate2(data)
    except:
        pass'''
    print(previosx,previosy,previosy1,previosh)






def values(startX,startY,endX,endY):
    xmid=(endX-startX)/2
    ymid=(endY-startY)/2

    lenx=endX-startX
    print(lenx)
    leny=endY-startY
    xaxis=xmid+startX
    yaxis=ymid+startY
    distance=fablength(abs(lenx))
    #sent values to class 
    updateValues(xaxis, yaxis, distance)

def main():
    print("main")

if __name__=='__main__':
    main()

#fab=fabrik()
print("herre")
global previosx, previosy, previosy1, previosh, ff, fabbeznew, xprevios
previosx=90
previosy=30
previosy1=30
previosh=0
fabbeznew=0
xprevios=90