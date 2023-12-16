# init Flask
from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

from random import choice, randint

def generate_tree(nameage, height, distance, treeimageNo, shoplink, description):
    page = render_template("home.html",
                            nameage=nameage,
                            height=height,
                            distance=distance,
                            treeimageNo=treeimageNo,
                            shoplink=shoplink,
                            description=description)

    return page


shoplinks = ("https://www.google.com/maps/@50.038385,15.6634833,15.88z?entry=ttu", "https://www.google.com/maps/@49.9328538,15.7070868,11.88z?entry=ttu", "https://www.google.com/maps/@49.0105747,15.1451436,7.85z?entry=ttu", "https://www.google.com/maps/@48.9399861,14.6079832,8.34z?entry=ttu", "https://www.google.com/maps/@48.5432567,21.9970784,5.63z?entry=ttu", "https://www.google.com/maps/@51.1718972,20.1323286,6.63z?entry=ttu", "https://www.google.com/maps/@46.2678024,6.4849165,5.82z?entry=ttu", "https://www.google.com/maps/@14.289778,14.8784081,4.18z?entry=ttu", "https://www.google.com/maps/@27.0666199,72.9260677,4.07z?entry=ttu", "https://www.google.com/maps/@55.5774897,53.0481825,4.73z?entry=ttu", "https://www.google.com/maps/@50.104143,17.4672411,7.54z?entry=ttu",
             "https://www.aliexpress.com/item/1005005628801037.html?spm=a2g0o.productlist.main.1.73397e8bc9i5c8&algo_pvid=8b603663-f217-4fe3-81a2-7f8e7dc6c595&algo_exp_id=8b603663-f217-4fe3-81a2-7f8e7dc6c595-0&pdp_npi=4%40dis%21CZK%21499.68%2158.42%21%21%21157.00%21%21%40211b600b17026891870594772ec154%2112000033806989144%21sea%21CZ%210%21AB&curPageLogUid=YdUsVrcaxEMw", "https://www.aliexpress.com/item/1005006165780363.html?spm=a2g0o.productlist.main.3.20447342FmdXmG&algo_pvid=4404df1a-8a73-41b5-ba76-bdae8cd4ad15&algo_exp_id=4404df1a-8a73-41b5-ba76-bdae8cd4ad15-1&pdp_npi=4%40dis%21CZK%21521.17%21407.7%21%21%21163.75%21%21%402103868d17026892130704350ebdc0%2112000036070392118%21sea%21CZ%210%21AB&curPageLogUid=yfOemJ78QaRp", "https://www.aliexpress.com/item/1005006165985932.html?spm=a2g0o.productlist.main.13.20447342FmdXmG&algo_pvid=4404df1a-8a73-41b5-ba76-bdae8cd4ad15&algo_exp_id=4404df1a-8a73-41b5-ba76-bdae8cd4ad15-6&pdp_npi=4%40dis%21CZK%21357.35%21243.88%21%21%21112.28%21%21%402103868d17026892130704350ebdc0%2112000036070786561%21sea%21CZ%210%21AB&curPageLogUid=lhFPgeuLRZ4C", "https://www.aliexpress.com/item/1005006124932342.html?spm=a2g0o.productlist.main.3.6c0752accAeQQB&algo_pvid=e7b6e84f-1200-4e10-8da5-d4c9b05d4828&algo_exp_id=e7b6e84f-1200-4e10-8da5-d4c9b05d4828-1&pdp_npi=4%40dis%21CZK%2182.08%2153.34%21%21%2125.79%21%21%40211b801a17026892396873503e0748%2112000035864791381%21sea%21CZ%210%21AB&curPageLogUid=loDvrXVz0UkZ", "https://www.aliexpress.com/item/1005004857599756.html?spm=a2g0o.productlist.main.9.6c0752accAeQQB&algo_pvid=e7b6e84f-1200-4e10-8da5-d4c9b05d4828&aem_p4p_detail=20231215171359957454217920540000581983&algo_exp_id=e7b6e84f-1200-4e10-8da5-d4c9b05d4828-4&pdp_npi=4%40dis%21CZK%21172.22%2187.85%21%21%2154.11%21%21%40211b801a17026892396873503e0748%2112000030771375682%21sea%21CZ%210%21AB&curPageLogUid=udFFDpAByjra&search_p4p_id=20231215171359957454217920540000581983_1", "https://www.aliexpress.com/item/1005006153035614.html?spm=a2g0o.productlist.main.1.6c0752accAeQQB&algo_pvid=e7b6e84f-1200-4e10-8da5-d4c9b05d4828&algo_exp_id=e7b6e84f-1200-4e10-8da5-d4c9b05d4828-0&pdp_npi=4%40dis%21CZK%21213.09%21110.74%21%21%219.39%21%21%40211b801a17026892396873503e0748%2112000036005285768%21sea%21CZ%210%21AB&curPageLogUid=vQmzNMAOmzss", "https://www.aliexpress.com/item/1005005486988177.html?spm=a2g0o.productlist.main.1.79883d69bHtA4k&algo_pvid=bf04008b-b67e-4e92-9680-a6a05150a438&algo_exp_id=bf04008b-b67e-4e92-9680-a6a05150a438-0&pdp_npi=4%40dis%21CZK%2154.69%2132.9%21%21%212.41%21%21%40210384cc17026892743231439eb29c%2112000033274712421%21sea%21CZ%210%21AB&curPageLogUid=2PMZ43aHud5t", "https://www.aliexpress.com/item/1005001941081773.html?spm=a2g0o.productlist.main.21.79883d69bHtA4k&algo_pvid=bf04008b-b67e-4e92-9680-a6a05150a438&algo_exp_id=bf04008b-b67e-4e92-9680-a6a05150a438-10&pdp_npi=4%40dis%21CZK%21260.52%21195.39%21%21%2111.48%21%21%40210384cc17026892743231439eb29c%2112000026872000668%21sea%21CZ%210%21AB&curPageLogUid=C9IQgHxN1JSH", "https://www.aliexpress.com/item/1005006131065258.html?spm=a2g0o.productlist.main.11.79883d69bHtA4k&algo_pvid=bf04008b-b67e-4e92-9680-a6a05150a438&algo_exp_id=bf04008b-b67e-4e92-9680-a6a05150a438-5&pdp_npi=4%40dis%21CZK%2118.38%2115.43%21%21%210.81%21%21%40210384cc17026892743231439eb29c%2112000035899280450%21sea%21CZ%210%21AB&curPageLogUid=n8JYGjPCsmbS", "https://www.aliexpress.com/item/1005004402196151.html?spm=a2g0o.productlist.main.13.79883d69bHtA4k&algo_pvid=bf04008b-b67e-4e92-9680-a6a05150a438&algo_exp_id=bf04008b-b67e-4e92-9680-a6a05150a438-6&pdp_npi=4%40dis%21CZK%2170.35%2111.12%21%21%213.10%21%21%40210384cc17026892743231439eb29c%2112000029049266298%21sea%21CZ%210%21AB&curPageLogUid=NlRmRFHcY29d")

