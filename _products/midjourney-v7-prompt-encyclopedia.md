# Midjourney V7 Prompt Encyclopedia

> 60+ copy-paste Midjourney prompts organized by style. Each includes full parameters. Replace [BRACKETED VARIABLES] with your subject matter.

---

## QUICK REFERENCE: V7 PARAMETERS

| Parameter | What It Does | Range |
|-----------|-------------|-------|
| `--ar` | Aspect ratio | 1:1, 16:9, 9:16, 4:3, 3:2, 21:9 |
| `--v 7` | Model version | 7 (latest) |
| `--s` / `--stylize` | How artistic vs literal | 0-1000 (default 100) |
| `--c` / `--chaos` | Variation between outputs | 0-100 (default 0) |
| `--w` / `--weird` | Unconventional aesthetics | 0-3000 |
| `--q` | Quality/detail level | .25, .5, 1 (default 1) |
| `--no` | Negative prompt (exclude) | text string |
| `--tile` | Seamless tileable pattern | no value needed |
| `--seed` | Reproducible results | any integer |
| `--style raw` | Less Midjourney beautification | use for photorealism |
| `--p` | Personalization | uses your trained style |

---

## SECTION 1: PHOTOREALISTIC PORTRAITS

### Prompt 1: Editorial Beauty Portrait
```
Close-up portrait of a [ETHNICITY] woman with [HAIR DESCRIPTION], shot on a Canon EOS R5, 85mm f/1.4 lens, natural window light from the left, soft bokeh background, editorial beauty photography, skin texture visible, catch lights in eyes, neutral expression --ar 3:4 --v 7 --s 50 --style raw
```

### Prompt 2: Professional Headshot
```
Professional corporate headshot of a [AGE] [GENDER] [DESCRIPTION], wearing [CLOTHING], warm smile, photographed against a [COLOR] seamless backdrop, Profoto studio lighting with a key light and fill, sharp focus on eyes, LinkedIn-ready, photorealistic --ar 4:5 --v 7 --s 30 --style raw
```

### Prompt 3: Cinematic Character Portrait
```
Cinematic portrait of a [CHARACTER DESCRIPTION], dramatic Rembrandt lighting, deep shadows, [ENVIRONMENT CONTEXT], shot on Arri Alexa, anamorphic lens flare, shallow depth of field, color graded in teal and orange, film grain --ar 2.35:1 --v 7 --s 200
```

### Prompt 4: Environmental Portrait
```
Environmental portrait of a [PROFESSION — e.g., blacksmith, chef, fisherman] in their workspace, [DESCRIBE THE ENVIRONMENT], natural available light, documentary photography style, weathered hands visible, storytelling composition, medium format film look --ar 4:5 --v 7 --s 80 --style raw
```

### Prompt 5: Fashion Editorial
```
High fashion editorial portrait of a model wearing [DESCRIBE OUTFIT], [POSE DESCRIPTION], photographed by [PHOTOGRAPHER STYLE — e.g., in the style of Peter Lindbergh], black and white, dramatic contrast, wind in hair, Vogue magazine quality, studio environment --ar 3:4 --v 7 --s 300
```

### Prompt 6: Street Portrait
```
Candid street portrait of a [PERSON DESCRIPTION] in [CITY], golden hour backlight creating rim light on hair, busy street background with bokeh, shot on Leica M11, 50mm Summilux, photojournalistic style, authentic emotion --ar 3:2 --v 7 --s 50 --style raw
```

---

## SECTION 2: PHOTOREALISTIC LANDSCAPES & NATURE

### Prompt 7: Epic Mountain Landscape
```
Breathtaking panoramic view of [MOUNTAIN/LOCATION], golden hour, dramatic cloud formations, snow-capped peaks reflected in a crystal-clear alpine lake, foreground wildflowers, National Geographic photography, shot on Nikon Z9 with 14-24mm f/2.8, hyper-detailed --ar 21:9 --v 7 --s 100 --style raw
```

