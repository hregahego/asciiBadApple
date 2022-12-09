from PIL import Image






#main converter
def convert(img,size,gap):
    # OPEN IMAGE

    image = Image.open(img)



    #VARIABLES
    output = ''

    # IMAGE PROCESSING
    
    imgRGB = image.convert("RGB")
    imgRGB = imgRGB.resize((int((imgRGB.size[0] * size)), int((imgRGB.size[1] * size))), Image.ANTIALIAS)

    width = imgRGB.size[0]
    height = imgRGB.size[1]
    #print(f"{width}, {height}")




    for y in range(int(height)):
        for x in range(int(width)):

            rgb = imgRGB.getpixel((x,y))

            r = rgb[0]
            g = rgb[1]
            b = rgb[2]
            brightness = (0.2126*r)+(0.7152*g)+(0.0722*b)

            if brightness > 200:
                output+=((gap*" ") + ".")
            elif brightness > 170:
                output+=((gap*" ") + ",")
            elif brightness > 150:
                output+=((gap*" ") + "_")
            elif brightness > 130:
                output+=((gap*" ") + "-")
            elif brightness > 110:
                output+=((gap*" ") + "=")
            elif brightness > 90:
                output+=((gap*" ") + "+")
            elif brightness > 70:
                output+=((gap*" ") + "*")
            elif brightness > 50:
                output+=((gap*" ") + "&")
            elif brightness > 30:
                output+=((gap*" ") + "#")
            elif brightness > 10:
                output+=((gap*" ") + "%")
            else:
                output+=((gap*" ") + "@")

        output+=('\n')


    return output

















