# Stable Diffusion Prompt Vault

> 50+ Stable Diffusion prompts with positive/negative prompt pairs, recommended models, sampler settings, and CFG guidance. Copy directly into Automatic1111, ComfyUI, or Forge.

---

## QUICK REFERENCE: RECOMMENDED SETTINGS

| Use Case | Model | Sampler | Steps | CFG Scale |
|----------|-------|---------|-------|-----------|
| Photorealistic | RealVisXL V5 / Juggernaut XL | DPM++ 2M Karras | 30-40 | 5-7 |
| Anime/Illustration | Animagine XL 3.1 / CounterfeitXL | Euler a | 25-35 | 7-9 |
| General Purpose | SDXL Base + Refiner | DPM++ SDE Karras | 30 | 7 |
| Artistic/Painterly | DreamShaper XL | DPM++ 2M Karras | 30-40 | 7-8 |
| Cinematic | CinematicRedmond | DPM++ 2M Karras | 35 | 6-7 |
| Product Shots | Realistic Vision V5 | DPM++ 2M Karras | 30 | 5-6 |

### Key Settings Explained
- **CFG Scale:** How strictly the model follows your prompt. 5-7 = creative freedom, 8-12 = strict adherence, 12+ = often over-cooked
- **Steps:** More steps = more detail but diminishing returns past 40. 25-35 is the sweet spot.
- **Sampler:** DPM++ 2M Karras is the reliable all-rounder. Euler a is fast and good for anime.
- **Resolution (SDXL):** 1024x1024, 1152x896, 896x1152, 1216x832, 832x1216

---

## SECTION 1: PHOTOREALISTIC PORTRAITS

### Prompt 1: Studio Beauty Portrait
**Positive:**
```
RAW photo, close-up portrait of a beautiful woman with [HAIR COLOR] hair and [EYE COLOR] eyes, professional studio lighting, softbox key light, subtle rim light, neutral gray background, Canon EOS R5, 85mm lens, f/2.0, sharp focus on eyes, natural skin texture, pores visible, professional retouching, 8k uhd, high quality
```
**Negative:**
```
(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 35 steps | CFG 5.5 | 896x1152

---

### Prompt 2: Environmental Portrait
**Positive:**
```
cinematic photo of a [AGE] year old [GENDER] [ETHNICITY] [PROFESSION], standing in [THEIR WORK ENVIRONMENT], natural window light, environmental portrait, documentary style, authentic expression, weathered hands, storytelling composition, Fujifilm X-T4, 56mm f/1.2, shallow depth of field, film grain
```
**Negative:**
```
(anime, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch), posing, fake smile, studio background, smooth skin, plastic, oversaturated, bad anatomy, deformed, extra limbs, poorly drawn face, mutation, watermark
```
**Settings:** RealVisXL V5 | DPM++ SDE Karras | 30 steps | CFG 6 | 1152x896

---

### Prompt 3: Fashion Editorial
**Positive:**
```
high fashion editorial photograph, model wearing [DESCRIBE OUTFIT], [POSE], dramatic directional lighting, hard shadows, [BACKGROUND — white studio / urban alley / minimalist set], shot for Vogue magazine, Peter Lindbergh style, black and white, high contrast, strong composition, medium format camera quality
```
**Negative:**
```
(worst quality, low quality, normal quality), text, watermark, amateur, poorly lit, flat lighting, soft focus, blurry, oversaturated colors, bad anatomy, deformed, extra fingers, mutated, ugly, disfigured
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 35 steps | CFG 7 | 832x1216

---

### Prompt 4: Headshot Professional
**Positive:**
```
professional corporate headshot, [GENDER] [AGE RANGE] [DESCRIPTION], wearing [BUSINESS ATTIRE], confident warm smile, eyes sharp, Profoto studio lighting with softbox, clean [COLOR] backdrop, LinkedIn photo quality, upper body framing, polished professional appearance, Canon 85mm f/1.4
```
**Negative:**
```
(cartoon, anime, illustration, painting), casual clothing, harsh shadows, dark circles, blemishes exaggerated, blurry, pixelated, bad anatomy, deformed face, extra fingers, poorly drawn, low resolution
```
**Settings:** Realistic Vision V5 | DPM++ 2M Karras | 30 steps | CFG 5 | 832x1216