### Prompt 8: Moody Seascape
```
Long exposure seascape at [LOCATION], storm clouds gathering, silky smooth water from 30-second exposure, jagged rocks in foreground, dramatic sky with god rays breaking through clouds, fine art landscape photography --ar 16:9 --v 7 --s 150
```

### Prompt 9: Aerial Nature Photography
```
Drone aerial view of [LANDSCAPE — e.g., turquoise river cutting through autumn forest], top-down perspective, abstract patterns created by nature, vivid fall colors contrasting with deep blue water, DJI Mavic shot, sharp detail --ar 4:3 --v 7 --s 80 --style raw
```

### Prompt 10: Intimate Macro Nature
```
Extreme macro photograph of [SUBJECT — e.g., dewdrops on a spider web at sunrise], razor-thin depth of field, bokeh circles from background light sources, every tiny detail visible, focus-stacked, Canon MP-E 65mm lens, nature photography --ar 1:1 --v 7 --s 50 --style raw
```

### Prompt 11: Northern Lights
```
Aurora borealis dancing over [LOCATION — e.g., a frozen lake in Norway], vibrant green and purple curtains of light, star-filled sky, silhouette of pine trees, reflection in still water, long exposure astrophotography, Sony A7S III --ar 16:9 --v 7 --s 200
```

### Prompt 12: Desert Landscape
```
Minimalist desert landscape at [LOCATION — e.g., White Sands, Sahara], single subject [TREE/FIGURE/DUNE] centered, vast negative space, golden hour shadows creating geometric patterns on sand dunes, fine art photography, serene and meditative --ar 3:2 --v 7 --s 120
```

---

## SECTION 3: PRODUCT PHOTOGRAPHY

### Prompt 13: Luxury Product on Pedestal
```
[PRODUCT — e.g., perfume bottle, watch, skincare jar] on a [MATERIAL — marble, concrete, velvet] pedestal, dramatic studio lighting with hard shadows, [COLOR] gradient background, luxury brand aesthetic, product photography, sharp focus, commercial quality --ar 4:5 --v 7 --s 100 --style raw
```

### Prompt 14: Lifestyle Flat Lay
```
Overhead flat lay arrangement of [PRODUCTS — e.g., skincare routine items, coffee accessories, stationery], arranged on [SURFACE — white marble, linen, wooden table], natural daylight from window, styled with [PROPS — fresh flowers, eucalyptus, fabric swatches], Instagram-ready product photography --ar 1:1 --v 7 --s 80
```

### Prompt 15: Product in Environment
```
[PRODUCT] in a [SETTING — e.g., rustic kitchen, modern bathroom, outdoor picnic], lifestyle product photography, natural setting, product is hero but environment tells a story, warm natural light, shallow depth of field with product in sharp focus --ar 4:5 --v 7 --s 60 --style raw
```

### Prompt 16: Food Photography
```
[DISH DESCRIPTION] on a [PLATE/SURFACE DESCRIPTION], overhead 45-degree angle, styled with [PROPS — scattered herbs, linen napkin, vintage cutlery], [LIGHTING — soft window light / moody dark / bright and airy], food photography, mouth-watering detail, shot for cookbook --ar 4:5 --v 7 --s 80 --style raw
```

### Prompt 17: Cosmetics Commercial
```
[COSMETIC PRODUCT — e.g., lipstick, foundation bottle] with a dynamic splash of [TEXTURE — liquid, powder, cream] frozen in mid-air, [COLOR] studio background, high-speed photography effect, hyper-clean commercial look, L'Oreal ad quality --ar 4:5 --v 7 --s 200
```

### Prompt 18: Tech Product Hero Shot
```
[TECH PRODUCT — e.g., wireless earbuds, smartphone, laptop] floating at slight angle, dark environment with [COLOR] accent lighting, reflective surface below, particle effects or light streaks, Apple-style product photography, ultra-clean, minimal --ar 16:9 --v 7 --s 150
```

