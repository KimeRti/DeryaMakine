from PIL import Image,ImageEnhance

def add_watermark(input_image_path, watermark_image_path, output_image_path, position, transparency=0.5):
    base_image = Image.open(input_image_path).convert("RGBA")
    watermark = Image.open(watermark_image_path).convert("RGBA")

    # Watermark'ın boyutlarını orantılı olarak küçültün (gerekirse)
    watermark_width, watermark_height = watermark.size
    base_width, base_height = base_image.size

    scale_factor = min(base_width / watermark_width, base_height / watermark_height) / 4  # Filigranı küçültme oranı
    new_size = (int(watermark_width * scale_factor), int(watermark_height * scale_factor))
    watermark = watermark.resize(new_size, Image.ANTIALIAS)

    # Filigranı şeffaf hale getirin
    alpha = watermark.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(transparency)
    watermark.putalpha(alpha)

    # Filigranı taban görüntünün üzerine yerleştirin
    if position == 'center':
        position = ((base_width - new_size[0]) // 2, (base_height - new_size[1]) // 2)
    elif position == 'bottom_right':
        position = (base_width - new_size[0], base_height - new_size[1])

    transparent = Image.new('RGBA', (base_width, base_height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, position, mask=watermark)
    transparent = transparent.convert('RGBA')  # PNG olarak kaydetmek için 'RGBA' olarak bırakın

    transparent.save(output_image_path)
