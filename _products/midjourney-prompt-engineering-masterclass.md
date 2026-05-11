# Midjourney Prompt Engineering Masterclass — 500+ Prompts, Parameters & Style Formulas

---

## How to Use This Masterclass

This masterclass contains 500+ Midjourney-specific prompts organized by visual style, a complete parameter reference, negative prompt guide, and aspect ratio cheat sheet. Every prompt is optimized for Midjourney v5+ and follows the platform's unique syntax.

**Midjourney Prompt Formula:**

```
/imagine [Subject] + [Environment/Setting] + [Style/Medium] + [Lighting] + [Mood] + [Composition] + [Parameters]
```

**Key Principles:**

1. **Be specific, not verbose.** Midjourney responds to clear nouns and adjectives more than long descriptions.
2. **Front-load important elements.** What appears first in the prompt has more weight.
3. **Use artist and style references strategically.** "In the style of..." gives Midjourney strong direction.
4. **Parameters control the output.** Aspect ratio, stylize, chaos, and weird all shape results dramatically.
5. **Iterate relentlessly.** Your first generation is a starting point. Use /vary, upscale, and remix to refine.

---

## Part 1: Complete Parameter Reference

### Core Parameters

| Parameter | Syntax | Range | What It Does |
|-----------|--------|-------|--------------|
| Aspect Ratio | `--ar W:H` | Any ratio | Controls image dimensions |
| Stylize | `--s [value]` | 0-1000 | How artistic vs. literal. Low = literal. High = artistic interpretation |
| Chaos | `--c [value]` | 0-100 | Variety between results. Low = similar. High = wildly different |
| Weird | `--w [value]` | 0-3000 | Unusual/unexpected aesthetic qualities |
| Quality | `--q [value]` | .25, .5, 1 | GPU time. 1 = default, .5 = faster/cheaper |
| Stop | `--stop [value]` | 10-100 | Stop generation partway for looser/abstract results |
| Tile | `--tile` | On/off | Creates seamless repeating patterns |
| No | `--no [item]` | Text | Remove specific elements from generation |
| Seed | `--seed [number]` | 0-4294967295 | Reproduce consistent starting points |
| Style Raw | `--style raw` | On/off | Less Midjourney beautification, more literal |

### Stylize Value Guide

| Value | Effect | Best For |
|-------|--------|----------|
| `--s 0` | Maximum prompt adherence, minimal artistic interpretation | Technical/architectural, exact descriptions |
| `--s 50` | Slight artistic touch, mostly literal | Product shots, realistic photography |
| `--s 100` | Default balance of literal and artistic | General purpose |
| `--s 250` | Noticeably artistic, beautiful compositions | Portraits, landscapes |
| `--s 500` | Highly stylized, dramatic, magazine-worthy | Editorial, fine art |
| `--s 750` | Very artistic, may diverge from prompt | Experimental, mood-driven |
| `--s 1000` | Maximum artistic freedom, loosest interpretation | Abstract, artistic exploration |

### Chaos Value Guide

| Value | Effect | Best For |
|-------|--------|----------|
| `--c 0` | All 4 results very similar | Consistent outputs, product shots |
| `--c 25` | Moderate variety, same theme | Exploring within a concept |
| `--c 50` | Significant variety, different interpretations | Brainstorming |
| `--c 75` | Wildly different results | Creative exploration |
| `--c 100` | Maximum chaos, unexpected combinations | Inspiration, surprise |

### Aspect Ratio Quick Reference

| Ratio | Pixels | Best For |
|-------|--------|----------|
| `--ar 1:1` | Square | Social media, icons, album art |
| `--ar 4:5` | 896x1120 | Instagram portrait |
| `--ar 2:3` | 832x1248 | Pinterest, posters, book covers |
| `--ar 9:16` | 720x1280 | Phone wallpapers, Stories |
| `--ar 3:2` | 1248x832 | Standard landscape photo |
| `--ar 16:9` | 1344x768 | Desktop wallpaper, YouTube, presentations |
| `--ar 21:9` | 1456x624 | Ultra-wide, cinematic, website hero |
| `--ar 3:1` | 1536x512 | Banners, headers |

---

## Part 2: Negative Prompt Guide (--no Parameter)

### How --no Works

The `--no` parameter removes unwanted elements. Use it to clean up common Midjourney defaults.

### Common Negative Prompt Combinations

```
--no text, watermark, signature, logo, writing, letters, words
```
Use when: Any image where you don't want AI-generated text

```
--no people, person, human, figure, crowd
```
Use when: Architecture, landscapes, product shots without models

```
--no blurry, blur, soft focus, out of focus
```
Use when: You want everything tack-sharp

```
--no frame, border, vignette, edges
```
Use when: Clean edge-to-edge images

```
--no cartoon, illustration, anime, drawing, sketch, digital art
```
Use when: You want photorealistic results only

```
--no dark, shadow, moody, dramatic
```
Use when: You want light, airy, bright images

```
--no cluttered, busy, complex, detailed background
```
Use when: You want minimal/clean backgrounds

```
--no symmetry, centered, straight
```
Use when: You want dynamic/asymmetrical compositions

