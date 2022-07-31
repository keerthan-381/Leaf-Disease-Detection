import imagehash
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageOps
from PIL import ImageChops
import cv2
from matplotlib import pyplot as plt

print ("                                                  Welcome")
print("                                  !!!Welcome to leaf disease check!!!")

def main_ho(x):
    if(x==1):
        showimg()
        
    elif(x==2):
        compareeucl()
        
    elif(x==3):
        compareimpro()
        
    else:
        print("Please check your input")

def showimg():
    print("DO you want to see the leaves???")
    print("1. Yes")
    print("2. No")
    ni = int(input("Please enter your choice"))
    if(ni == 1):
        print("1. Leaf 1")
        print("2. Leaf 2")
        print("3. Leaf 1 as well as Leaf 2")
        
        nip = int(input("Enter the Leaf number you want to see "))
        
        if(nip == 1):
            Img1 = Image.open("HealthyLeaf.jpg")
            Img1.show()
            
        elif(nip == 2):
            Img2 = Image.open("LeafD.jpg")
            Img2.show()
            
        elif(nip == 3):
            Img1 = Image.open("HealthyLeaf.jpg")
            Img1.show()
            Img2 = Image.open("LeafD.jpg")
            Img2.show()
            
        else:
            print("Bad input. Please check your input")
    elif(ni == 2):
        print("You don't want to see the leaves")
    else:
        print("Invalid Input! Please correct the same")

def compareeucl():

    image1 = cv2.imread("HealthyLeaf.jpg")
    image2 = cv2.imread("LeafD.jpg")
    
    print("~~~~~~~~~~~~~~ Disease check ~~~~~~~~~~~~~")
    print("1. DO you want to the see leaves in greyscale???")
    print("2. Do you want to see the histogram of the leaves???")
    print("3. Do you want to compare the leaves based on the Euclidean Distance???")
    
    nicheck = int(input("Please enter your choice"))
    
    if(nicheck == 1):
        print("1. Healthy Leaf")
        print("2. Diseased Leaf")
        print("3. Healthy Leaf as well as Diseased Leaf")
        nip = int(input("Enter the Leaf number you want to see in greyscale "))
        
        if(nip == 1):
            grayimage1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
            plt.figure()
            plt.axis("off")
            plt.imshow(cv2.cvtColor(grayimage1, cv2.COLOR_GRAY2RGB))
            plt.show()
            
        elif(nip == 2):
            grayimage2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
            plt.figure()
            plt.axis("off")
            plt.imshow(cv2.cvtColor(grayimage2, cv2.COLOR_GRAY2RGB))
            plt.show()
            
        elif(nip == 3):
            grayimage1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
            plt.figure()
            plt.axis("off")
            plt.imshow(cv2.cvtColor(grayimage1, cv2.COLOR_GRAY2RGB))
            plt.show()
            
            grayimage2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
            plt.figure()
            plt.axis("off")
            plt.imshow(cv2.cvtColor(grayimage2, cv2.COLOR_GRAY2RGB))
            plt.show()
            
        else:
            print("Bad input. Please check your input")
            
    elif(nicheck == 2):
        print("1. Histogram of Healthy Leaf")
        print("2. Histogram of Diseased Leaf")
        print("3. Histogram of Healthy Leaf as well as Diseased Leaf")
        nip = int(input("Enter the Leaf number you want to see in greyscale "))
        
        if(nip == 1):
            grayimage1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
            histogramtest = cv2.calcHist([grayimage1], [0], None, [256], [0, 256])
            histogramtest /= histogramtest.sum()
            plt.figure()
            plt.title("Healthy Leaf")
            plt.xlabel("Bins")
            plt.ylabel("% of Pixels")
            plt.plot(histogramtest)
            plt.xlim([0, 256])
            plt.show()
            
        elif(nip == 2):
            grayimage2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
            histogram1 = cv2.calcHist([grayimage2], [0], None, [256], [0, 256])
            histogram1 /= histogram1.sum()
            plt.figure()
            plt.title("Diseased leaf")
            plt.xlabel("Bins")
            plt.ylabel("% of Pixels")
            plt.plot(histogram1)
            plt.xlim([0, 256])
            plt.show()
            
        elif(nip == 3):
            grayimage1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
            histogramtest = cv2.calcHist([grayimage1], [0], None, [256], [0, 256])
            histogramtest /= histogramtest.sum()
            plt.figure()
            plt.title("Healthy Leaf")
            plt.xlabel("Bins")
            plt.ylabel("% of Pixels")
            plt.plot(histogramtest)
            plt.xlim([0, 256])
            plt.show()

            grayimage2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
            histogram1 = cv2.calcHist([grayimage2], [0], None, [256], [0, 256])
            histogram1 /= histogram1.sum()
            plt.figure()
            plt.title("Diseased leaf")
            plt.xlabel("Bins")
            plt.ylabel("% of Pixels")
            plt.plot(histogram1)
            plt.xlim([0, 256])
            plt.show()
            
        else:
            print("Bad input. Please check your input")
            
    elif(nicheck == 3):
        grayimage1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        histogramtest = cv2.calcHist([grayimage1], [0], None, [256], [0, 256])

        grayimage2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        histogram1 = cv2.calcHist([grayimage2], [0], None, [256], [0, 256])

        c1 = 0
        c2 = 0
        
        i = 0
        while i<len(histogramtest) and i<len(histogram1):
            c1+=(histogramtest[i]-histogram1[i])**2
            i+= 1
        c1 = c1**(1 / 2)

        if(c1==0):
            print("There is no disease in the leaf")
            
        else:
            print("There is disease in the leaf, and the Euclidean Distance between Healthy Leaf and Diseased Leaf is: ", c1)
            
    else:
        print("Invalid Input! Please correct the same")

