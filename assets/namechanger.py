# this python script helps us rename all images(any format) present in the pics folder  in desired format

import os

os.chdir("./pics")
for count, filename in enumerate(os.listdir()): 
    count = (count+2)//2
    extn = str(filename).split('.')[1]       #to extract extension of the media like .jpg/.gif/.jpeg/.png etc.
    dst ="pic-" + str(count) +'.'+ extn
    src = os.path.join(os.getcwd(), filename) 
    dst = os.path.join(os.getcwd(), dst)
    
    #uncomment next line only when sure to rename, else make a dummy pics folder n try there first.
    # os.rename(src, dst)
    print(os.path.basename(src), '->renamed to->', os.path.basename(dst))       
    
print('\n\n====names changed successfully!====\n\n'.upper())