---

## SECTION 4: ILLUSTRATION & DIGITAL ART

### Prompt 19: Children's Book Illustration
```
[SCENE DESCRIPTION — e.g., a curious fox exploring a magical library], children's book illustration style, warm color palette, whimsical details, soft textures like gouache painting, gentle lighting, storytelling composition, picture book quality --ar 3:2 --v 7 --s 400
```

### Prompt 20: Botanical Illustration
```
Detailed botanical illustration of [PLANT/FLOWER — e.g., a blooming peony with stems and leaves], scientific illustration style, white background, fine linework with watercolor fills, labeled parts, vintage botanical plate aesthetic, hand-drawn quality --ar 3:4 --v 7 --s 250
```

### Prompt 21: Fantasy Concept Art
```
[FANTASY SCENE — e.g., an ancient elven city built into massive tree canopies], epic scale, volumetric fog, bioluminescent elements, intricate architectural details, concept art for film, painterly style, dramatic perspective, warm and cool color contrast --ar 21:9 --v 7 --s 500
```

### Prompt 22: Retro Comic Book Style
```
[SCENE/CHARACTER DESCRIPTION] in the style of vintage 1960s Marvel comic art, bold ink outlines, Ben-Day dots, limited color palette, dynamic action pose, dramatic foreshortening, speech bubble space, halftone printing effect --ar 3:4 --v 7 --s 400
```

### Prompt 23: Anime/Manga Style
```
[CHARACTER DESCRIPTION], anime illustration style, [SETTING], dynamic pose, vibrant color palette, detailed shading with cel-shading technique, expressive eyes, wind-blown elements, studio Ghibli meets modern anime aesthetic --ar 3:4 --v 7 --s 350
```

### Prompt 24: Art Nouveau Poster
```
[SUBJECT — e.g., a woman holding flowers] in Art Nouveau style, ornate decorative border, flowing organic lines, muted jewel-tone color palette, Alphonse Mucha inspired, poster composition with space for text at top, gilded details --ar 2:3 --v 7 --s 500
```

### Prompt 25: Pixel Art Scene
```
[SCENE DESCRIPTION — e.g., a cozy coffee shop interior at night], pixel art style, 32-bit era aesthetic, warm interior lighting contrasting with dark exterior, detailed environment with animated feel, nostalgic retro game vibes --ar 16:9 --v 7 --s 300
```

### Prompt 26: Watercolor Loose Style
```
[SUBJECT — e.g., a Venetian canal scene] in loose expressive watercolor style, wet-on-wet technique, color bleeding and blooming, minimal linework, artistic imperfection, white paper showing through, plein air painting aesthetic --ar 3:4 --v 7 --s 400
```

---

## SECTION 5: 3D RENDERS & ABSTRACT

### Prompt 27: Isometric Room Design
```
Isometric 3D render of a [ROOM TYPE — e.g., cozy home office, plant-filled living room, retro gaming setup], cute miniature dollhouse aesthetic, soft pastel colors, detailed tiny objects, clean white background, Blender render quality --ar 1:1 --v 7 --s 300
```

### Prompt 28: 3D Character Design
```
3D rendered character of a [CHARACTER — e.g., friendly robot, cartoon chef, stylized warrior], Pixar-style rendering, soft subsurface scattering on skin, expressive pose, simple studio background with bounce light, clay render feel with color --ar 4:5 --v 7 --s 250
```

### Prompt 29: Abstract Fluid Art
```
Abstract fluid dynamics simulation, [COLOR PALETTE — e.g., deep blues and molten gold, iridescent pastels], hyper-realistic liquid interaction, flowing organic shapes, studio lit against dark background, Houdini render quality, mesmerizing motion frozen in time --ar 1:1 --v 7 --s 600
```

