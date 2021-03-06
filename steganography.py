"""A program that encodes and decodes hidden messages in images through LSB steganography"""
from PIL import Image, ImageFont, ImageDraw
import textwrap


def decode_image(file_location="images/encoded_sample.png"):
    """Decodes the hidden message in an image.

    Parameters
    ----------
    file_location: str
        The location of the image file to decode. This defaults to the provided
        encoded image in the images folder.
    """
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]
    # The above could also be written as one of:
    #   red_channel, green_channel, blue_channel = encoded_image.split()
    #   red_channel, _, _ = encoded_image.split()
    #   red_channel, *_ = encoded_image.split()
    # The first has the disadvantage of creating temporary variables that aren't
    # used. The special variable name _ (underscore) is conventionally named
    # an unused variable.

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]
    # The above could also be written as:
    #   x_size, y_size = encoded_image.size[0]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for x in range(x_size):
        for y in range(y_size):
            pixel_bits = len(bin(red_channel.getpixel((x,y))))
            #print(bin(red_channel.getpixel((x,y))))
            if int(bin(red_channel.getpixel((x,y)))[pixel_bits-1]) == 0:
                decoded_image.putpixel((x,y),(0,0,0))
            if int(bin(red_channel.getpixel((x,y)))[pixel_bits-1]) == 1:
                decoded_image.putpixel((x,y),(255,255,255))

    decoded_image.save("images/decoded_image.png")


def write_text(text_to_write, image_size):
    """Write text to an RGB image. Automatically line wraps.

    Parameters
    ----------
    text_to_write: str
        The text to write to the image.
    image_size: (int, int)
        The size of the resulting text image.
    """
    image_text = Image.new("RGB", image_size)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)

    # Text wrapping. Change parameters for different text formatting
    margin = offset = 10
    for line in textwrap.wrap(text_to_write, width=60):
        drawer.text((margin, offset), line, font=font)
        offset += 10
    return image_text


def encode_image(text_to_encode, template_image="images/samoyed.jpg"):
    """Encode a text message into an image.

    Parameters
    ----------
    text_to_encode: str
        The text to encode into the template image.
    template_image: str
        The image to use for encoding. An image is provided by default.
    """
    image_to_encode = Image.open(template_image)
    image_text = write_text(text_to_encode, image_to_encode.size)
    image_text.save("images/written_text.png")
    R_channel = image_text.getchannel(0)
    encode_r_channel = image_to_encode.getchannel(0)
    encode_g_channel = image_to_encode.getchannel(1)
    encode_b_channel = image_to_encode.getchannel(2)

    encoded_image = image_to_encode

    for x in range(image_to_encode.width):
        for y in range(image_to_encode.height):
            pixel_bits = len(bin(encode_r_channel.getpixel((x,y))))
            if R_channel.getpixel((x,y)) == 0:
                thing = bin(encode_r_channel.getpixel((x,y)))
                thing = thing[:len(thing)-1] + "0"
                encoded_image.putpixel((x,y),(int(thing, 2),int(encode_g_channel.getpixel((x,y))),int(encode_b_channel.getpixel((x,y)))))
            if R_channel.getpixel((x,y)) == 255:
                thing2 = bin(encode_r_channel.getpixel((x,y)))
                thing2 = thing2[:len(thing2)-1] + "1"
                encoded_image.putpixel((x,y),(int(thing2, 2),int(encode_g_channel.getpixel((x,y))),int(encode_b_channel.getpixel((x,y)))))

    encoded_image.save("images/encoded_image.png")


if __name__ == '__main__':
    print("Decoding the image...")
    decode_image()

    print("Encoding the image...")
    encode_image("For a number of years now, work has been proceeding in order to bring perfection to the crudely conceived idea of a transmission that would not only supply inverse reactive current for use in unilateral phase detractors, but would also be capable of automatically synchronizing cardinal grammeters. Such an instrument is the turbo encabulator. Now basically the only new principle involved is that instead of power being generated by the relative motion of conductors and fluxes, it is produced by the modial interaction of magneto-reluctance and capacitive diractance. The original machine had a base plate of pre-famulated amulite surmounted by a malleable logarithmic casing in such a way that the two spurving bearings were in a direct line with the panametric fan. The latter consisted simply of six hydrocoptic marzlevanes, so fitted to the ambifacient lunar waneshaft that side fumbling was effectively prevented. The main winding was of the normal lotus-o-delta type placed in panendermic semi-boloid slots of the stator, every seventh conductor being connected by a non-reversible tremie pipe to the differential girdle spring on the up end of the grammeters. The turbo-encabulator has now reached a high level of development, and it's being successfully used in the operation of novertrunnions. Moreover, whenever a forescent skor motion is required, it may also be employed in conjunction with a drawn reciprocation dingle arm, to reduce sinusoidal repleneration. It's not cheap, but I'm sure the government will buy it.")