---

### Prompt 5: Street Photography Portrait
**Positive:**
```
candid street portrait of a [PERSON DESCRIPTION] in [CITY], golden hour backlight creating hair rim light, urban environment with bokeh, shot on Leica M11 with 50mm Summilux, photojournalistic style, authentic emotion, natural available light, slight grain, decisive moment
```
**Negative:**
```
(posed, stiff, studio, cartoon, anime, illustration), looking directly at camera, fake expression, smooth plastic skin, text, watermark, bad anatomy, deformed, low quality
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 30 steps | CFG 5 | 1152x896

---

## SECTION 2: LANDSCAPES & NATURE

### Prompt 6: Epic Mountain Scene
**Positive:**
```
breathtaking landscape photograph of [MOUNTAIN/LOCATION], golden hour, dramatic clouds, snow-capped peaks reflected in crystal alpine lake, wildflowers in foreground, depth and layers, National Geographic quality, Nikon Z9, 14-24mm wide angle, hyper detailed, 8k resolution
```
**Negative:**
```
(painting, illustration, cartoon, anime, drawing), people, text, watermark, flat, boring, oversaturated, HDR look, low quality, blurry, artifacts, overprocessed
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 40 steps | CFG 6 | 1216x832

---

### Prompt 7: Moody Forest
**Positive:**
```
atmospheric photograph of a [FOREST TYPE — e.g., ancient redwood, misty bamboo, snowy birch] forest, volumetric fog filtering through canopy, rays of light penetrating, moss-covered ground, depth and mystery, fine art landscape photography, medium format film quality, ethereal mood
```
**Negative:**
```
(cartoon, anime, illustration, 3d render), people, animals, text, watermark, overexposed, flat lighting, ugly, low quality, blurry, amateur
```
**Settings:** DreamShaper XL | DPM++ SDE Karras | 35 steps | CFG 7 | 832x1216

---

### Prompt 8: Dramatic Seascape
**Positive:**
```
long exposure seascape photograph, [LOCATION/DESCRIPTION], dramatic storm clouds, silky smooth water from 30 second exposure, jagged rocks in foreground, golden hour light breaking through clouds, fine art photography, Lee filters, tripod shot, medium format camera, dynamic range
```
**Negative:**
```
(cartoon, painting, illustration, digital art), people, boats, text, watermark, overprocessed, HDR, flat, boring composition, low quality
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 35 steps | CFG 5.5 | 1216x832

---

### Prompt 9: Macro Nature
**Positive:**
```
extreme macro photograph of [SUBJECT — e.g., dewdrops on a leaf, butterfly wing scales, frost crystals on glass], razor-thin depth of field, creamy bokeh, backlit, natural colors, focus-stacked sharpness, Canon MP-E 65mm, scientific detail, nature photography
```
**Negative:**
```
(illustration, painting, cartoon, sketch), blurry, out of focus, flat lighting, text, watermark, low quality, artificial, plastic
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 30 steps | CFG 5 | 1024x1024

---

### Prompt 10: Desert Minimalist
**Positive:**
```
minimalist desert landscape, [LOCATION — e.g., Sahara, White Sands, Namib], single [SUBJECT — lone tree, tiny figure, camel caravan] for scale, vast negative space, geometric shadow patterns on sand dunes, fine art photography, serene and meditative, warm golden tones
```
**Negative:**
```
(cartoon, illustration, busy, cluttered), text, watermark, people crowds, vehicles, buildings, low quality, overprocessed, flat
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 35 steps | CFG 5 | 1216x832

---

## SECTION 3: PRODUCT PHOTOGRAPHY

### Prompt 11: Luxury Product Hero Shot
**Positive:**
```
professional product photography of [PRODUCT — e.g., premium watch, perfume bottle, skincare jar], placed on [SURFACE — polished marble, dark slate, white acrylic], dramatic studio lighting, hard shadow on one side, [ACCENT COLOR] gradient background, sharp focus, commercial photography, advertising quality
```
**Negative:**
```
(cartoon, illustration, 3d render, anime), blurry, low quality, bad lighting, amateur, text on product, watermark, reflections of photographer, dusty
```
**Settings:** Realistic Vision V5 | DPM++ 2M Karras | 35 steps | CFG 5 | 1024x1024

---

### Prompt 12: Food Photography
**Positive:**
```
professional food photography of [DISH DESCRIPTION], on [PLATE/SURFACE], styled with [PROPS — fresh herbs, linen napkin, rustic cutlery], [ANGLE — overhead 90 degree / 45 degree / eye level], soft natural window light from left, shallow depth of field, warm tones, appetizing, cookbook quality
```
**Negative:**
```
(cartoon, illustration, 3d, anime), artificial looking, plastic food, bad lighting, harsh flash, amateur, blurry, oversaturated, text, watermark, ugly plating
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 30 steps | CFG 5.5 | 1024x1024