### Prompt 30: Geometric Abstract
```
Abstract geometric composition, [SHAPES — e.g., interconnected polyhedra, tessellated triangles], [COLOR PALETTE], dramatic lighting casting long shadows, floating in void, mathematical precision meets artistic beauty, 3D render, Octane quality --ar 1:1 --v 7 --s 500
```

### Prompt 31: Surreal 3D Composition
```
Surreal still life, [OBJECTS — e.g., melting clock on a marble shelf, impossible architecture], physically impossible elements rendered photoreal, dramatic studio lighting, Dali meets modern CGI, uncanny and thought-provoking --ar 4:5 --v 7 --s 400 --w 500
```

### Prompt 32: Inflated 3D Object
```
[EVERYDAY OBJECT — e.g., sneaker, handbag, headphones] rendered as if made of inflated glossy balloon material, soft studio lighting, pastel [COLOR] tones, playful and tactile, 3D render with subsurface scattering, minimal clean background --ar 1:1 --v 7 --s 300
```

### Prompt 33: Glass and Refraction
```
[OBJECT — e.g., a chess piece, a skull, a geometric shape] made entirely of clear glass, complex light refraction and caustics, [COLOR] colored light passing through, studio lit on reflective surface, hyper-realistic glass material, octane render --ar 1:1 --v 7 --s 200 --style raw
```

---

## SECTION 6: ARCHITECTURE & INTERIORS

### Prompt 34: Modern Minimalist Interior
```
Interior design photography of a [ROOM — e.g., living room, bedroom, bathroom], minimalist modern style, [KEY ELEMENTS — e.g., floor-to-ceiling windows, concrete walls, oak flooring], natural light flooding in, curated furniture, architectural digest quality, warm and inviting --ar 16:9 --v 7 --s 100 --style raw
```

### Prompt 35: Cozy Atmospheric Interior
```
[ROOM TYPE — e.g., reading nook, cabin living room, bookshop] interior, warm ambient lighting from [LIGHT SOURCE — fireplace, string lights, table lamps], rich textures [LEATHER/WOOD/VELVET], plants, books, lived-in but styled, hygge atmosphere, photography --ar 4:3 --v 7 --s 150
```

### Prompt 36: Futuristic Architecture
```
[BUILDING TYPE — e.g., museum, residence, skyscraper] with futuristic parametric architecture, flowing organic forms, [MATERIAL — white concrete, glass, living moss walls], set in [ENVIRONMENT], dramatic sky, architectural visualization, Zaha Hadid inspired --ar 16:9 --v 7 --s 200
```

### Prompt 37: Japanese Minimalist Space
```
Japanese wabi-sabi interior, [ROOM TYPE], natural materials — raw wood, stone, paper screens, tatami — minimal furniture, single [FOCAL ELEMENT — flower arrangement, ceramic bowl, bonsai], natural light through shoji screens, serene and meditative --ar 3:2 --v 7 --s 150
```

### Prompt 38: Brutalist Architecture
```
Brutalist [BUILDING TYPE] exterior, raw exposed concrete, geometric repetition, dramatic shadows from harsh sunlight, blue sky contrast, [LOCATION/SETTING], architectural photography with a Fuji GFX medium format camera, powerful and imposing --ar 3:4 --v 7 --s 100 --style raw
```

### Prompt 39: Outdoor Living Space
```
[OUTDOOR SPACE — e.g., rooftop terrace, courtyard garden, pool area] at [TIME — golden hour, twilight, midday], [STYLE — Mediterranean, tropical, Scandinavian], lush greenery, comfortable seating, [FEATURES — fire pit, pergola, water feature], aspirational lifestyle photography --ar 16:9 --v 7 --s 120
```

---

## SECTION 7: BRAND & MARKETING VISUALS

