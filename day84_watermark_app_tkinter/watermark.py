from PIL import Image, ImageDraw, ImageFont

SAVE_DIR = 'out/your_watermarked_image.png'

def wt_text(path_image, txt):
    with Image.open(path_image).convert("RGBA") as base:
        # find the center of the image
        x = int(base.size[0] / 2)
        y = int(base.size[1] / 2)

        # make a blank image for the text, initialized to transparent text color
        txt_layer = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # get a font
        fnt = ImageFont.truetype("arial.ttf", 40)
        # get a drawing context
        d = ImageDraw.Draw(txt_layer)

        # draw text, half opacity
        d.text((x+10, y+10), text=txt, font=fnt, fill=(255, 255, 255, 130))

        # merging text "layer" with base
        out = Image.alpha_composite(base, txt_layer)

        out.save(SAVE_DIR)

def wt_logo(path_image, path_logo):
    with Image.open(path_image).convert("RGBA") as base:
        # find the center of the image
        x = int(base.size[0] / 2)
        y = int(base.size[1] / 2)

        logo = Image.open(path_logo).convert("RGBA")
        logo.putalpha(130)

        w = base.size[0] + logo.size[0]
        h = max(base.size[1], logo.size[1])
        im = Image.new("RGBA", (w, h))

        im.paste(base)
        im.paste(logo, box=(x,y), mask=logo)

        im.save(SAVE_DIR)