def compareimpro():
    print("~~~~~~~~~~~~~~ Disease check ~~~~~~~~~~~~~")
    print("1. Do you want to see the place where disease has occured???")
    print("2. Do you want to see the number of places where disease has occured???")
    print("3. Do you want to see the number of places as well as see the place where disease has occured???")
    
    nicheck = int(input("Please enter your choice"))
    
    if(nicheck == 1):
        print("You need to resize Diseased Leaf with respect to Healthy Leaf")
        healthy = cv2.imread("HealthyLeaf.jpg")
        diseased = cv2.imread("LeafD.jpg")
 
        print('Original Dimensions of Healthy Leaf: ',healthy.shape)
 
        height = int(input("Enter the value of height(1st value): "))
        width = int(input("Enter the value of width(2nd value): "))
        dim = (width, height)
 
        # resize image
        diseased = cv2.resize(diseased, dim, interpolation = cv2.INTER_AREA)

        print('Resized Dimensions of Diseased Leaf: ',diseased.shape)
        
        if healthy.shape==diseased.shape:
            # subtract the images
            subtracted = cv2.subtract(diseased, healthy)
    
            # TO show the output
            cv2.imshow('image', subtracted)
    
            # To close the window
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("The Diseased Leaf has not been resized properly with respect to Healthy Leaf")
            
            print("Please try again after resing the Leaf")
            
    elif(nicheck == 2):
        Healthyleaf = imagehash.whash(Image.open("HealthyLeaf.jpg"))
        Diseasedleaf = imagehash.whash(Image.open("LeafD.jpg"))
        
        if(Healthyleaf == Diseasedleaf):
            print("There is no disease in the leaf!!")
            
        else:
            print("There is disease in leaf at ",str(Healthyleaf - Diseasedleaf)," places")
            
    elif(nicheck == 3):
        Healthyleaf = imagehash.whash(Image.open("HealthyLeaf.jpg"))
        Diseasedleaf = imagehash.whash(Image.open("LeafD.jpg"))
        
        if(Healthyleaf == Diseasedleaf):
            print("There is no disease in the leaf!!")
            
        else:
            print("There is disease in leaf at ",str(Healthyleaf - Diseasedleaf)," places")
            print("You need to resize Diseased Leaf with respect to Healthy Leaf to view the places where there is disease")
            healthy = cv2.imread("HealthyLeaf.jpg")
            diseased = cv2.imread("LeafD.jpg")
 
            print('Original Dimensions of Healthy Leaf: ',healthy.shape)
 
            height = int(input("Enter the value of height(1st value): "))
            width = int(input("Enter the value of width(2nd value): "))
            dim = (width, height)
 
            # resize image
            diseased = cv2.resize(diseased, dim, interpolation = cv2.INTER_AREA)

            print('Resized Dimensions of Diseased Leaf: ',diseased.shape)
        
            if healthy.shape==diseased.shape:
                # subtract the images
                subtracted = cv2.subtract(diseased, healthy)
    
                # TO show the output
                cv2.imshow('image', subtracted)
    
                # To close the window
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            
    else:
        print("Invalid Input! Please correct the same")
        
ch = "y"

while(ch=="y"):
    
    print("1. View the leaves")
    print("2. Compare healthy leaf with diseased leaf using Euclidean Distance")
    print("3. Compare healthy leaf with diseased leaf using Image Processing")
    n = int(input("Enter your choice :"))
    main_ho(n)
    ch = input("Do you wish to continue? (y/n) ")

if(ch == "n"):
    print ("                                                  !!!Thank you!!!")