### Prompt 40: Hero Image for Website
```
[INDUSTRY — e.g., fintech, wellness, education] brand hero image, [SUBJECT/SCENE — e.g., diverse team collaborating, person using product, abstract brand concept], [BRAND COLORS] color palette, clean modern aesthetic, professional photography suitable for above-the-fold website placement --ar 16:9 --v 7 --s 80 --style raw
```

### Prompt 41: Social Media Graphic Background
```
Abstract background for social media graphic, [COLOR PALETTE — e.g., soft gradient in brand colors], subtle geometric elements, clean negative space in center for text overlay, modern and professional, Instagram post format --ar 1:1 --v 7 --s 200 --no text letters words
```

### Prompt 42: Icon Set Style Guide
```
Set of [NUMBER] icons representing [LIST CONCEPTS — e.g., security, speed, collaboration, growth, analytics], consistent [STYLE — line art, filled, 3D rendered, glassmorphism] style, [COLOR PALETTE], white background, clean and modern, suitable for website or app --ar 1:1 --v 7 --s 200
```

### Prompt 43: Packaging Mockup
```
Product packaging mockup for [PRODUCT TYPE — e.g., coffee bag, supplement bottle, candle], [DESIGN STYLE — minimalist, bold, luxurious, playful], [COLOR SCHEME], displayed on [SURFACE/ENVIRONMENT], studio lighting, premium feel, retail-ready appearance --ar 4:5 --v 7 --s 150
```

### Prompt 44: Brand Lifestyle Photography
```
Lifestyle brand photography for [BRAND TYPE — e.g., outdoor apparel, organic skincare, home goods], [SCENE — e.g., person hiking at sunrise, morning routine in bright bathroom, cooking in stylish kitchen], authentic and aspirational, warm color grade, [DEMOGRAPHIC] model, editorial quality --ar 4:5 --v 7 --s 80 --style raw
```

---

## SECTION 8: TEXTURES, PATTERNS & BACKGROUNDS

### Prompt 45: Seamless Textile Pattern
```
Seamless repeating pattern of [MOTIF — e.g., tropical leaves, geometric shapes, abstract brushstrokes], [COLOR PALETTE], suitable for fabric or wallpaper, [STYLE — hand-drawn, digital, watercolor], balanced density, elegant repeat --ar 1:1 --v 7 --s 300 --tile
```

### Prompt 46: Marble Texture
```
[COLOR — e.g., white Carrara, green verde, black and gold] marble texture, high resolution, natural veining patterns, polished surface with subtle reflections, realistic stone photography, suitable for 3D material or background --ar 1:1 --v 7 --s 50 --style raw --tile
```

### Prompt 47: Abstract Gradient Background
```
Smooth abstract gradient background, [COLORS — e.g., soft peach transitioning to lavender to pale blue], subtle grain texture overlay, atmospheric and dreamy, suitable as wallpaper or presentation background, no distinct objects --ar 16:9 --v 7 --s 200 --no objects people text
```

### Prompt 48: Paper Texture
```
[TYPE — e.g., aged parchment, handmade cotton, Japanese washi, kraft] paper texture, overhead flat view, natural imperfections, subtle fiber detail visible, [COLOR — cream, white, brown, grey], photography of real material --ar 1:1 --v 7 --s 30 --style raw --tile
```

---

## SECTION 9: MOOD & CONCEPT

### Prompt 49: Dark Academia Aesthetic
```
[SCENE — e.g., ancient library interior, study desk with manuscripts, gothic university courtyard], dark academia aesthetic, rich warm tones — burgundy, gold, dark wood, aged leather, candlelight and natural light mixing, moody atmosphere, intellectual and romantic --ar 3:4 --v 7 --s 300
```

### Prompt 50: Solarpunk Utopia
```
Solarpunk [SCENE — e.g., urban rooftop garden, community center, public transit], lush vegetation integrated with modern sustainable architecture, solar panels, diverse community enjoying the space, optimistic and vibrant, golden afternoon light, utopian future --ar 16:9 --v 7 --s 350
```