```
--no modern, contemporary, new
```
Use when: Creating vintage/historical imagery

```
--no ugly, deformed, distorted, bad anatomy, extra fingers, extra limbs
```
Use when: Portraits and figure work (reduces deformations)

### Category-Specific Negatives

**For portraits:**
```
--no cropped head, cut off, bad hands, extra fingers, deformed face, cross-eyed, ugly
```

**For products:**
```
--no text, watermark, label, brand name, reflections of photographer, dust, scratches
```

**For landscapes:**
```
--no people, buildings, power lines, cars, trash, modern objects, airplane trails
```

**For food:**
```
--no hands, utensils in mouth, messy table, dirty dishes, unappetizing
```

**For architecture:**
```
--no people, cars, construction, scaffolding, wires, signs
```

---

## Part 3: Style Formulas (100 Proven Combinations)

### Photography Styles (20 Formulas)

```
1. Magazine Editorial:
[subject], editorial photography, shot for Vogue, studio lighting, fashion campaign, high-end retouching --ar 2:3 --s 500

2. National Geographic:
[subject], National Geographic photography, golden hour, dramatic landscape, award-winning nature photography --ar 16:9 --s 250

3. Film Noir:
[subject], film noir photography, black and white, high contrast, dramatic shadows, 1940s detective aesthetic, venetian blind shadows --ar 3:2 --s 350

4. Kodak Portra 400:
[subject], shot on Kodak Portra 400, warm skin tones, soft grain, natural light, analog photography feel --ar 4:5 --s 200

5. Cinematic Still:
[subject], cinematic film still, anamorphic lens flare, color graded, widescreen, movie lighting, 35mm film --ar 21:9 --s 400

6. Street Photography:
[subject], street photography, Henri Cartier-Bresson style, decisive moment, black and white, 35mm focal length --ar 3:2 --s 150 --style raw

7. Sports Illustrated:
[subject], Sports Illustrated cover, peak action frozen, dramatic lighting, sweat visible, powerful composition --ar 3:4 --s 300

8. Annie Leibovitz Portrait:
[subject], Annie Leibovitz style portrait, elaborate set, storytelling, dramatic lighting, celebrity photography --ar 2:3 --s 500

9. Product Commercial:
[subject], commercial product photography, studio lighting, seamless background, sharp focus, advertising quality --ar 4:5 --s 100 --style raw

10. Travel Documentary:
[subject], travel documentary photography, Steve McCurry style, vibrant colors, cultural portrait, meaningful moment --ar 3:2 --s 300

11. Minimalist Photography:
[subject], minimalist photography, negative space, clean composition, single subject, Zen-like simplicity --ar 1:1 --s 250

12. Underwater Photography:
[subject], underwater photography, natural light filtering through surface, blue-green tones, marine biology, crystal clear water --ar 3:2 --s 300

13. Infrared Photography:
[subject], infrared photography, false color, white foliage, dark sky, surreal landscape, dreamlike --ar 16:9 --s 350

14. Drone/Aerial:
[subject], drone photography, top-down view, abstract patterns, geographic, DJI quality --ar 1:1 --s 200

15. Lomography:
[subject], lomography, light leaks, vignette, cross-processed colors, toy camera aesthetic, accidental beauty --ar 1:1 --s 400

16. Polaroid Style:
[subject], instant photograph, Polaroid SX-70, slightly faded, warm cast, white border, nostalgic moment --ar 4:5 --s 350

17. Night Photography:
[subject], night photography, long exposure, available light, neon reflections, urban darkness, moody --ar 16:9 --s 300

18. Macro Photography:
[subject], extreme macro, incredible detail, shallow depth of field, magnified 5x, scientific clarity --ar 1:1 --s 150

19. Black and White Fine Art:
[subject], Ansel Adams style, black and white, full tonal range, zone system, large format camera quality --ar 3:2 --s 400

20. Fashion Lookbook:
[subject], fashion lookbook photography, full body, clean studio, model pose, e-commerce quality, flat lighting --ar 2:3 --s 100
```

### Illustration & Art Styles (20 Formulas)