---

### Prompt 13: Flat Lay Product Arrangement
**Positive:**
```
overhead flat lay photograph of [PRODUCTS/ITEMS — e.g., skincare collection, coffee accessories, desk setup], arranged on [SURFACE — white marble, linen fabric, wooden table], natural daylight, styled with [PROPS — dried flowers, fabric swatches, greenery], clean aesthetic, Instagram lifestyle brand quality
```
**Negative:**
```
(illustration, cartoon, 3d render), cluttered, messy, bad lighting, harsh shadows, text, watermark, blurry, low quality, amateur styling
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 30 steps | CFG 5 | 1024x1024

---

### Prompt 14: Tech Product Floating
**Positive:**
```
[TECH PRODUCT — e.g., wireless earbuds, smartphone, laptop] floating at dynamic angle, dark studio environment, [COLOR — blue, purple, orange] rim lighting from behind, particle effects, reflective dark surface below, minimal composition, Apple-style product photography, ultra clean render
```
**Negative:**
```
(cartoon, anime, hand-drawn), text, fingerprints, scratches, dust, wires, cluttered background, bad reflections, low quality, blurry
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 35 steps | CFG 7 | 1216x832

---

### Prompt 15: Cosmetics with Texture Splash
**Positive:**
```
[COSMETIC PRODUCT — e.g., lipstick, foundation bottle, eyeshadow palette] with dynamic splash of [TEXTURE — liquid, powder, cream] frozen in mid-air around the product, [BACKGROUND COLOR] studio background, high-speed photography effect, commercial beauty advertising quality
```
**Negative:**
```
(cartoon, amateur, sketch), messy, uncontrolled, blurry, text, watermark, low quality, bad composition, dull colors
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 35 steps | CFG 7 | 832x1216

---

## SECTION 4: ILLUSTRATION & DIGITAL ART

### Prompt 16: Fantasy Concept Art
**Positive:**
```
epic fantasy concept art of [SCENE — e.g., dragon perched on ancient ruins, elven forest city, underwater kingdom], volumetric lighting, atmospheric perspective, intricate details, painterly brushstrokes, dramatic scale, cinematic composition, trending on ArtStation, masterpiece quality
```
**Negative:**
```
(photo, photorealistic, photography), blurry, low quality, bad anatomy, extra limbs, text, watermark, signature, frame, border, amateur, flat colors
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 35 steps | CFG 7.5 | 1216x832

---

### Prompt 17: Character Design Sheet
**Positive:**
```
character design sheet of [CHARACTER DESCRIPTION — e.g., female warrior with red armor, friendly robot companion, young wizard], multiple angles (front, side, back, three-quarter), consistent design, clean white background, professional concept art, detailed costume design, color annotations
```
**Negative:**
```
(photo, photorealistic), inconsistent design between views, blurry, bad anatomy, extra limbs, text, watermark, low quality, dark background, cluttered
```
**Settings:** Animagine XL 3.1 or DreamShaper XL | Euler a | 30 steps | CFG 8 | 1216x832

---