### Prompt 51: Cyberpunk City
```
Cyberpunk [SCENE — e.g., rainy alley, rooftop view, street market] at night, neon signs in [LANGUAGE — Japanese, Chinese, Korean], volumetric fog, rain-slicked reflective streets, holographic advertisements, dense urban layering, Blade Runner atmosphere --ar 21:9 --v 7 --s 400
```

### Prompt 52: Cottagecore Scene
```
[SCENE — e.g., kitchen with fresh-baked bread, flower garden, reading by the fire], cottagecore aesthetic, soft warm morning light, vintage floral elements, handmade details, wildflowers, pastoral and peaceful, nostalgic and comforting --ar 4:5 --v 7 --s 350
```

### Prompt 53: Liminal Space
```
[LIMINAL SPACE — e.g., empty shopping mall at 3am, endless hotel corridor, backrooms office], unsettling emptiness, fluorescent lighting with slight flicker, no people, slightly wrong proportions, nostalgic yet eerie, liminal space photography --ar 16:9 --v 7 --s 100 --style raw --w 500
```

---

## SECTION 10: CINEMATIC & STORYTELLING

### Prompt 54: Film Still — Drama
```
Film still from an unreleased [DECADE — 1970s, 1990s, 2020s] [GENRE — thriller, romance, drama], [SCENE DESCRIPTION], [ACTOR DESCRIPTION — do not name real actors], cinematic lighting, anamorphic bokeh, color graded in [PALETTE], 35mm film grain, directed by [STYLE REFERENCE — e.g., in the style of Denis Villeneuve] --ar 2.35:1 --v 7 --s 250
```

### Prompt 55: Documentary Moment
```
Documentary photography, [SCENE — e.g., street vendor preparing food, musician performing on subway, farmer at dawn], candid and unposed, natural available light, photojournalistic framing, emotional authenticity, Magnum Photos quality --ar 3:2 --v 7 --s 50 --style raw
```

### Prompt 56: Double Exposure Effect
```
Double exposure photograph combining [SUBJECT 1 — e.g., portrait of a woman] with [SUBJECT 2 — e.g., forest trees, city skyline, ocean waves], artistic blend, silhouette of first subject filled with second image, moody color grade in [COLORS], fine art photography --ar 3:4 --v 7 --s 400
```

### Prompt 57: Vintage Film Photography
```
[SCENE/SUBJECT], shot on expired [FILM STOCK — Kodak Portra 400, Fuji Velvia, Kodachrome, Cinestill 800T], [ERA — 1970s, 1980s, 1990s] aesthetic, light leaks, [WARM/COOL] color cast, visible grain, slightly imperfect focus, nostalgic feeling, found photograph quality --ar 3:2 --v 7 --s 150 --style raw
```

---

## SECTION 11: SPECIAL TECHNIQUES

### Prompt 58: Tilt-Shift Miniature Effect
```
[LARGE SCENE — e.g., cityscape, beach, construction site, train station] photographed with tilt-shift lens creating miniature model effect, extreme shallow depth of field at top and bottom, saturated colors, overhead or elevated angle, tiny world illusion --ar 16:9 --v 7 --s 100 --style raw
```

### Prompt 59: Cross-Section Illustration
```
Cross-section view of [SUBJECT — e.g., a cruise ship, underground ant colony, a tree with root system, a volcano], educational illustration style, cutaway revealing interior details, labeled layers, scientific yet beautiful, detailed and accurate --ar 3:4 --v 7 --s 300
```

### Prompt 60: Knolling / Organized Flat Lay
```
Knolling arrangement of [OBJECTS — e.g., all components of a mechanical watch, camping gear, artist's supplies], every item organized at right angles on [BACKGROUND COLOR] background, overhead view, satisfying organization, even studio lighting, no shadows --ar 1:1 --v 7 --s 100 --style raw
```