```
21. Studio Ghibli:
[subject], Studio Ghibli anime style, Hayao Miyazaki, pastoral landscape, soft watercolor, whimsical, hand-drawn animation still --ar 16:9 --s 500

22. Art Nouveau:
[subject], Art Nouveau style, Alphonse Mucha, ornate flowing lines, decorative border, muted jewel tones, poster design --ar 2:3 --s 600

23. Ukiyo-e Woodblock:
[subject], ukiyo-e Japanese woodblock print, Hokusai style, flat color areas, bold outlines, traditional composition --ar 3:2 --s 500

24. Oil Painting — Classical:
[subject], classical oil painting, Caravaggio chiaroscuro, rich colors, canvas texture, dramatic lighting, old master technique --ar 4:5 --s 600

25. Watercolor Botanical:
[subject], watercolor botanical illustration, delicate brushwork, white paper background, scientific accuracy, Elizabeth Blackwell style --ar 3:4 --s 400

26. Cyberpunk Concept Art:
[subject], cyberpunk concept art, Syd Mead style, neon-lit megacity, holographic displays, dystopian future --ar 21:9 --s 500

27. Children's Book Illustration:
[subject], children's book illustration, Oliver Jeffers style, simple shapes, warm watercolor, charming and gentle --ar 3:2 --s 500

28. Pixel Art:
[subject], pixel art, 16-bit style, limited color palette, retro gaming aesthetic, detailed at low resolution --ar 16:9 --s 250

29. Art Deco Poster:
[subject], Art Deco style, geometric patterns, gold and black, 1920s glamour, sharp lines, Tamara de Lempicka influence --ar 2:3 --s 500

30. Impressionist:
[subject], impressionist painting, Claude Monet style, visible brushstrokes, natural light, plein air, soft edges, color over line --ar 3:2 --s 600

31. Comic Book Art:
[subject], comic book art, Jack Kirby dynamic composition, bold inks, halftone dots, superhero aesthetic, action pose --ar 2:3 --s 400

32. Surrealist:
[subject], surrealist painting, Salvador Dali, impossible geometry, dreamscape, melting/distorted reality, subconscious imagery --ar 3:2 --s 700

33. Bauhaus Design:
[subject], Bauhaus style, primary colors, geometric shapes, flat design, modernist aesthetic, Kandinsky meets Mondrian --ar 1:1 --s 500

34. Pencil Sketch:
[subject], detailed pencil sketch, graphite on paper, crosshatching, realistic rendering, artist's sketchbook quality --ar 4:5 --s 200 --style raw

35. Gouache Illustration:
[subject], gouache painting, opaque watercolor, flat areas of vibrant color, mid-century modern illustration style --ar 1:1 --s 400

36. Linocut Print:
[subject], linocut print, bold graphic, limited to 2-3 colors, visible texture of print process, handmade quality --ar 1:1 --s 350

37. Stained Glass:
[subject], stained glass window design, lead came outlines, translucent colored glass, light shining through, cathedral quality --ar 2:3 --s 500

38. Papercut Illustration:
[subject], paper cut art, layered colored paper, visible depth between layers, shadow play, handcrafted precision --ar 1:1 --s 400

39. Risograph Print:
[subject], risograph print style, limited color palette, halftone dots, slight misregistration, CMYK layering, zine aesthetic --ar 2:3 --s 350

40. Isometric Digital:
[subject], isometric illustration, flat shading, clean lines, technical precision, cute and detailed miniature world --ar 1:1 --s 300
```

### 3D & Rendered Styles (20 Formulas)

```
41. Pixar/3D Animation:
[subject], Pixar 3D animation style, subsurface scattering, soft global illumination, appealing character design, theatrical lighting --ar 16:9 --s 400

42. Octane Render:
[subject], octane render, photorealistic 3D, studio lighting, caustics, volumetric atmosphere, 8K resolution --ar 4:5 --s 200

43. Low-Poly 3D:
[subject], low-poly 3D render, geometric facets, flat shading, limited color palette, modern digital art --ar 1:1 --s 300

44. Claymation:
[subject], claymation stop-motion style, clay texture, visible fingerprints, warm studio lighting, Aardman aesthetic --ar 16:9 --s 400

45. Voxel Art:
[subject], voxel art, 3D pixel blocks, isometric view, Minecraft meets fine art, bright colors, playful --ar 1:1 --s 300

46. Glass/Crystal:
[subject], made of clear glass, refracting light, caustics, transparent material, studio lit against dark background --ar 4:5 --s 400

47. Chrome/Metallic:
[subject], made of polished chrome, mirror reflections, studio environment reflected, liquid metal appearance --ar 1:1 --s 350

48. Paper/Origami:
[subject], made of folded paper, origami style, clean precise folds, white paper, soft shadows, paper craft --ar 1:1 --s 400

49. Miniature/Diorama:
[subject], miniature diorama, tilt-shift effect, handmade model, tiny detailed world, macro photography of a model --ar 16:9 --s 400

50. Holographic:
[subject], holographic iridescent material, rainbow reflections, futuristic, light-reactive surface, ethereal and technological --ar 4:5 --s 500

51. Neon Light Sculpture:
[subject], made of neon light tubes, glowing in darkness, bent glass tubes, colorful gas illumination --ar 1:1 --s 400

52. Embroidery/Textile:
[subject], embroidered on fabric, thread texture visible, needlework art, hoop frame, handcrafted textile art --ar 1:1 --s 400

53. Ice Sculpture:
[subject], carved from clear ice, frozen, translucent, cold blue lighting, crystal formations, melting slightly --ar 4:5 --s 350

54. Balloon Art:
[subject], made of twisted balloons, balloon animal artist quality, shiny latex material, colorful and playful --ar 1:1 --s 400

55. LEGO Build:
[subject], built from LEGO bricks, studs visible, accurate brick construction, toy photography, detailed build --ar 1:1 --s 300

56. Inflatable:
[subject], inflatable bouncy castle material, air-filled shiny vinyl, puffy and rounded, playful, oversized --ar 1:1 --s 400

57. Wireframe:
[subject], 3D wireframe render, visible mesh topology, blue on black, CAD aesthetic, architectural/technical --ar 16:9 --s 200

58. Candlelit Scene:
[subject], lit only by candlelight, warm orange glow, flickering shadows, intimate and atmospheric, renaissance painting lighting --ar 3:4 --s 500

59. Underwater 3D:
[subject], submerged underwater, caustic light patterns, floating and weightless, blue-green environment, bubbles --ar 3:2 --s 400

60. Tilt-Shift 3D:
[subject], tilt-shift 3D render, miniature effect, shallow depth of field, toy-like appearance, isometric --ar 16:9 --s 350
```