### Prompt 18: Children's Book Illustration
**Positive:**
```
charming children's book illustration of [SCENE — e.g., a fox and rabbit having tea in a cozy burrow], gouache painting style, warm color palette, whimsical details, soft rounded shapes, gentle lighting, storytelling composition, picture book quality, heartwarming
```
**Negative:**
```
(photorealistic, photo, 3d render), scary, dark, violent, creepy, text, watermark, bad anatomy, ugly, low quality, adult content
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 30 steps | CFG 8 | 1152x896

---

### Prompt 19: Anime Character
**Positive:**
```
masterpiece, best quality, 1[GIRL/BOY], [HAIR DESCRIPTION], [EYE COLOR] eyes, [OUTFIT DESCRIPTION], [POSE], [SETTING — e.g., cherry blossom garden, rooftop at sunset, library], dynamic angle, detailed shading, vibrant colors, expressive, anime illustration
```
**Negative:**
```
(worst quality, low quality, normal quality), bad anatomy, bad hands, extra fingers, fewer fingers, extra limbs, bad proportions, ugly, duplicate, morbid, mutilated, deformed, blurry, text, watermark
```
**Settings:** Animagine XL 3.1 | Euler a | 28 steps | CFG 7 | 832x1216

---

### Prompt 20: Botanical Scientific Illustration
**Positive:**
```
detailed botanical illustration of [PLANT — e.g., rosa damascena, monstera deliciosa, lavender], scientific accuracy, showing flower, leaf, stem, and root structures, white background, fine linework with watercolor fills, vintage botanical plate style, educational
```
**Negative:**
```
(photo, photorealistic, 3d render), blurry, low quality, inaccurate anatomy, text, watermark, dark background, modern digital art style
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 35 steps | CFG 8 | 832x1216

---

### Prompt 21: Retro Poster Art
**Positive:**
```
vintage [DECADE — 1950s, 1960s, 1970s] travel poster for [LOCATION], flat color illustration, limited color palette, bold geometric shapes, screen print texture, retro typography space at top, nostalgic and optimistic mood, mid-century modern design
```
**Negative:**
```
(photorealistic, photo, 3d), modern style, gradients, complex shading, text, watermark, low quality, busy composition, too many colors
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 30 steps | CFG 8 | 832x1216

---

## SECTION 5: CINEMATIC & MOODY

### Prompt 22: Film Noir Scene
**Positive:**
```
film noir scene, [DESCRIPTION — e.g., detective in trench coat under streetlamp, femme fatale in smoky bar], black and white, high contrast, dramatic shadows, venetian blind light pattern, rain-wet streets reflecting light, 1940s aesthetic, cinematic composition, moody and atmospheric
```
**Negative:**
```
(color, colorful, bright, cheerful), cartoon, anime, low quality, blurry, bad anatomy, text, watermark, modern elements
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 35 steps | CFG 7 | 1216x832

---

### Prompt 23: Cyberpunk Street
**Positive:**
```
cyberpunk city street at night, [SCENE DETAILS — e.g., food vendor stall, neon signs in Asian characters, crowded alley], rain falling, neon reflections on wet pavement, holographic advertisements, dense urban environment, volumetric fog, Blade Runner atmosphere, cinematic lighting
```
**Negative:**
```
(cartoon, anime style, bright daylight), empty, clean, sterile, text, watermark, blurry, low quality, bad anatomy, deformed people
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 35 steps | CFG 7.5 | 1216x832

---

### Prompt 24: Golden Hour Cinematic
**Positive:**
```
cinematic still, [SUBJECT — e.g., person walking through wheat field, couple on empty highway, child running through sprinklers], golden hour backlight, lens flare, warm color grade, shallow depth of field, anamorphic bokeh, shot on Arri Alexa, emotional and nostalgic
```
**Negative:**
```
(cartoon, anime, illustration, painting), harsh midday light, flat lighting, ugly, low quality, blurry, bad anatomy, text, watermark, overprocessed
```
**Settings:** CinematicRedmond | DPM++ 2M Karras | 35 steps | CFG 6 | 1216x832

---

### Prompt 25: Horror Atmospheric
**Positive:**
```
atmospheric horror scene, [DESCRIPTION — e.g., abandoned hospital corridor, figure standing at end of foggy road, old house with single lit window], unsettling mood, desaturated colors, heavy fog, low-key lighting, film grain, found footage quality, psychological horror
```
**Negative:**
```
(bright, cheerful, cartoon, anime), gore, blood, text, watermark, low quality, blurry, bad anatomy, overexposed
```
**Settings:** DreamShaper XL | DPM++ SDE Karras | 35 steps | CFG 7 | 1216x832

---

### Prompt 26: Vintage Film Look
**Positive:**
```
[SCENE/SUBJECT], shot on expired [FILM STOCK — Kodak Portra 400, Fuji Velvia, Kodachrome], [ERA — 1970s, 1980s] aesthetic, light leaks, [WARM/COOL] color cast, visible grain, slightly soft focus, nostalgic feeling, found photograph quality, analog imperfections
```
**Negative:**
```
(digital, clean, modern, sharp, perfect), cartoon, anime, text, watermark, low quality, 3d render
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 30 steps | CFG 5.5 | 1152x896

