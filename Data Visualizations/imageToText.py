from urllib import request
from PIL import Image

ascii_chars = list('$@B%mZXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`')
               
def scale_image(image, new_width=80):
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width) * 0.5
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=25):
    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ascii_chars[int(pixel_value/range_width)] for pixel_value in pixels_in_image]
    return ''.join(pixels_to_chars)

def convert_image_to_ascii(image, new_width=80):
    image = scale_image(image, new_width)
    image = convert_to_grayscale(image)
    
    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)
    
    image_ascii = [pixels_to_chars[index: index + new_width] for index in range(0,len_pixels_to_chars,new_width)]
    return '\n'.join(image_ascii)

def handle_image_conversion(image_filepath, new_width=80):
    image = Image.open(image_filepath)
    image_ascii = convert_image_to_ascii(image,new_width)
    print(image_ascii)
    
image_file_path = 'a'
image_url = 'https://2.bp.blogspot.com/-0Z44UG8mCYM/W_k745lbDRI/AAAAAAAAGMs/vyRsH8BiWaEFz7lI_D_Jc1R5B2rzuK3AgCK4BGAYYCw/s1600/Benedict%2BCumberbatch%2BAwesome%2BProfile%2BPics%2BDP%2BImages%2B%252827%2529.jpg'
request.urlretrieve(image_url,image_file_path)
handle_image_conversion(image_file_path)