from PIL import Image
image = Image.open('test.png')
def hide_text(original_image, text):
    blank_image = Image.new("RGB", (original_image.width, original_image.height))
    blank_image_data = blank_image.load()
    original_data = original_image.load()
    #Switch the message to hid to binary 
    binary_text = ''.join(format(ord(i), '08b') for i in text)
    print(binary_text)
    index = 0

    #Loop thru image
    for y in range(original_image.height):
        for x in range(original_image.width):
            #Groups of 3 
            r, g, b = original_data[x, y]
            
            #Check if the index of the pixels to change is greater than index 
            if index < len(binary_text):
                #Perform AND operation with NOT 1 on Binrary and Or it with the same index of the binary int
                r = (r & 254) | int(binary_text[index])  
                index += 1
            #Do Green
            if index < len(binary_text): #Check
                g = (g & 254) | int(binary_text[index]) 
                index += 1
            if index < len(binary_text):
                b = (b & 254) | int(binary_text[index])  
                index += 1
            if index >= len(binary_text):
                break
        if index >= len(binary_text):
            break
        return blank_image
steg_image = hide_text(image, 'Hello')
steg_image.save('Steg.png')

#data = image.load()
#for y in range(image.height)
    #for x in range
        #r,g,b,_ = data[x,y]   No errors
        # data[x,y] = (r,g,b)
        # r = r & 254 
        # g = g & 254
        # b = b & 254

        # LSB is 11111110
        #Can Modify as we go add more 0
