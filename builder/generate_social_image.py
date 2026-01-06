#!/usr/bin/env python3
"""
Generate social preview image (1200×630px) for Open Graph and Twitter Cards.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def generate_social_preview():
    """Generate a 1200×630px social preview image."""

    # Image dimensions (Open Graph standard)
    width, height = 1200, 630

    # Colors
    bg_color = '#1e293b'  # Dark slate
    text_color = '#ffffff'  # White
    accent_color = '#60a5fa'  # Blue

    # Create image
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Try to load fonts, fall back to default if not available
    try:
        title_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 72)
        subtitle_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 36)
        lang_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 24)
    except:
        # Fallback to default font
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        lang_font = ImageFont.load_default()

    # Title
    title_text = "Programming Language"
    title2_text = "Comparison"

    # Calculate center positions
    # Title line 1
    bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = bbox[2] - bbox[0]
    title_x = (width - title_width) / 2
    title_y = 150

    # Title line 2
    bbox2 = draw.textbbox((0, 0), title2_text, font=title_font)
    title2_width = bbox2[2] - bbox2[0]
    title2_x = (width - title2_width) / 2
    title2_y = title_y + 90

    # Draw title
    draw.text((title_x, title_y), title_text, fill=text_color, font=title_font)
    draw.text((title2_x, title2_y), title2_text, fill=text_color, font=title_font)

    # Subtitle
    subtitle_text = "23+ Languages Side by Side"
    bbox3 = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = bbox3[2] - bbox3[0]
    subtitle_x = (width - subtitle_width) / 2
    subtitle_y = title2_y + 120

    draw.text((subtitle_x, subtitle_y), subtitle_text, fill=accent_color, font=subtitle_font)

    # Add sample language names
    languages = ["Python", "JavaScript", "Rust", "Go", "Java"]
    lang_text = "  •  ".join(languages)

    bbox4 = draw.textbbox((0, 0), lang_text, font=lang_font)
    lang_width = bbox4[2] - bbox4[0]
    lang_x = (width - lang_width) / 2
    lang_y = subtitle_y + 70

    draw.text((lang_x, lang_y), lang_text, fill='#94a3b8', font=lang_font)

    # Add decorative line
    line_y = 100
    line_margin = 150
    draw.line([(line_margin, line_y), (width - line_margin, line_y)], fill=accent_color, width=3)

    # Save image
    output_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'social-preview.png')
    img.save(output_path, 'PNG')

    print(f"✓ Social preview image generated: {output_path}")
    print(f"  Size: {width}×{height}px")
    print(f"  Format: PNG")

    return output_path

if __name__ == '__main__':
    generate_social_preview()