### Mood & Atmosphere Formulas (20 Formulas)

```
61. Dark Academia:
[subject], dark academia aesthetic, mahogany and leather, old books, candlelit, Oxford/Cambridge atmosphere, scholarly and mysterious --ar 3:2 --s 500

62. Cottagecore:
[subject], cottagecore aesthetic, wildflower garden, linen and wicker, soft natural light, rural English countryside, gentle and idyllic --ar 4:5 --s 500

63. Vaporwave:
[subject], vaporwave aesthetic, pink and purple gradients, Greek statues, palm trees, retro technology, nostalgia glitch --ar 1:1 --s 500

64. Solarpunk:
[subject], solarpunk aesthetic, green technology, optimistic future, plants and solar panels, Art Nouveau architecture meets sustainable design --ar 16:9 --s 500

65. Gothic:
[subject], gothic aesthetic, dark and ornate, cathedral architecture, ravens, fog, moonlight, romantic darkness --ar 2:3 --s 500

66. Tropical Paradise:
[subject], tropical paradise aesthetic, turquoise water, lush vegetation, golden sunlight, island life, saturated natural colors --ar 16:9 --s 400

67. Scandinavian Minimal:
[subject], Scandinavian minimalism, white and light wood, clean lines, hygge warmth, natural materials, understated elegance --ar 3:2 --s 250

68. Cyberpunk Noir:
[subject], cyberpunk noir, neon rain, dystopian megacity, purple and cyan, blade runner atmosphere, technological decay --ar 21:9 --s 500

69. Desert Southwest:
[subject], American Southwest aesthetic, warm terracotta, turquoise accents, desert plants, adobe architecture, golden hour warmth --ar 16:9 --s 400

70. Maritime/Coastal:
[subject], coastal maritime aesthetic, navy and white, weathered wood, lighthouse, sailing, New England charm --ar 3:2 --s 350

71. Ethereal/Dreamy:
[subject], ethereal dreamy atmosphere, soft focus, pastel palette, floating/weightless feeling, otherworldly, gentle light --ar 2:3 --s 600

72. Industrial Raw:
[subject], industrial aesthetic, raw concrete, exposed steel, Edison bulbs, warehouse conversion, honest materials --ar 3:2 --s 250

73. Maximalist:
[subject], maximalist interior, bold patterns, rich colors, collected objects, eclectic layering, more is more philosophy --ar 3:2 --s 600

74. Wabi-Sabi:
[subject], wabi-sabi aesthetic, imperfection as beauty, aged materials, organic shapes, quiet and contemplative, Japanese simplicity --ar 1:1 --s 350

75. 80s Retro:
[subject], 1980s aesthetic, neon colors, geometric patterns, Memphis design, synthwave, bold and playful, nostalgic excess --ar 16:9 --s 500

76. Moody/Dark:
[subject], dark moody atmosphere, deep shadows, muted colors, dramatic, introspective, cinematic noir influence --ar 3:2 --s 400

77. Light and Airy:
[subject], light and airy, bright whites, soft pastels, overexposed slightly, editorial lifestyle, clean and fresh --ar 4:5 --s 300

78. Autumn/Fall Warmth:
[subject], autumn aesthetic, warm oranges and reds, golden light, cozy layers, falling leaves, nostalgic warmth --ar 3:2 --s 400

79. Psychedelic:
[subject], psychedelic art, kaleidoscopic colors, flowing organic forms, 1960s counter-culture, trippy and mind-expanding --ar 1:1 --s 750

80. Zen/Meditative:
[subject], zen aesthetic, extreme simplicity, empty space, single element, calm water, balanced stones, peaceful emptiness --ar 16:9 --s 250
```

### Composition & Technique Formulas (20 Formulas)

