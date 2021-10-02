import os, sys
from PIL import Image, ImageChops, ImageEnhance

# converts input image to ela applied image
def convert_to_ela_image(path, quality):

    original_image = Image.open(path).convert("RGB")

    # resaving input image at the desired quality
    resaved_file_name = "resaved_image.jpg"  # predefined filename for resaved image
    original_image.save(resaved_file_name, "JPEG", quality=quality)
    resaved_image = Image.open(resaved_file_name)

    # pixel difference between original and resaved image
    ela_image = ImageChops.difference(original_image, resaved_image)

    # scaling factors are calculated from pixel extremas
    extrema = ela_image.getextrema()
    max_difference = max([pix[1] for pix in extrema])
    if max_difference == 0:
        max_difference = 1
    scale = 350.0 / max_difference

    # enhancing elaimage to brighten the pixels
    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)

    ela_image.save("ela_image.png")
    return ela_image


if __name__ == "__main__":
    file_path = sys.argv[1]
    quality = int(sys.argv[2])
    convert_to_ela_image(file_path, quality).show()
