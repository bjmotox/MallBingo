from PIL import Image, ImageDraw, ImageFont
import random

# list of phrases/bingo objects
bingo_board = [
    "Kid dressed cooler than you", "Man shopping for lingerie", "Group together, all on their phones(3+)", "Man waiting outside store holding bags", "Line of over 7 people", "Couple with too much PDA", "Man carrying 3 bags", "Christian T Shirt", "Mannequin in floral", "unibrow", "Employee outside of store", "ripped jeans", "Elderly Couple", "red tennis shoes", "Seasonally Inappropriate", "Kid Running", "quiet argument", "Unnatural hair color", "Someone Talking on Phone", "Eating Lolipop", "Walking on phone not looking", "4+ Girls together", "Family of 6+", "parent scolding", "Using Massage Chair", "Someone Facetiming", "Monochrome outfit", 
]

#Shuffle board objects
random.shuffle(bingo_board)

# generate the bingo card, and create the grid
bingo_card = []
for i in range(5):
    row = bingo_board [i *5: (i+1)*5]
    bingo_card.append(row)
# Center Free space
bingo_card [2][2] = "FREE"


def create_bingo_card_image(card, output_file="bingo_card.png"):
    # Dimensions
    cell_width = 150
    cell_height = 100
    grid_width = 5 * cell_width
    grid_height = 5 * cell_height
    
    # Create image
    img = Image.new("RGB", (grid_width, grid_height), "white")
    draw = ImageDraw.Draw(img)
    
    # Font setup
    try:
        font = ImageFont.truetype("arial.ttf", 12)
    except IOError:
        font = ImageFont.load_default()  # Fallback to default font
    
    # Draw grid and phrases
    for i, row in enumerate(card):
        for j, cell in enumerate(row):
            x0 = j * cell_width
            y0 = i * cell_height
            x1 = x0 + cell_width
            y1 = y0 + cell_height
            
            # Draw rectangle for each cell
            draw.rectangle([x0, y0, x1, y1], outline="black", width=2)
            
            # Add the phrase
            text_width, text_height = draw.textsize(cell, font=font)
            text_x = x0 + (cell_width - text_width) / 2
            text_y = y0 + (cell_height - text_height) / 2
            draw.text((text_x, text_y), cell, fill="black", font=font)
    
    # Save image
    img.save(output_file)
    print(f"Bingo card saved as {output_file}")

# Step 4: Create the image
create_bingo_card_image(bingo_card)