```
81. Rule of Thirds:
[subject], positioned off-center using rule of thirds, dynamic composition, intentional negative space, professional framing --s 200

82. Centered Symmetry:
[subject], perfectly centered symmetrical composition, Wes Anderson style, formal and satisfying, architectural precision --s 300

83. Leading Lines:
[subject], strong leading lines drawing eye to focal point, roads/rails/fences/rivers creating depth, vanishing point --s 250

84. Frame Within Frame:
[subject], framed by natural element in foreground (doorway/window/arch/branches), creating depth and context --s 300

85. Bird's Eye View:
[subject], directly overhead perspective, top-down flat lay, pattern and arrangement visible from above --s 200

86. Worm's Eye View:
[subject], extreme low angle looking up, dramatic perspective, subject appears powerful and monumental --s 350

87. Negative Space:
[subject], minimalist with 70% negative space, subject small in frame, breathing room, editorial simplicity --s 200

88. Golden Spiral:
[subject], composed along golden spiral/Fibonacci curve, natural and pleasing eye flow, classical composition --s 400

89. Dutch Angle:
[subject], Dutch angle/tilted horizon, dynamic tension, unsettling or energetic feeling, cinematic technique --s 300

90. Panoramic Sweep:
[subject], ultra-wide panoramic composition, sweeping vista, epic scale, multiple focal points across width --ar 3:1 --s 300

91. Close-Up Detail:
[subject], extreme close-up filling frame, intimate detail, shallow depth of field, abstracting through proximity --s 200

92. Layered Depth:
[subject], multiple distinct layers creating depth (foreground/middle/background), atmospheric perspective, painterly depth --s 400

93. Split Composition:
[subject], frame divided into contrasting halves (light/dark, warm/cool, natural/man-made), visual tension --s 350

94. Radial Composition:
[subject], elements radiating from center point, circular energy, spiraling inward or outward, dynamic movement --s 400

95. Diagonal Dominance:
[subject], strong diagonal lines dominating composition, dynamic and energetic, action and movement implied --s 300

96. Pattern/Repetition:
[subject], repeating pattern filling frame, rhythm and texture, single break in pattern creating focal point --s 250

97. Silhouette:
[subject], pure silhouette against bright/colorful background, shape is everything, dramatic contrast, graphic impact --s 300

98. Reflection:
[subject], perfect mirror reflection in water/glass/chrome, symmetry between real and reflected, doubled world --s 350

99. Motion Blur:
[subject], intentional motion blur showing movement, panned background or moving subject, energy and speed --s 300

100. Bokeh Isolation:
[subject], extreme shallow depth of field, creamy bokeh background, subject isolated in focus, dreamy separation --s 350
```

---

## Part 4: 400 Subject-Specific Prompts

### Portraits (50 Prompts)

```
101. Elderly wisdom portrait, deep wrinkles telling life stories, warm directional light, dark background, Steve McCurry inspired --ar 4:5 --s 400

102. Ballet dancer in mid-leap, studio, frozen grace, dramatic side light, athletic power meets elegance --ar 2:3 --s 350

103. Musician with their instrument, environmental portrait, rehearsal space, natural light, authentic candid moment --ar 3:2 --s 250

104. Child laughing genuinely, outdoor natural light, bokeh background, pure joy captured, lifestyle photography --ar 4:5 --s 300

105. Double exposure portrait, human face merged with forest landscape, ethereal, surreal fine art --ar 2:3 --s 500

106. Warrior queen portrait, elaborate armor and crown, fierce expression, dramatic cinematic lighting, fantasy epic --ar 2:3 --s 600

107. Scientist in laboratory, surrounded by equipment, blue ambient glow, discovery moment, editorial portrait --ar 3:2 --s 300

108. Underwater portrait, flowing hair and fabric, sunlight through surface, ethereal and weightless, fine art --ar 2:3 --s 500

109. Street vendor portrait, surrounded by their goods, environmental context, warm evening light, documentary --ar 3:2 --s 300

110. Twins portrait, identical features different expressions, studio, centered symmetrical composition, conceptual --ar 1:1 --s 350

111-150. [Additional portrait subjects: astronaut, chef, artist painting, grandmother cooking, newborn, couple dancing, swimmer emerging from water, person in rain, meditating yogi, tattooed artist, flower crown portrait, vintage glamour, androgynous model, elderly couple holding hands, rock climber, reader in library, backlit dancer, profile silhouette, laughing friends, person in doorway, artist with paint-stained hands, window-lit contemplation, festival dancer, ice cream shop worker, jazz musician performing, grandmother's hands, skateboarder mid-trick, bride preparation, farmer in field, artist studio self-portrait, contemplative by ocean, neon-lit portrait, morning coffee ritual, gardener among flowers, student studying late, marketplace vendor, sunset silhouette figure, rain-soaked street portrait, autumn leaves falling around face]
```

### Landscapes & Nature (50 Prompts)

