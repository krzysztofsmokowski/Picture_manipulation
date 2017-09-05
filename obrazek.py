from PIL import Image, ImageDraw

def duzy_punkt(x, y, draw):
    for dx in range(-2,3):
        for dy in range(-2,3):
            draw.point((dx+x, dy+y), fill='red')


def get_point_on_map(longitude, latitude):
    '''
    Input: longitude and latitude in float, eg:
        51*30' = 51,50
    Return: x, y where x i horizontal pixel number, and y vertical
    for the map file
    We will use the image properties to calculate pixels
    longitude map:
    15*10' is 106
    23*10' is 744
    so 1' = 80px
    assumption: 14* is the 0 pixel
    latitude map:
    50*20' is 518
    53*40' is 160
    so 1' = 107px
    assumption: 55' is the 0 pixel
    (360.0, 420.0)
    '''
    x=(longitude-14) * 80 + 15
    y=(55-latitude) *107.3 +20
    return(x,y)


def draw_point_on_image(x,y):
    im = Image.open("blank-simple-map-of-poland-no-labels.jpg")
    draw = ImageDraw.Draw(im)
    duzy_punkt(x, y, draw)

    im.save("mapka.PNG")