### Prompt 61: Before/After Split
```
Split image: left side shows [BEFORE STATE — e.g., abandoned building, overgrown garden, messy room], right side shows [AFTER STATE — e.g., renovated modern space, manicured garden, organized room], clean vertical split line, same camera angle both sides, transformation concept --ar 16:9 --v 7 --s 100
```

### Prompt 62: Cinemagraph Concept
```
[SCENE WITH ONE MOVING ELEMENT — e.g., woman at cafe with steam rising from coffee, person standing still while crowd blurs past, candle flame in otherwise still room], suggesting frozen moment with one element of implied motion, atmospheric, cinematic --ar 16:9 --v 7 --s 150
```

---

## SECTION 12: STYLE MODIFIERS LIBRARY

### Lighting Modifiers
Use these at the end of any prompt to control lighting:
```
, golden hour sunlight
, blue hour twilight
, harsh midday sun with deep shadows
, overcast soft diffused light
, dramatic chiaroscuro lighting
, neon-lit
, candlelit
, backlit silhouette
, volumetric god rays
, studio Rembrandt lighting
, ring light catchlights
, practical lighting only
```

### Camera/Lens Modifiers
```
, shot on Hasselblad medium format
, Leica 35mm street photography
, Canon 85mm f/1.2 shallow DOF
, fisheye lens distortion
, macro lens extreme closeup
, tilt-shift lens miniature effect
, infrared photography
, Polaroid instant film
, disposable camera aesthetic
, drone aerial DJI
```

### Mood/Atmosphere Modifiers
```
, ethereal and dreamlike
, gritty and raw
, serene and contemplative
, chaotic and energetic
, melancholic and nostalgic
, whimsical and playful
, dark and ominous
, warm and inviting
, sterile and clinical
, lush and abundant
```

### Art Movement Modifiers
```
, Art Deco geometric elegance
, Bauhaus functional minimalism
, Impressionist loose brushwork
, Surrealist impossible reality
, Pop Art bold graphic
, Ukiyo-e Japanese woodblock
, Art Nouveau organic flowing
, De Stijl primary colors and grids
, Romanticism dramatic nature
, Constructivist bold angular
```

### Texture/Material Modifiers
```
, oil painting thick impasto texture
, pencil sketch crosshatch shading
, collage mixed media
, embroidered textile art
, stained glass
, ceramic glazed
, carved wood relief
, etched metal engraving
, risograph print misalignment
, screen print limited palette
```

---

## PRO TIPS FOR V7

**1. Prompt Structure Formula:**
```
[Subject] + [Environment/Setting] + [Style/Medium] + [Lighting] + [Camera/Technical] + [Mood] + --parameters
```

**2. Getting More Photorealistic:**

- Add `--style raw` to reduce Midjourney's artistic interpretation
- Lower `--stylize` to 30-80
- Reference specific cameras and lenses
- Mention "photography" or "photograph" explicitly

**3. Getting More Artistic:**

- Increase `--stylize` to 300-750
- Reference art movements or specific artists' styles
- Use medium descriptors (oil painting, watercolor, charcoal)
- Add `--chaos 20-50` for more variation

**4. Consistent Characters Across Images:**

- Use `--seed` with the same number across prompts
- Describe the character identically each time
- Use character reference with `--cref [URL]`
- Keep styling/environment descriptions consistent

**5. Avoiding Common Mistakes:**

- Don't overload prompts — 40-60 words is the sweet spot
- Put the most important elements first
- Use `--no` for things you DON'T want (e.g., `--no text watermark`)
- Commas separate concepts; the model weighs earlier words more heavily

**6. Batch Workflow:**

- Generate with `--chaos 40` first to explore variations
- Pick your favorite, grab its `--seed`
- Re-run with `--chaos 0` and refined prompt for consistency
- Use `--s 750` for maximum Midjourney aesthetic or `--s 30` for literal interpretation