---

## SECTION 6: ARCHITECTURE & INTERIORS

### Prompt 27: Modern Interior Design
**Positive:**
```
interior design photography of a [ROOM — living room, bedroom, kitchen], [STYLE — minimalist modern, Scandinavian, mid-century, Japanese], [KEY FEATURES — floor-to-ceiling windows, built-in shelving, marble island], natural light flooding in, styled with [DETAILS — plants, books, art], Architectural Digest quality, warm and inviting
```
**Negative:**
```
(cartoon, illustration, 3d render, anime), cluttered, messy, dated, ugly furniture, bad proportions, distorted perspective, text, watermark, low quality
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 35 steps | CFG 5.5 | 1216x832

---

### Prompt 28: Cozy Atmospheric Room
**Positive:**
```
cozy [ROOM — reading nook, cabin interior, bookshop corner], warm ambient lighting from [SOURCE — fireplace, candles, string lights, table lamps], rich textures — [MATERIALS — velvet, worn leather, knitted throws, dark wood], stacked books, indoor plants, rain visible through window, hygge atmosphere
```
**Negative:**
```
(cartoon, anime, illustration, clinical, sterile), bright harsh lighting, modern minimalist, empty, cold, text, watermark, low quality, blurry
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 35 steps | CFG 7 | 1152x896

---

### Prompt 29: Futuristic Architecture
**Positive:**
```
architectural visualization of a futuristic [BUILDING TYPE — museum, residence, office tower], parametric organic forms, [MATERIALS — white concrete, curved glass, living green walls], integrated with landscape, dramatic sky, golden hour light, photorealistic render quality, Zaha Hadid inspired
```
**Negative:**
```
(cartoon, low poly, sketch), ugly, boring, generic box building, bad proportions, unrealistic scale, text, watermark, low quality, people in foreground
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 40 steps | CFG 6 | 1216x832

---

### Prompt 30: Japanese Minimalist Space
**Positive:**
```
Japanese wabi-sabi interior, [ROOM TYPE — tea room, bedroom, entryway], natural materials — raw wood, stone, paper screens, tatami, minimal furniture, single [FOCAL ELEMENT — flower arrangement, ceramic bowl, bonsai], natural light through shoji screens, serene and meditative, imperfect beauty
```
**Negative:**
```
(modern, flashy, cluttered, cartoon), bright colors, plastic, chrome, text, watermark, low quality, Western furniture, busy decor
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 35 steps | CFG 7 | 1216x832

---

## SECTION 7: ABSTRACT & CREATIVE

### Prompt 31: Fluid Abstract Art
**Positive:**
```
abstract fluid art, [COLOR PALETTE — e.g., deep ocean blues and molten gold, iridescent pastels, black and crimson], organic flowing shapes, high contrast, studio lit against dark background, liquid simulation frozen in time, mesmerizing detail, fine art photography of fluid dynamics
```
**Negative:**
```
(text, face, person, recognizable objects), blurry, muddy colors, low resolution, boring, flat, jpeg artifacts
```
**Settings:** DreamShaper XL | DPM++ SDE Karras | 30 steps | CFG 8 | 1024x1024

---