names = ("Maggie", "Jake", "Grace", "Jim", "Tammy", "Marty", "Gloria", "Freda", "Charlie", "Susan", "Grace", "Raul", "Chuck", "Dylan", "Penelope", "Vicky", "Willow", "Benny", "Holly", "Sam")

descriptions = (
"""

🌲 Shape & Type: I'm a festive Fraser Fir, shaped to sleigh perfection!\n
🎁 Hobbies: Hosting ornament parties, spreading joy, and making spirits bright.\n
🌟 Fun Facts: I've been the star of three family holiday cards in a row!\n
😄 Favorite Tree Joke: Why did the Christmas tree go to therapy? It had too many issues with its family roots!\n
""", """

🌲 Shape & Type: I'm a classic Colorado Blue Spruce, standing tall and proud!\n
🎁 Hobbies: Sparkling with lights, playing Santa, and being the heart of the celebration.\n
🌟 Fun Facts: I once survived a blizzard and came out even merrier!\n
😄 Favorite Tree Joke: How do Christmas trees get their hair done? They go to the pine-salon!\n
""", """

🌲 Shape & Type: I'm a shimmering Silver Tip, adding elegance to your festivities!\n
🎁 Hobbies: Collecting the fanciest ornaments, creating a winter wonderland, and twinkle-light acrobatics.\n
🌟 Fun Facts: I once had a cameo in a holiday commercial—blink, and you might miss me!\n
😄 Favorite Tree Joke: What do you call a Christmas tree with no decorations? Bough naked!\n
""", """

🌲 Shape & Type: I'm a plump and merry Pine, perfect for holiday cuddles!\n
🎁 Hobbies: Spreading twinkling lights, hosting ornament parties, and basking in the festive glow.\n
🌟 Fun Facts: I once had a cameo in a holiday movie, and my branches are certified mistletoe-free!\n
😄 Favorite Tree Joke: Why do Christmas trees like knitting? They've got the best needles in town!\n
""", """

🌲 Shape & Type: I'm a graceful and slender Spruce, designed for elegance!\n
🎁 Hobbies: Draping myself in dazzling tinsel, making spirits bright, and creating the perfect backdrop for holiday selfies.\n
🌟 Fun Facts: I've survived three snowstorms and a particularly enthusiastic cat encounter.\n
😄 Favorite Tree Joke: What do you call a cat on the beach during Christmas time? Sandy Claws!\n
""", """

🌲 Shape & Type: I'm a quirky and asymmetrical Cedar, bringing a touch of whimsy to the holidays!\n
🎁 Hobbies: Hosting woodland creature tea parties, swaying to holiday tunes, and embracing my unique charm.\n
🌟 Fun Facts: My branches are perfect for secret ornament hiding spots, and I've been featured in a tree art exhibition.\n
😄 Favorite Tree Joke: What do you get if you cross a Christmas tree with an iPad? A pineapple!\n
""", """

🌲 Shape & Type: I'm a glamorous and frosted Fir, always ready for a winter wonderland!\n
🎁 Hobbies: Being the star of the show, sparkling with holiday magic, and indulging in cozy fireside snuggles.\n
🌟 Fun Facts: I once stood beside Santa for an entire night, and I've mastered the art of the perfect ornament t\n\nwir
😄 Favorite Tree Joke: Why was the Christmas tree so bad at math? It could never count its needles!\n
""", """

🌲 Shape & Type: I'm a round and jolly Redwood, ready to embrace the season with open branches!\n
🎁 Hobbies: Spreading joy, cultivating a forest of holiday cheer, and collecting heartwarming memories.\n
🌟 Fun Facts: I once served as a makeshift stage for a surprise proposal, and my sap is 100% certified jo\n\nyou
😄 Favorite Tree Joke: What did the Christmas tree say to the ornament? 'You light up my life!'\n
""", """

🌲 Shape & Type: I'm a harmonious and traditional Hemlock, ready to sing in the spirit of the season!\n
🎁 Hobbies: Spreading carol vibes, hosting sing-alongs, and standing tall as a beacon of festive melody.\n
🌟 Fun Facts: I once duetted with a neighborhood owl, and my needles are known for their melodious rustle.\n
😄 Favorite Tree Joke: What do you call a Christmas tree that sings? Spruce Springsteen!\n
""", """

🌲 Shape & Type: I'm a radiant and twinkling Tannenbaum, designed for maximum holiday dazzle!\n
🎁 Hobbies: Illuminating the night, playing hide-and-seek with ornaments, and being the shining star of every celebration.\n
🌟 Fun Facts: I once inspired a local light show, and my branches have a natural glittery shimmer.\n
😄 Favorite Tree Joke: Why do Christmas trees like to knit? They’re purl-fectly suited for it!\n
""", """

🌲 Shape & Type: I'm a whimsical Willow, dancing through the holidays with my weeping branches!\n
🎁 Hobbies: Hosting woodland critter tea parties, swaying in the winter breeze, and sprinkling magic dust on snowflakes.\n
🌟 Fun Facts: My branches have a built-in mistletoe, and I once starred in a tree fashion show.\n
😄 Favorite Tree Joke: Why did the tree go to therapy? It had too many issues with its family roots!\n
""", """

🌲 Shape & Type: I'm a dazzling Dogwood, spreading love and sparkle wherever I grow!\n
🎁 Hobbies: Illuminating the night with my colorful lights, crafting handmade ornaments, and standing tall as a beacon of joy.\n
🌟 Fun Facts: My flowers bloom in the shape of tiny stars, and I once had a cameo in a tree-themed sitcom.\n
😄 Favorite Tree Joke: What did the tree say to the lumberjack? 'I'm falling for you!'\n
""", """

🌲 Shape & Type: I'm a perky Palm Tree turned holiday delight, swaying in the tropical winter breeze!\n
🎁 Hobbies: Hosting beach-themed holiday parties, sipping coconut eggnog, and spreading warmth with my frondy cheer.\n
🌟 Fun Facts: My coconuts double as festive ornaments, and I once surfed a wave of tinsel.\n
😄 Favorite Tree Joke: What do you call a palm tree in Alaska? Lost!\n
""", """

🌲 Shape & Type: I'm a stylish and symmetrical Sycamore, adding a touch of class to your holiday decor!\n
🎁 Hobbies: Decking myself in bow ties, hosting tree-mendous gatherings, and turning every occasion into an elegant affair.\n
🌟 Fun Facts: I once starred in a tree ballroom dancing competition, and my leaves have a natural glossy shine.\n
😄 Favorite Tree Joke: What do trees wear to weddings? Bark suits!\n
""", """

🌲 Shape & Type: I'm a curious Cypress, standing tall with a hint of mystery in my evergreen allure!\n
🎁 Hobbies: Hosting riddle-solving game nights, blending into the forest, and casting enchanted spells with my boughs.\n
🌟 Fun Facts: My cones hold secrets of ancient tree wisdom, and I once outsmarted a mischievous woodland gnome.\n
😄 Favorite Tree Joke: Why did the tree break up with the stump? It couldn't handle the roots of the problem!\n
""", """

🌲 Shape & Type: I'm a lively and colorful Coral Tree, turning the winter scene into a tropical paradise!\n
🎁 Hobbies: Blooming vibrant flowers, attracting hummingbird friends, and bringing a splash of exotic charm to snowy days.\n
🌟 Fun Facts: My blossoms burst with hues of pink and red, and I once hosted a luau-themed holiday luau.\n
😄 Favorite Tree Joke: What did the tropical tree say to the winter tree? 'You're pining for warmer weather!'\n
""", """

🌲 Shape & Type: I'm a clever Corkscrew Willow, adding a twist of humor to the holiday season!\n
🎁 Hobbies: Telling tree jokes, hosting stand-up comedy nights, and bending my branches into amusing shapes.\n
🌟 Fun Facts: My twisted branches are perfect for hanging whimsical ornaments, and I once collaborated with a famous tree comedian.\n
😄 Favorite Tree Joke: Why do trees have so many friends? They're great at branching out!\n
""", """

🌲 Shape & Type: I'm a bubbling and effervescent Baobab, adding a dose of joy to the winter landscape!\n
🎁 Hobbies: Storing water for thirsty animals, hosting bubble-blowing contests, and spreading happiness with my bulbous charm.\n
🌟 Fun Facts: I've been featured in a documentary on ancient trees, and my trunk can store up to 30,000 gallons of water.\n
😄 Favorite Tree Joke: Why was the tree so good at math? It knew how to multiply!\n
""", """

🌲 Shape & Type: I'm a harmonious and festive Holly tree, bringing a melody of joy to your holiday celebrations!\n
🎁 Hobbies: Sprinkling red berries like musical notes, harmonizing with carolers, and creating a symphony of winter beauty.\n
🌟 Fun Facts: I'm considered a symbol of protection, and I once played a cameo in a holiday musical.\n
😄 Favorite Tree Joke: What's a tree's favorite kind of music? Tree-mbling!\n
""", """

🌲 Shape & Type: I'm a sleigh-shaped Sassafras, ready to dash through the snow with festive flair\n!
🎁 Hobbies: Hosting sleigh rides, spreading aromatic scents, and turning my leaves into nature's potpourri.\n
🌟 Fun Facts: I once had a cameo in a holiday parade, and my roots are known for their spicy aroma.\n
😄 Favorite Tree Joke: What did the Christmas tree say to the ornament? 'You light up my life!'\n
""")


@app.route('/')
def home():
    page = generate_tree(nameage=choice(names)+" "+str(randint(3, 14)),
                         height=str(randint(120, 350)),
                         distance=str(randint(1, 88)),
                         treeimageNo=str(randint(1, 19)),
                         shoplink=choice(shoplinks),
                         description=choice(descriptions).split('\n')
    )

    return page

@app.route('/about')
def about():
    return 'About'