```
151. Ancient forest with sunbeams filtering through canopy, mossy ground, morning mist, Pacific Northwest, ethereal --ar 16:9 --s 400

152. Lavender fields in Provence at golden hour, rows extending to horizon, purple sea of flowers, warm and fragrant --ar 16:9 --s 400

153. Volcanic eruption at night, lava flowing, red-orange glow against dark sky, raw power of nature, dramatic --ar 16:9 --s 500

154. Bioluminescent bay at night, glowing blue water with paddler's silhouette, stars above, magical and otherworldly --ar 16:9 --s 500

155. Cherry blossom tunnel, peak bloom, petals falling like snow, soft pink light, Japanese spring perfection --ar 3:2 --s 500

156. Dramatic thunderstorm over wheat field, lightning bolt, dark threatening clouds, golden field below, contrast --ar 16:9 --s 400

157. Arctic iceberg with underwater portion visible, split-level view, turquoise water, massive scale, climate documentary --ar 3:2 --s 350

158. Ancient sequoia forest, massive trees dwarfing tiny hiker, scale and awe, green cathedral, misty --ar 2:3 --s 400

159. Desert oasis from above, patch of green in endless sand, drone perspective, abstract pattern, contrast --ar 1:1 --s 300

160. Fjord at dawn, mirror-still water, dramatic cliffs rising from mist, Nordic landscape perfection, serene and epic --ar 16:9 --s 400

161-200. [Additional landscapes: rice terraces green and flooded, frozen waterfall ice formations, autumn road lined with golden trees, coral reef teeming with life, rolling hills Tuscany, slot canyon light beam, wildflower meadow mountain backdrop, aurora over frozen lake, tropical rainforest waterfall, tide pools close-up, storm waves lighthouse, bamboo forest path, sand dunes at sunrise with long shadows, mangrove roots underwater, English countryside morning fog, canyon river aerial view, winter birch forest, Mediterranean cliffside village, moss-covered temple ruins, moonlit beach with bioluminescence, prairie thunderstorm, ancient olive grove, salt flats mirror reflection, glacier cave blue ice, meadow with single oak tree, Joshua Tree sunset, emerald mine interior, Scottish highlands, Japanese garden autumn, deep ocean abyss bioluminescent creatures, cloud inversion valley, tulip field aerial, rainforest canopy bridge, crystal cave formations, African savanna sunset with acacia tree, alpine wildflower meadow, coastal erosion dramatic cliffs, morning dew macro on spider web, waterlily pond Monet-like]
```

### Architecture & Interiors (50 Prompts)

```
201. Abandoned Art Deco theater, decaying grandeur, ornate ceiling crumbling, light streaming through broken roof --ar 3:2 --s 400

202. Modern minimalist house cantilevered over cliff, glass walls, ocean view, architectural masterpiece, clear sky --ar 16:9 --s 300

203. Ancient Roman ruins at golden hour, columns and arches, warm stone, historical grandeur meets nature reclaiming --ar 16:9 --s 400

204. Spiral staircase from above, geometric perfection, Fibonacci spiral, architectural photography, pattern and rhythm --ar 1:1 --s 300

205. Futuristic space station interior, clean white, large windows showing Earth, sci-fi living space, hopeful future --ar 16:9 --s 400

206. Gothic cathedral interior, light streaming through stained glass, colored light on stone floor, sacred geometry --ar 2:3 --s 500

207. Traditional Japanese ryokan room, tatami, sliding screens, garden view, minimal and peaceful, natural materials --ar 3:2 --s 350

208. Brutalist concrete building against dramatic sky, imposing geometry, raw material beauty, architectural photography --ar 3:4 --s 300

209. Cozy bookshop interior, floor-to-ceiling shelves, reading nook, warm lamp light, books everywhere, inviting --ar 3:2 --s 400

210. Parametric architecture, flowing organic forms, Zaha Hadid inspired, future building, impossible curves made real --ar 16:9 --s 400

211-250. [Additional architecture: Victorian greenhouse, underground subway station retro tile, treehouse complex, floating market, library with ladder, mid-century modern house, Moroccan riad courtyard, ice hotel room, underground bunker converted to home, lighthouse interior spiral stairs, abandoned factory nature reclaiming, modern church with light installation, Venetian palazzo canal view, subway station cathedral-like, rooftop garden urban, shipping container house, ancient Egyptian temple interior, coffee shop industrial chic, museum white cube gallery, castle great hall with fireplace, glass bridge between buildings, underground cavern restaurant, Art Deco elevator lobby, windmill interior traditional, observatory dome interior, traditional English pub, modernist swimming pool, underground wine cellar, monastery library, space habitat garden module, train station grand hall, Georgian townhouse interior, bamboo architecture, underwater research station, converted church loft, Japanese onsen bath, skyscraper lobby, Hobbit-style earth house, airport terminal modernist, floating house on water]
```

### Food & Beverage (50 Prompts)

```
251. Ramen bowl overhead, steam rising, perfect soft egg, nori, chopsticks resting, dark wood surface, food magazine --ar 1:1 --s 300

252. Artisan sourdough bread, just sliced, crispy crust detail, steam escaping, flour-dusted surface, bakery morning --ar 4:5 --s 300

253. Cocktail with smoke bubble about to burst, dramatic bar lighting, amber liquid, ice sphere, mixology art --ar 4:5 --s 400

254. Chocolate cake mid-slice, ganache dripping, layered interior visible, decadent, dark background, indulgent --ar 4:5 --s 350

255. Fresh sushi platter, jewel-like fish, precise cuts, wasabi and ginger, black slate, Japanese precision --ar 3:2 --s 300

256-300. [Additional food: espresso extraction close-up, farmers market produce rainbow, pizza fresh from wood-fired oven, morning pancake stack with syrup pour, fresh pasta making hands working dough, tropical fruit flat lay, wine glass with vineyard background, ice cream melting in summer heat, charcuterie board styled, street food vendor wok flames, thanksgiving table overhead, fresh berries with morning dew, French pastries display case, burger with dripping cheese, matcha latte art, honeycomb with golden honey drip, outdoor summer barbecue scene, artisan cheese selection, smoothie bowl with toppings arranged, breakfast spread European hotel, dim sum bamboo steamers, birthday cake sparklers lit, olive oil pouring onto bread, fresh juice bottles rainbow colors, spice market overhead, fish market fresh catch, hot chocolate with marshmallows, poke bowl colorful arrangement, Indian thali plate, Greek spread outdoor table, morning toast with avocado, wine cellar tasting, gelato display vibrant colors, farm-to-table plated dish, midnight snack kitchen scene, baking in progress messy counter, food truck exterior colorful, afternoon tea spread, camping coffee by fire, molecular gastronomy dish, vintage diner milkshake, market spices overhead bags open, fresh baked cookies cooling rack, cheese wheel being cut]
```