### Prompt 32: Geometric Abstract
**Positive:**
```
abstract geometric composition, [SHAPES — interconnected polyhedra, tessellated triangles, flowing curves], [COLOR PALETTE], dramatic directional lighting casting crisp shadows, floating against [BACKGROUND — void, gradient, textured wall], mathematical precision, 3D rendered, clean and modern
```
**Negative:**
```
(photo, person, face, text), blurry, messy, chaotic, low quality, pixelated, boring, flat colors
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 30 steps | CFG 7.5 | 1024x1024

---

### Prompt 33: Surreal Dreamscape
**Positive:**
```
surreal dreamscape, [SCENE — e.g., staircase leading into clouds, room with ocean floor, desert with floating islands], impossible physics, photorealistic rendering of impossible scene, dramatic lighting, Salvador Dali meets modern CGI, thought-provoking, cinematic composition
```
**Negative:**
```
(cartoon, sketch, amateur), blurry, low quality, bad composition, flat lighting, text, watermark, boring, generic
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 35 steps | CFG 7 | 1216x832

---

### Prompt 34: Double Exposure
**Positive:**
```
double exposure effect, silhouette of [SUBJECT 1 — e.g., woman's profile, wolf, tree] filled with [SUBJECT 2 — e.g., starry night sky, forest, ocean waves, city skyline], artistic blend, moody color grade, fine art photography, creative concept, black background
```
**Negative:**
```
(cartoon, anime, simple), cluttered, confusing composition, blurry, low quality, text, watermark, bad blend, harsh edges
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 35 steps | CFG 7.5 | 832x1216

---

## SECTION 8: TEXTURES & PATTERNS

### Prompt 35: Seamless Fabric Pattern
**Positive:**
```
seamless repeating pattern, [MOTIF — e.g., tropical monstera leaves, geometric art deco, delicate florals, abstract brushstrokes], [COLOR PALETTE], fabric print design, balanced density, elegant repeat, suitable for textile, clean edges
```
**Negative:**
```
(3d, photorealistic, person, face), uneven spacing, cut off elements at edges, blurry, low quality, text, watermark
```
**Settings:** SDXL Base | DPM++ 2M Karras | 30 steps | CFG 7 | 1024x1024 (use Tiling option)

---

### Prompt 36: Material Texture
**Positive:**
```
high resolution texture of [MATERIAL — e.g., aged leather, brushed copper, weathered wood, rough concrete, woven linen], flat lit, overhead view, natural color and detail, tileable, material reference quality, 4k detail
```
**Negative:**
```
(objects, person, text, 3d scene), uneven lighting, harsh shadows, low quality, blurry, color cast
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 25 steps | CFG 4 | 1024x1024 (use Tiling option)

---

## SECTION 9: STYLIZED & ARTISTIC

### Prompt 37: Oil Painting Portrait
**Positive:**
```
oil painting portrait of [SUBJECT DESCRIPTION], thick impasto brushstrokes visible, [COLOR PALETTE — warm earth tones / rich jewel tones], dramatic chiaroscuro lighting, classical composition, museum quality, reminiscent of [ARTIST — Rembrandt, Sargent, Vermeer], canvas texture visible
```
**Negative:**
```
(photorealistic, photograph, digital art, smooth), flat, blurry, amateur, bad anatomy, text, watermark, frame, border
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 35 steps | CFG 8 | 832x1216

---

### Prompt 38: Watercolor Landscape
**Positive:**
```
watercolor painting of [LANDSCAPE — e.g., coastal village, autumn forest path, lavender field], loose expressive brushwork, wet-on-wet technique, color bleeding and blooming, white paper visible in highlights, atmospheric perspective, artistic imperfection, plein air quality
```
**Negative:**
```
(photorealistic, photograph, 3d render, digital), overworked, tight and controlled, dark, text, watermark, frame, border, low quality
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 30 steps | CFG 8 | 1152x896

---

### Prompt 39: Studio Ghibli Style
**Positive:**
```
[SCENE DESCRIPTION — e.g., girl riding bicycle through countryside, magical forest with spirits, seaside town], Studio Ghibli animation style, hand-painted background quality, lush nature, fluffy cumulus clouds, warm sunlight, nostalgic and peaceful, detailed environment art
```
**Negative:**
```
(photorealistic, photo, 3d, western cartoon), dark, scary, violent, low quality, blurry, text, watermark, bad anatomy
```
**Settings:** Animagine XL 3.1 or DreamShaper XL | Euler a | 28 steps | CFG 7 | 1216x832

---

### Prompt 40: Pixel Art
**Positive:**
```
pixel art of [SCENE/CHARACTER — e.g., cozy coffee shop interior, knight with sword, forest clearing], 32-bit era style, limited color palette, clean pixel placement, [MOOD — warm, nostalgic, dramatic], retro game aesthetic, detailed environment, sprite art quality
```
**Negative:**
```
(photorealistic, 3d render, smooth gradients, blurry), anti-aliased, modern style, text, watermark, low quality
```
**Settings:** DreamShaper XL | Euler a | 25 steps | CFG 8 | 1024x1024

---

### Prompt 41: Art Nouveau
**Positive:**
```
Art Nouveau illustration of [SUBJECT — e.g., woman with flowing hair surrounded by flowers], ornate decorative border, flowing organic lines, muted jewel-tone palette, gold accents, Alphonse Mucha inspired, poster composition, intricate floral details, elegant and romantic
```
**Negative:**
```
(photorealistic, photo, modern, minimalist), plain, boring, low detail, text, watermark, bad anatomy, low quality, simple
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 35 steps | CFG 8 | 832x1216

---

## SECTION 10: PEOPLE & LIFESTYLE

### Prompt 42: Candid Lifestyle
**Positive:**
```
candid lifestyle photograph of [PERSON — young woman, couple, family, friends] [ACTIVITY — cooking together, laughing at cafe, walking through market, working at laptop], natural available light, authentic unposed moment, shallow depth of field, warm color grade, editorial lifestyle quality
```
**Negative:**
```
(posed, stiff, awkward, cartoon, illustration), looking at camera, bad anatomy, extra fingers, deformed, text, watermark, low quality, blurry, studio background
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 30 steps | CFG 5 | 1152x896

---

### Prompt 43: Fitness/Wellness
**Positive:**
```
[FITNESS SCENE — woman doing yoga at sunrise on beach, athlete mid-sprint, meditation in minimal studio], athletic physique, dynamic energy, [LIGHTING — golden backlight, clean studio, natural outdoor], activewear, healthy glow, fitness brand photography quality, inspirational mood
```
**Negative:**
```
(cartoon, anime, illustration), unnatural pose, bad anatomy, extra limbs, deformed muscles, text, watermark, low quality, blurry, inappropriate
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 30 steps | CFG 5.5 | 896x1152

---

### Prompt 44: Travel/Adventure
**Positive:**
```
travel photography, [PERSON] standing at [EPIC LOCATION — edge of cliff, ancient temple doorway, narrow European street], back to camera or side profile, sense of wonder and adventure, dramatic landscape, golden hour, backpack, wanderlust mood, National Geographic quality
```
**Negative:**
```
(cartoon, illustration, posed, selfie), looking at camera, bad anatomy, deformed, text, watermark, low quality, blurry, touristy, crowded
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 30 steps | CFG 6 | 896x1152

---

## SECTION 11: SPECIAL EFFECTS & TECHNIQUES

### Prompt 45: Smoke/Particle Effect
**Positive:**
```
[SUBJECT — portrait, dancer, object] surrounded by [EFFECT — swirling colored smoke, disintegrating into particles, emerging from dust cloud], dramatic studio lighting, [COLOR] against dark background, high-speed photography freeze effect, cinematic and dramatic
```
**Negative:**
```
(cartoon, simple, flat), blurry, low quality, bad anatomy, text, watermark, boring, muddy colors
```
**Settings:** DreamShaper XL | DPM++ SDE Karras | 35 steps | CFG 7 | 832x1216

---

### Prompt 46: Miniature/Tilt-Shift
**Positive:**
```
tilt-shift miniature effect photograph of [LARGE SCENE — city intersection, beach, construction site], selective focus creating toy model illusion, overhead or elevated angle, saturated colors, small people and vehicles looking like figurines, playful perspective trick
```
**Negative:**
```
(cartoon, illustration, normal perspective), all in focus, flat, boring, text, watermark, low quality, dark
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 30 steps | CFG 5.5 | 1216x832

---

### Prompt 47: Glass Material Object
**Positive:**
```
[OBJECT — e.g., chess piece, skull, geometric shape, animal] made entirely of clear glass, complex light refraction and caustics, [COLOR] colored light passing through, studio lit on reflective surface, hyper-realistic glass material, pristine, octane render quality
```
**Negative:**
```
(cartoon, flat, matte, opaque), fingerprints, dust, scratches, low quality, blurry, text, watermark, dark
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 40 steps | CFG 7 | 1024x1024