### Fantasy & Sci-Fi (50 Prompts)

```
301. Dragon perched on mountain peak, vast landscape below, scales catching sunrise, epic fantasy, concept art --ar 16:9 --s 600

302. Underwater alien city, bioluminescent architecture, organic-technological hybrid, deep sea civilization, sci-fi --ar 16:9 --s 600

303. Enchanted forest with sentient trees, glowing runes, fairy lights, magical atmosphere, fantasy illustration --ar 16:9 --s 600

304. Space battle fleet engagement, massive capital ships, energy weapons, debris field, sci-fi epic, cinematic --ar 21:9 --s 500

305. Wizard's tower library, impossible architecture, floating books, magical light sources, fantasy detail --ar 2:3 --s 600

306-350. [Additional fantasy/sci-fi: fairy market underground, steampunk airship docking tower, alien jungle planet exploration, medieval tavern with diverse fantasy races, portal opening between worlds, cyberpunk street vendor AI customer, post-apocalyptic nature reclaiming city, mermaid city coral architecture, time traveler Victorian London, robot gardener tending flowers, crystal dragon egg hatching, space station hydroponics bay, witch's cottage exterior autumn, mech warrior standing in field at sunset, phoenix rising from ashes, ghost ship in fog, alien marketplace bazaar, forest spirit deer with galaxy antlers, floating islands connected by bridges, undersea steampunk submarine, ancient golem awakening, fairy ring mushroom circle moonlight, colonizing Mars first settlement, necromancer's laboratory, living ship biological spacefaring vessel, dwarf forge underground, magical academy classroom, AI consciousness visualized, elven city in ancient trees, cosmic horror Lovecraftian entity, post-human evolution, pirate ship vs kraken, enchanted mirror showing other world, space elevator ground view looking up, mushroom kingdom tiny civilization, celestial being cosmic scale, crashed spaceship overgrown, wizard duel energy clashing, generation ship interior city, fairy tale castle sunrise, dark forest spirit wolves, magic shop interior curiosities, terraforming new world time-lapse, underwater treasure shipwreck, phoenix feather close-up magical]
```

### Products & Commercial (50 Prompts)

```
351. Luxury perfume bottle, crystal facets catching light, dark gradient background, floating golden particles, premium --ar 4:5 --s 400

352. Running shoe mid-stride, dynamic splash of color/energy, dark background, athletic power, Nike campaign style --ar 16:9 --s 400

353. Watch on dark surface, dramatic side lighting, reflections in crystal, mechanical detail visible, Swiss craftsmanship --ar 1:1 --s 300

354. Skincare bottles with cream texture swirl, botanical ingredients around, clean white surface, luxury beauty --ar 4:5 --s 300

355. Coffee beans and cup, steam rising, warm tones, rustic wooden surface, morning ritual, artisan quality --ar 1:1 --s 300

356-400. [Additional products: sunglasses reflecting beach scene, candle with melted wax detail, leather bag craftsmanship detail, headphones floating dramatic light, smartphone with screen content glowing, lipstick with color smear, ceramic mug handmade glaze detail, sneaker collection display, wine bottle with vineyard label, moisturizer jar with dewy texture, keyboard mechanical detail shot, camera lens with reflections, ring jewelry box proposal setup, nail polish with drip art, backpack adventure outdoor setting, speaker with visible sound waves, pen on leather journal, essential oils with botanicals, sunscreen beach lifestyle, book stack with reading glasses, bicycle detail gear mechanism, tea ceremony accessories, guitar strings macro, artisan soap handmade texture, chair design iconic piece, plant in designer pot minimalist, beard oil grooming setup, stationery flatlay organized, vintage camera collection, art supplies organized, cooking knife chef's tools, record player vinyl detail, gaming setup RGB lighting, water bottle outdoor adventure, hat collection styled, desk lamp industrial design, fitness equipment gym lifestyle, puzzle box wooden craftsmanship, kitchen appliance modern design, luggage travel lifestyle, pottery wheel creation process, phone case artistic design, glasses frame detail, tool collection workshop, brush set art supplies]
```

### Abstract & Conceptual (50 Prompts)