---

### Prompt 48: Infrared Photography
**Positive:**
```
infrared photography of [SCENE — forest, park, landscape with trees], false color effect, vegetation rendered in white and pink, dark dramatic sky, dreamlike surreal quality, ethereal and otherworldly, fine art photography, 720nm infrared filter
```
**Negative:**
```
(normal colors, green trees, cartoon, illustration), low quality, blurry, text, watermark, boring, amateur
```
**Settings:** RealVisXL V5 | DPM++ 2M Karras | 30 steps | CFG 6 | 1216x832

---

### Prompt 49: Stained Glass Art
**Positive:**
```
[SUBJECT — e.g., peacock, tree of life, landscape, angel] depicted as stained glass window, lead came lines separating colored glass sections, light shining through from behind, rich jewel-tone colors, cathedral quality craftsmanship, intricate details, backlit glow
```
**Negative:**
```
(photorealistic, painting, sketch), flat, no light effect, boring, low quality, blurry, text, watermark, modern
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 35 steps | CFG 8 | 832x1216

---

### Prompt 50: Collage Mixed Media
**Positive:**
```
mixed media collage artwork featuring [SUBJECT/THEME], combining torn paper textures, vintage photographs, painted elements, newspaper clippings, washi tape, layered composition, contemporary art, [COLOR PALETTE], textured and tactile quality
```
**Negative:**
```
(photorealistic, clean, digital, smooth), boring, flat, simple, text, watermark, low quality, uniform texture
```
**Settings:** DreamShaper XL | DPM++ 2M Karras | 30 steps | CFG 8 | 1024x1024

---

## ADVANCED TECHNIQUES

### Prompt Weighting (A1111 Syntax)
Control emphasis using parentheses and numbers:
```
(important element:1.3) — increases weight by 30%
(less important:0.7) — decreases weight by 30%
((double parens)) — approximately 1.21x weight
[brackets] — decreases weight
```

**Example:**
```
(beautiful woman:1.2) standing in a (misty forest:1.4), wearing a flowing white dress, (dramatic volumetric lighting:1.3), cinematic
```

### BREAK Keyword
Force attention reset to ensure later tokens get attention:
```
portrait of a woman with red hair, green eyes, freckles BREAK autumn forest background, golden hour sunlight, shallow depth of field BREAK photorealistic, high quality, 8k
```

### ControlNet Tips
- **Canny:** Best for preserving edges/outlines from a reference image
- **Depth:** Best for maintaining spatial composition
- **OpenPose:** Best for controlling human poses precisely
- **IP-Adapter:** Best for style transfer from reference images
- **Tile:** Best for upscaling while adding detail

### Upscale Workflow
1. Generate at base resolution (1024x1024 for SDXL)
2. Use img2img at 0.3-0.4 denoise strength at 2x resolution
3. OR use Ultimate SD Upscale with 4x-UltraSharp model
4. OR use Tiled Diffusion for very large outputs

### LoRA Usage Tips
- Weight 0.6-0.8 for style LoRAs (full weight can overpower)
- Weight 0.8-1.0 for character/subject LoRAs
- Stack max 2-3 LoRAs before quality degrades
- Trigger words go in the positive prompt (check LoRA page for specific triggers)

### Common Fixes
| Problem | Solution |
|---------|----------|
| Blurry output | Increase steps, lower CFG, try different sampler |
| Over-saturated | Remove "vibrant" from prompt, lower CFG |
| Extra fingers | Add "bad hands" to negative, use hand-focused LoRA |
| Inconsistent style | Lower CFG to 5-6, be more specific in prompt |
| Text/watermarks appearing | Add "text, watermark, signature" to negative |
| Flat lighting | Specify lighting direction in prompt explicitly |
| Wrong aspect ratio feel | Match resolution to content (portrait = tall, landscape = wide) |