```
401. Time concept visualization, melting clocks in infinite space, surreal, Dali meets modern digital art --ar 1:1 --s 750

402. Sound made visible, colorful geometric shapes emanating from point source, synaesthesia art, vibrant --ar 16:9 --s 600

403. Emotion: loneliness, single figure in vast empty space, muted palette, tiny and isolated, contemplative --ar 16:9 --s 500

404. Data visualization as organic living form, information flowing like blood vessels, bioluminescent, sci-art --ar 1:1 --s 600

405. Impossible architecture, Escher-like staircases, gravity-defying geometry, black and white, mind-bending --ar 1:1 --s 600

406-450. [Additional abstract/conceptual: growth concept seed to tree transformation, music genre as landscape, anxiety visualized as weather, memory fading like dissolving photograph, connection between two minds, creativity as explosion of color from mind, seasons changing in single frame, language as flowing river of light, gravity inverting objects floating, entropy and order meeting point, consciousness expanding beyond body, fear manifested as shadow creature, hope as light breaking through storm, technology and nature merging, infinity visualization, dreams becoming physical, patience as slowly growing crystal, anger as volcanic eruption contained, peace as still water vast expanse, knowledge as expanding universe, identity fragmented prismatic, belonging as puzzle pieces connecting, freedom as bird becoming wind, nostalgia as faded polaroid ghost, potential energy before release, balance between opposing forces, metamorphosis mid-transformation, silence having a physical presence, courage as stepping into light from darkness, wisdom as ancient tree rings, love as intertwining light streams, loss as missing piece in landscape, joy as bursting particles, curiosity as doors infinite hallway, resilience as bent not broken tree, empathy as color bleeding between figures, solitude as lighthouse in fog, harmony as overlapping circles, chaos controlled into beauty, vulnerability as glass heart, renewal as spring through concrete]
```

### Animals & Nature (50 Prompts)

```
451. Hummingbird frozen mid-flight, iridescent feathers catching rainbow light, fast shutter speed, nature miracle --ar 4:5 --s 350

452. Snow leopard in mountain habitat, camouflage barely visible, intense eyes, endangered beauty, wildlife photography --ar 3:2 --s 350

453. Underwater jellyfish cluster, bioluminescent, flowing tentacles, dark deep ocean, alien beauty on Earth --ar 2:3 --s 400

454. Eagle diving for fish, talons extended, water spray, peak action, wings spread, raw power --ar 3:2 --s 350

455. Chameleon on branch, skin changing color, detailed scales, Madagascar, macro photography, color spectrum --ar 3:2 --s 300

456-500. [Additional animals: fox in autumn leaves, blue whale underwater scale, monarch butterfly migration thousands, wolf pack in snow, coral reef macro cleaner shrimp, owl in flight silent wings spread, polar bear mother with cubs, seahorse among seagrass, octopus camouflage changing, pangolin curled defensive, wild horse running beach, tree frog on red-eyed leaf, manta ray flying underwater, tiger drinking at water reflection, peacock full display, giraffe pattern close-up abstract, emperor penguin colony, bees on honeycomb macro, wild mushrooms fairy ring, spider web morning dew droplets, flamingo flock from above pink, koi fish in clear pond, dragonfly wings macro iridescent, elephant herd crossing river, arctic fox in winter white, clownfish in anemone, moss and lichen micro landscape, whale shark mouth open feeding, bird of paradise dance display, panda in bamboo forest, sea turtle ancient swimming, wild cat hunting stance, bonsai tree ancient detail, barnacles and tide pool macro, lion mane portrait intense, deep sea anglerfish dark depth, caterpillar to butterfly chrysalis, coral spawning event, wolf spider eyes macro, baby animals collection various species, fireflies summer night forest, starfish arm regenerating, bird nest eggs springtime, mantis shrimp colorful close-up, underwater cave diving light beam]
```

---

## Part 5: Workflow Templates

### Brand Consistency Workflow

```
Step 1: Create a base image you love
Step 2: Note the seed (--seed XXXX) from /info or /show
Step 3: Use same seed + same style parameters for consistency
Step 4: Only change the subject while keeping environment/lighting/style

Formula: [new subject], [keep all other descriptors identical] --seed [your seed] --s [same value] --ar [same ratio]
```

### Iteration Workflow

```
Round 1: Generate 4 options with your prompt + --c 50 (variety)
Round 2: Pick best, use /vary (strong) for meaningful variations
Round 3: Pick best, use /vary (subtle) for fine-tuning
Round 4: Upscale final selection
Round 5: If needed, use inpainting/outpainting for fixes
```

### Multi-Image Series Workflow

```
Keep consistent across a series:
- Same --seed (or similar prompt structure)
- Same --s value
- Same --ar ratio
- Same style/lighting descriptors
- Only change the subject

Example series prompt base:
"[SUBJECT], minimalist studio portrait, white background, soft diffused lighting, clean and modern, editorial quality --ar 4:5 --s 250 --seed 12345"

Then swap [SUBJECT] for each image in the series.
```

---

*Thank you for purchasing the Midjourney Prompt Engineering Masterclass. You now have 500+ prompts, a complete parameter reference, negative prompt strategies, and proven style formulas. Start with the style formulas most relevant to your work, iterate using the workflow templates, and build your personal prompt library over time. The more you use these as starting points and refine them, the faster you'll develop your own visual language.*
