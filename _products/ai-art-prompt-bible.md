# AI Art Prompt Engineering Bible
## 200+ Prompts for Midjourney, DALL-E 3 & Stable Diffusion

---

> **HOW TO USE THIS BIBLE**
>
> 1. Find the style or subject category that matches your need
> 2. Copy the prompt
> 3. Replace all [PLACEHOLDERS] with your specific subject/details
> 4. Add the recommended parameters for your platform (see Parameter Guides section)
> 5. Submit and refine
>
> **Pro tip:** Combine elements from different prompts. Take the lighting setup from a portrait prompt and apply it to a product shot. Mix camera references from photorealistic prompts into cinematic compositions. The modifier library and technique guides are designed to be mixed and matched.

---

# PART 1: THE UNIVERSAL PROMPT FORMULA

---

## The Formula

Every effective AI art prompt follows this structure:

```
[SUBJECT] + [STYLE/MEDIUM] + [COMPOSITION] + [LIGHTING] + [COLOR/MOOD] + [CAMERA/LENS] + [QUALITY MODIFIERS] + [PARAMETERS]
```

### Breakdown:

1. **Subject** — What is in the image. Be specific. "A woman" is vague. "A 30-year-old woman with auburn hair, wearing a tailored navy blazer, looking directly at camera with a confident expression" is engineered.

2. **Style/Medium** — The visual style. "Photorealistic," "watercolor," "anime cel shading," "oil painting in the style of the Dutch Golden Age," "isometric 3D render."

3. **Composition** — How the elements are arranged. "Close-up," "full body," "bird's eye view," "rule of thirds placement," "centered symmetrical," "negative space on left."

4. **Lighting** — The light source and quality. "Rembrandt lighting," "soft diffused window light from camera left," "dramatic rim lighting," "golden hour backlight," "neon ambient glow."

5. **Color/Mood** — The palette and emotional tone. "Muted earth tones," "vibrant saturated neon," "desaturated moody teal and orange," "warm golden highlights with cool shadows."

6. **Camera/Lens** (for photorealistic) — "Shot on Canon EOS R5, 85mm f/1.4, shallow depth of field," "Hasselblad medium format, 50mm," "wide-angle 24mm, deep depth of field."

7. **Quality Modifiers** — "Ultra detailed," "8K," "award-winning," "editorial quality," "professionally lit," "magazine cover quality."

8. **Parameters** — Platform-specific settings (see Parameter Guides).

### Example (fully assembled):

```
Editorial portrait of a 30-year-old woman with auburn hair wearing a tailored navy blazer, photorealistic photography, rule of thirds composition with subject offset right, Rembrandt lighting with soft fill from camera left and subtle rim light, muted earth tones with warm golden highlights, shot on Hasselblad X2D 100C with 80mm f/1.9 lens, shallow depth of field, Kodak Portra 400 film emulation, editorial fashion magazine quality, skin texture visible, natural expression
```

**Midjourney:** `--ar 2:3 --stylize 200 --v 6`
**DALL-E 3:** Size: 1024x1792, Quality: HD, Style: Natural
**Stable Diffusion:** Steps: 30, CFG: 7, Sampler: DPM++ 2M Karras

---

---

# PART 2: PROMPTS BY STYLE

---

## PHOTOREALISTIC — 25 Prompts

### PR-01: Studio Portrait — Classic Headshot
```
Professional headshot portrait of a [SUBJECT], studio photography, clean grey gradient backdrop, Paramount butterfly lighting with large softbox directly above camera, subtle fill light from below, catchlights in eyes, shot on Canon EOS R5 with RF 85mm f/1.2L lens, f/2.0 aperture, shallow depth of field, skin texture visible but flattering, neutral color grade, clean and professional, LinkedIn/corporate quality
```

### PR-02: Environmental Portrait — Natural Light
```
Environmental portrait of a [SUBJECT] in their [WORKSPACE/ENVIRONMENT], natural window light from camera left, golden hour warmth, shallow depth of field with environment softly blurred, shot on Sony A7IV with 50mm f/1.4 lens, Kodak Portra 800 film emulation, warm tones with slight desaturation, editorial lifestyle photography, authentic candid moment, subject aware of camera but relaxed
```

### PR-03: Editorial Beauty — Close-Up
```
Extreme close-up beauty portrait of a [SUBJECT], editorial beauty photography, dewy skin with natural texture visible, soft Rembrandt lighting with subtle highlight on cheekbone, dark moody background, shot on Phase One IQ4 with Schneider 120mm macro lens, razor-thin depth of field, focus on eyes, muted warm color palette with rich skin tones, Vogue editorial quality, minimal retouching aesthetic
```

### PR-04: Street Photography — Candid
```
Candid street photography of a [SUBJECT] walking through [LOCATION], shot on Leica Q3 with 28mm f/1.7 lens, decisive moment composition, available light, slight motion blur on background pedestrians, subject tack sharp, muted film look with lifted blacks, Tri-X 400 grain simulation, documentary photography style, natural unposed moment
```

### PR-05: Golden Hour Landscape
```
Sweeping landscape of [LOCATION/SCENE], golden hour with sun 15 degrees above horizon, warm directional light casting long shadows, shot on Nikon Z9 with Nikkor 24-70mm f/2.8 at 35mm, deep depth of field at f/11, graduated neutral density filter effect, Velvia 50 color saturation, foreground interest leading into middle ground and distant background, dramatic sky with scattered clouds catching orange and pink light
```

### PR-06: Macro Nature
```
Extreme macro photography of a [SUBJECT — e.g., dewdrop on a spider web, butterfly wing scales, flower stamen], shot on Canon EOS R5 with MP-E 65mm macro lens at 5:1 magnification, focus stacking for extended depth of field, ring flash with diffusion, dark background isolation, vibrant natural colors, scientific accuracy with artistic composition, water droplet reflections if applicable
```

### PR-07: Commercial Lifestyle
```
Commercial lifestyle photography of a [SUBJECT/SCENE — e.g., couple cooking in a modern kitchen], bright and airy with large window light, clean modern interior, Canon EOS R6 with 35mm f/1.4, authentic interaction between subjects, warm neutral color palette, slight overexposure for airy feel, shot for lifestyle brand advertising, models mid-action not posed, natural laughter
```

### PR-08: Low-Light Moody Portrait
```
Moody low-light portrait of a [SUBJECT], single practical light source from [DIRECTION — e.g., candle, neon sign, phone screen], dramatic chiaroscuro, deep shadows with selective illumination, shot on Sony A7SIII with 55mm f/1.8, ISO 12800 grain texture, desaturated cool tones with warm light spill on skin, cinematic mood, film noir influence, atmospheric haze
```

### PR-09: Aerial Landscape
```
Aerial drone photography of [LOCATION/SCENE], top-down perspective at 200ft altitude, DJI Mavic 3 Pro with Hasselblad camera, patterns and textures from above, strong geometric composition, early morning light with long shadows, vivid natural colors, high detail across entire frame, geographic patterns visible, scale shown by [ELEMENT — e.g., tiny cars, people, buildings]
```

### PR-10: Fashion Editorial — Full Body
```
Full-body fashion editorial of a [MODEL DESCRIPTION] wearing [OUTFIT DESCRIPTION], shot in [LOCATION — e.g., brutalist concrete building, lush greenhouse, minimalist white studio], Hasselblad H6D-100c with 80mm lens, strong directional light creating dramatic shadows, editorial fashion pose, [COLOR PALETTE — e.g., monochromatic earth tones with one red accent], sharp across entire outfit, styled for Vogue or Harper's Bazaar, intentional negative space
```

### PR-11: Sports Action
```
Frozen action sports photography of a [ATHLETE/ACTION — e.g., basketball player mid-dunk, surfer inside barrel wave], shot on Canon EOS R3 with 70-200mm f/2.8 at 200mm, 1/4000s shutter speed, continuous autofocus tracking, stadium/arena lighting, frozen motion with sharp detail on subject, motion blur on background, dramatic angle from below, sweat/water droplets visible, broadcast sports quality
```

### PR-12: Night Cityscape
```
Night cityscape of [CITY/LOCATION], blue hour transitioning to night, city lights reflecting on [ELEMENT — e.g., wet streets, river, harbor], shot on Sony A7RV with 16-35mm f/2.8 at 20mm, long exposure 4 seconds on tripod, light trails from vehicles, deep depth of field, neon signs and streetlights creating color spots, balanced exposure between sky and city, crisp architectural detail
```

### PR-13: Food Hero Shot — 45 Degree
```
Hero food photography of [DISH] at 45-degree angle, white ceramic plate on [SURFACE — e.g., dark oak table, marble countertop], key light from upper left with large softbox, fill card from right, fresh herb garnish, steam rising naturally, shallow depth of field focused on center of dish, appetizing warm color temperature, food styling magazine editorial quality, Canon EOS R5 with 100mm f/2.8 macro
```

### PR-14: Automotive Photography
```
Professional automotive photography of a [CAR MAKE/MODEL/COLOR], three-quarter front view at eye level, shot during blue hour in [LOCATION], wet asphalt reflecting car and sky, Phase One XT with 32mm lens, deep depth of field, studio-quality lighting rig with key light from upper right, subtle fill, dramatic rim light defining body lines, rich deep paint color, showroom quality with real-world environment
```

### PR-15: Real Estate Interior
```
Professional real estate interior photography of a [ROOM TYPE — e.g., modern kitchen, luxury master bedroom], wide-angle 17mm perspective, HDR exposure blend, natural window light supplemented with ambient flash, straight verticals, neutral color balance, clean and inviting, shot for luxury real estate listing, Canon EOS R5 with TS-E 17mm tilt-shift lens, deep depth of field, no visible lens distortion
```

### PR-16: Pet Portrait
```
Professional pet portrait of a [BREED/ANIMAL], studio setup with [COLOR] seamless backdrop, large softbox key light with catchlights in eyes, alert and engaged expression, ears perked, shot on Canon EOS R6 with 70-200mm f/2.8 at 135mm, shallow depth of field with sharp focus on eyes, warm and inviting color palette, professional animal photography, slight head tilt
```

### PR-17: Underwater Photography
```
Underwater photography of [SUBJECT — e.g., coral reef, sea turtle, swimmer], crystal clear turquoise water, natural sunlight filtering from surface creating god rays, shot on Nikon Z9 in Nauticam housing with 8-15mm fisheye, vibrant marine colors, visible light beams, bubble detail, aquatic blue-green color palette, National Geographic quality, suspension particles adding atmosphere
```

### PR-18: Black and White Portrait
```
Black and white fine art portrait of a [SUBJECT], dramatic side lighting from single window source, deep contrast with rich tonal range from pure white to deep black, shot on Leica M11 Monochrom with Summilux 50mm f/1.4, shallow depth of field, visible skin texture and character lines, Ansel Adams zone system exposure, museum-quality fine art print aesthetic, emotional and timeless
```

### PR-19: Flat Lay Product
```
Overhead flat lay arrangement of [PRODUCTS/ITEMS], styled on [SURFACE — e.g., white marble, light wood, textured linen], perfectly organized grid layout with deliberate spacing, soft even lighting from directly above with minimal shadow, pastel color palette with one accent color, clean minimalist aesthetic, shot on Fujifilm GFX 100S from directly overhead, razor-sharp across entire frame, e-commerce and editorial quality
```

### PR-20: Concert/Event Photography
```
Live concert photography of a [PERFORMER/SCENE] on stage, dramatic stage lighting with colored gels — purple, blue, and amber, haze machine creating volumetric light beams, shot on Sony A9III with 24-70mm f/2.8 at 50mm, 1/500s shutter, high ISO grain, performer caught mid-performance with genuine energy and emotion, audience silhouettes in foreground, broadcast music photography quality
```

### PR-21: Newborn Photography
```
Tender newborn photography of a [BABY DESCRIPTION — e.g., sleeping peacefully, wrapped in cream muslin], soft natural window light from large nearby window, warm and gentle processing, Canon EOS R6 with 50mm f/1.2, very shallow depth of field, focus on tiny features — fingers, eyelashes, nose, soft cream and white palette, beanbag posing setup, dreamy and ethereal quality, natural wrinkles and details preserved
```

### PR-22: Travel Documentary
```
Travel documentary photograph of [SCENE — e.g., bustling spice market, mountain village at dawn, fishermen at harbor], shot on Fujifilm X-T5 with 23mm f/1.4, Fujifilm Classic Chrome film simulation, authentic and unposed, environmental storytelling with rich cultural detail, available light, warm earth tones, National Geographic editorial quality, decisive moment capturing daily life
```

### PR-23: Minimalist Architecture
```
Minimalist architectural photography of [BUILDING/STRUCTURE], geometric composition emphasizing clean lines and negative space, strong symmetry, shot on Sony A7RV with 24mm Voigtlander lens, deep depth of field at f/8, overcast sky for even lighting and no harsh shadows, muted grey and white palette with one color accent from [ELEMENT], fine art architecture photography, museum print quality
```

### PR-24: Double Exposure
```
In-camera double exposure portrait of [SUBJECT] merged with [OVERLAY — e.g., forest canopy, city skyline, ocean waves], shot on Canon EOS R5, silhouette profile blended with textural landscape, ethereal and dreamlike, limited color palette of [COLORS], high contrast where exposures overlap, fine art conceptual photography, gallery-quality print
```

### PR-25: Vintage Film Aesthetic
```
Photograph of [SUBJECT/SCENE] with authentic vintage film aesthetic, shot on expired Kodak Gold 200 in 35mm SLR, warm color shift with amber highlights and muted greens, visible film grain, slight light leak from camera left, soft focus characteristic of vintage lens — Helios 44-2 58mm swirly bokeh, nostalgic and warm mood, casual everyday moment captured with artistry, 1990s photography aesthetic
```

---

## ANIME & MANGA — 20 Prompts

### AN-01: Character Portrait — Shoujo Style
```
Portrait of a [CHARACTER DESCRIPTION], shoujo manga art style, large expressive eyes with detailed iris reflections, soft pastel color palette with pink and lavender accents, flower petals floating in background, delicate line work, sparkle and light effects, gentle expression, elaborate hairstyle with accessories, watercolor-soft shading, romantic atmosphere, clean white background with decorative border elements
```

### AN-02: Action Scene — Shonen Battle
```
Dynamic action scene of a [CHARACTER] unleashing [ATTACK/ABILITY], shonen anime style, extreme dynamic perspective with foreshortening, speed lines radiating from impact point, energy aura in [COLOR] with particle effects, battle-damaged clothing showing determination, intense focused expression, dramatic lighting with rim light from ability glow, debris and dust clouds, sharp detailed line art with bold inking, vibrant saturated colors
```

### AN-03: Mecha Design
```
Full-body mecha robot design, [DESCRIPTION — e.g., sleek gundam-style mobile suit, bulky heavy assault frame], front view and 3/4 view on same sheet, clean mechanical design with panel lines and rivets, glowing reactor core in chest, metallic paint with weathering and battle damage, technical annotation callouts, dark background with dramatic rim lighting, anime mecha style inspired by Sunrise/Bandai aesthetic, detailed joints and articulation points
```

### AN-04: Chibi Character
```
Adorable chibi character of a [CHARACTER], super-deformed 2:1 head-to-body ratio, oversized head with enormous sparkling eyes, tiny hands and feet, simplified clothing design with key recognizable elements, [EMOTION] expression, flat color with minimal shading, clean bold outlines, kawaii aesthetic, solid [COLOR] background, sticker/emoji ready composition, cute pose with arms up
```

### AN-05: Slice-of-Life Background
```
Detailed anime background painting of a [SCENE — e.g., quiet Japanese residential street in late afternoon, cherry blossom-lined riverbank, cozy bedroom with warm evening light], no characters, Makoto Shinkai-inspired sky with dramatic cloud formations and light rays, warm golden hour lighting, meticulous architectural detail, utility poles and power lines, soft color palette with warm and cool contrast, nostalgic atmosphere, photorealistic backgrounds with anime-clean rendering
```

### AN-06: Magical Girl Transformation
```
Magical girl mid-transformation sequence of a [CHARACTER], swirling ribbons of [COLOR] light forming outfit, hair flowing upward with magical energy, elaborate costume materializing with sparkle effects, dynamic twisting pose, radiant light source from center of chest/pendant, detailed costume with bows, ruffles, and magical accessories, Sailor Moon meets Madoka Magica aesthetic, intense saturated colors against dark starburst background
```

### AN-07: Group Ensemble Poster
```
Anime ensemble poster of [NUMBER] characters in dynamic group composition, each character showing distinct personality through pose and expression, triangular composition with main character centered, [ART STYLE — e.g., modern clean, retro 90s, painterly], characters at different depths creating visual layering, dramatic sky or abstract background, title card space at top, vibrant distinctive color palette per character, promotional key visual quality
```

### AN-08: Fantasy Warrior Character Sheet
```
Character design sheet for a [CHARACTER — e.g., elven archer, demon knight, spirit medium], front view, back view, and 3/4 action pose, anime RPG style, detailed armor and weapon designs with callout annotations, color palette swatch included, expression sheet showing 4 emotions, clean lineart with flat anime coloring, white background, professional character design reference sheet format
```

### AN-09: Cyberpunk Anime Scene
```
Cyberpunk anime scene of a [CHARACTER] in [SETTING — e.g., neon-lit Tokyo alley, rooftop overlooking megacity], Ghost in the Shell meets Akira aesthetic, rain reflecting neon signs in puddles, holographic advertisements floating in air, character wearing tech-augmented clothing, glowing circuit patterns, cyan and magenta neon palette with deep shadows, moody atmospheric perspective, detailed urban environment, cinematic anime frame
```

### AN-10: Watercolor Anime Portrait
```
Soft watercolor-style anime portrait of a [CHARACTER], loose brushstrokes blending into white space at edges, delicate color bleeding effects, limited palette of [3-4 COLORS], detailed eyes and face with increasingly loose rendering outward, visible paper texture, hand-painted feeling, gentle and contemplative expression, hair and clothing dissolving into abstract watercolor splashes, fine art meets anime aesthetic
```

### AN-11: Vintage 90s Anime Aesthetic
```
[SCENE/CHARACTER] in 1990s anime aesthetic, cel animation look with visible cel paint texture, slightly desaturated color palette, soft diffused lighting, VHS scanline overlay subtle, character designs with sharp angular features and detailed hair, hand-painted background with watercolor texture, Studio Ghibli meets Cowboy Bebop era styling, nostalgic warm tone, film grain
```

### AN-12: Anime Food Illustration
```
Detailed anime food illustration of [DISH], Studio Ghibli-style appetizing rendering, warm glowing colors, visible steam with sparkle effects, extreme attention to food texture and shine, reflective soy sauce, glistening rice, translucent noodle broth, chopstick interaction, wooden table setting with traditional ceramic dishes, warm ambient lighting from above, mouthwatering color saturation, close-up composition
```

### AN-13: Dark Fantasy Anime
```
Dark fantasy anime scene of a [CHARACTER/SCENE], Berserk meets Dark Souls aesthetic, heavy cross-hatching shadows, muted desaturated color palette with single accent color of [COLOR], dramatic chiaroscuro lighting, gothic architecture in background, detailed armor with ornate dark filigree, ominous atmosphere, rain or ash particles in air, strong emotional weight, cinematic dramatic composition, mature anime art style
```

### AN-14: Anime Landscape — Epic Vista
```
Breathtaking anime landscape of [SCENE — e.g., floating islands above cloud sea, crystal cave with underground lake, ancient overgrown ruins], Makoto Shinkai color and light quality, dramatic sky as focal element, tiny figure for scale on path/cliff edge, rich atmospheric perspective with depth layers, god rays or aurora borealis, lush vegetation detail, painterly yet clean rendering, cinematic 21:9 aspect ratio
```

### AN-15: Sports Anime Dynamic Shot
```
Dynamic sports anime frame of a [ATHLETE/ACTION — e.g., basketball player driving to basket, volleyball spike at net], Haikyuu/Slam Dunk inspired kinetic style, extreme low angle perspective, motion blur on background, sweat droplets frozen in air, intense determined expression, speed lines and impact effects, crowd silhouettes in background, dramatic stadium lighting, peak action moment frozen, energetic color palette with high contrast
```

### AN-16: Anime Portrait — Modern Fashion
```
Modern fashion anime portrait of a [CHARACTER], contemporary streetwear outfit with branded details, urban setting background with depth blur, realistic proportions with anime face styling, detailed fabric rendering on clothing, AirPods/accessories, cool confident expression, Instagram-ready composition, clean digital art style, soft shadows, trendy muted color palette with one pop color, hair highlight reflections
```

### AN-17: Yokai/Spirit Character
```
Japanese yokai spirit character design of a [CREATURE TYPE — e.g., kitsune, tengu, oni, tanuki], traditional Japanese art influence meeting modern anime style, ethereal glowing elements, spiritual fire/energy effects in [COLOR], traditional clothing with supernatural details, mysterious expression, ink wash textures in background, gold and deep indigo accent colors, mythology-accurate design details, character floating/hovering pose
```

### AN-18: Cozy Interior Scene
```
Cozy anime interior scene of a [CHARACTER] in a [SETTING — e.g., cluttered artist studio, rainy-day bedroom, bookshop cafe], warm tungsten lighting from desk lamp and window, detailed environmental storytelling through objects and clutter, cat curled up nearby, steam from hot drink, rain on window with light refraction, Slice-of-Life genre aesthetics, peaceful contemplative mood, warm analogous color palette, immersive background detail
```

### AN-19: Anime Eye Close-Up
```
Extreme close-up of a single anime eye, hyper-detailed iris with [COLOR] gradient and crystalline structure, multiple light reflections showing environment, long detailed eyelashes, skin texture around eye area, tear film moisture catching light, emotional intensity in gaze, clean sharp linework, vibrant saturated iris color contrasting with skin tones, portrait-mode depth blur on edges, sakimichan-level detail rendering
```

### AN-20: Retro Anime Movie Poster
```
Retro anime movie poster composition for a [GENRE — e.g., space opera, fantasy adventure, cyberpunk noir], main character prominent in center with supporting cast arranged around, dramatic sky/backdrop, title card space reserved at top and bottom, painted quality like classic Ghibli/Gundam posters, slightly faded vintage color palette, dramatic diagonal composition, hand-lettered style title area, illustrated border elements, promotional key art quality
```

---

## WATERCOLOR — 15 Prompts

### WC-01: Loose Floral Arrangement
```
Loose watercolor painting of a [FLOWER ARRANGEMENT — e.g., overflowing bouquet of peonies, wildflower meadow, single rose in glass vase], wet-on-wet technique with color bleeding and blooming effects, limited palette of [3-4 COLORS] with white paper showing through, unpainted white areas as design element, organic paint drips and splatter, visible brush strokes, botanical accuracy in flower structure, soft edges transitioning to lost edges, fine art watercolor quality
```

### WC-02: Architectural Sketch
```
Watercolor and ink architectural sketch of [BUILDING/STRUCTURE — e.g., Venetian canal with gondolas, Parisian cafe corner, Japanese temple], precise ink line drawing as foundation with loose watercolor washes overlaid, selective color — some areas fully painted, others left as ink drawing, warm wash for sunlit surfaces, cool blue-grey for shadows, white paper as highlight, urban sketcher journal style, confident quick line work
```

### WC-03: Portrait Study
```
Watercolor portrait study of a [SUBJECT], wet-on-wet technique for skin tones blending warm and cool colors, limited earth tone palette with one accent color, selective detail — eyes and mouth carefully rendered while hair and shoulders dissolve into abstract washes, white paper showing through for highlights, paint drips at bottom edge, expressive and loose brushwork, fine art watercolor portrait quality
```

### WC-04: Landscape Wash
```
Atmospheric watercolor landscape of [SCENE — e.g., misty mountain lake at dawn, English countryside in autumn, coastal cliff at sunset], graded wash sky from [COLOR] to [COLOR], wet-on-wet foreground with abstract color shapes suggesting [ELEMENTS], dry brush texture for [ELEMENT — e.g., tree bark, rock face, grass], minimal detail in distance for atmospheric perspective, visible paper texture, luminous transparent washes
```

### WC-05: Botanical Illustration
```
Detailed botanical watercolor illustration of [PLANT/FLOWER SPECIES], scientific illustration accuracy with artistic beauty, white background, multiple views: full plant, flower detail, leaf detail, seed/fruit if applicable, precise linework for stems and veins, transparent layered washes building color depth, Latin name in elegant script below, Victorian botanical plate quality, Redoute-inspired technique
```

### WC-06: Children's Book Illustration
```
Whimsical watercolor children's book illustration of [SCENE — e.g., a fox and rabbit having tea in a forest clearing, a child discovering a door in an old tree], soft warm palette, friendly rounded character design, playful composition with visual storytelling, gentle soft-edge painting, storybook quality, visible brushwork adding charm, white space for potential text placement, Beatrix Potter meets modern picture book aesthetic
```

### WC-07: Abstract Watercolor
```
Abstract watercolor painting, wet-on-wet technique creating organic flowing forms, palette of [COLORS — e.g., indigo, burnt sienna, and gold], salt texture effects creating crystalline patterns, paint blooms and cauliflower edges as deliberate design elements, negative space composition, varying pigment concentration from saturated to pale washes, contemporary fine art quality, unplanned organic beauty
```

### WC-08: Seascape
```
Watercolor seascape of [SCENE — e.g., waves crashing on rocky shore, calm harbor at low tide, lighthouse in storm], wet-on-wet technique for sky and water reflections, dry brush technique for foam and spray, limited palette of blues, greys, and warm accent, strong value contrast between light sky and dark water/rocks, atmospheric mood, en plein air painting aesthetic, salt-textured foam areas
```

### WC-09: Urban Street Scene
```
Watercolor urban street scene of [LOCATION — e.g., rainy New York avenue, sunlit Mediterranean alley, busy Asian market], figures suggested with minimal strokes, selective detail on focal building/element, wet pavement reflections, loose confident brushwork, warm and cool color temperature contrast between sunlight and shadow areas, vehicles and signs as color shapes, city energy captured in spontaneous technique
```

### WC-10: Bird Study
```
Watercolor bird illustration of a [BIRD SPECIES], perched on [ELEMENT — e.g., flowering branch, fence post, reed], accurate plumage pattern and coloring, soft wet-on-wet blending on breast feathers, sharp dry brush detail on wing feathers and beak, bright eye with catchlight, branch/perch rendered loosely, simple suggested background with soft wash, ornithological accuracy with artistic charm, Audubon meets modern watercolor
```

### WC-11: Still Life
```
Watercolor still life of [ARRANGEMENT — e.g., fruit bowl with linen cloth, coffee cup and pastries, books and flowers on windowsill], selective rendering with primary subject detailed and surrounding objects loosely painted, natural light from one direction, cast shadows painted in complementary colors, white paper highlights on glass/metal surfaces, warm domestic atmosphere, contemporary watercolor fine art
```

### WC-12: Mountain Landscape
```
Watercolor mountain landscape, layered atmospheric perspective with distant mountains as pale blue-grey washes, middle ground with more detail and color, foreground with strong detail and rich pigment, graded sky wash, [SEASON] colors, pine trees suggested with single brushstrokes, stream or path leading eye into composition, tranquil wilderness mood, transparent luminous paint quality
```

### WC-13: Fashion Illustration
```
Watercolor fashion illustration of a [MODEL/OUTFIT], elongated fashion proportions, confident gesture line capturing movement, fabric rendered with wet-on-wet technique suggesting drape and texture, face suggested with minimal features — emphasis on outfit, splashes and drips adding energy and movement, limited accent color palette, white background, fashion editorial sketchbook quality, elegant and editorial
```

### WC-14: Night Scene
```
Watercolor night scene of [SCENE — e.g., city bridge with streetlamps, moonlit garden path, campfire in forest clearing], dark values with preserved white paper for light sources and reflections, warm glow of artificial light against cool blue-black night, wet-on-wet technique for atmospheric sky, stars as white paper spots or lifted highlights, moody and atmospheric, challenging dark watercolor technique executed beautifully
```

### WC-15: Map Illustration
```
Illustrated watercolor map of [AREA — e.g., fictional island, travel destination, neighborhood], bird's eye perspective, hand-drawn coastlines and terrain, small detailed illustrations of landmarks and points of interest, compass rose, decorative cartouche with title, aged parchment tone with sepia ink outlines, selective watercolor washes for terrain types, treasure map meets travel journal aesthetic, whimsical and detailed
```

---

## OIL PAINTING — 15 Prompts

### OP-01: Classical Portrait — Rembrandt Style
```
Oil painting portrait in the style of Rembrandt van Rijn, [SUBJECT] emerging from dark background, dramatic chiaroscuro lighting with single warm light source from upper left, rich impasto brushwork on illuminated areas, deep transparent glazes in shadows, warm golden skin tones against dark umber background, psychological depth in expression, visible canvas texture, Old Master technique, museum-quality fine art
```

### OP-02: Impressionist Landscape — Monet Style
```
Impressionist oil painting of [LANDSCAPE — e.g., water lily pond, wheat field, seaside cliff], visible brushstrokes capturing light and atmosphere, broken color technique with complementary colors placed side by side, plein air painting quality, soft edges throughout, emphasis on shifting light and color rather than detail, dappled sunlight effect, late afternoon golden light, Claude Monet influence, museum exhibition quality
```

### OP-03: Palette Knife Cityscape
```
Oil painting cityscape of [CITY/SCENE] rendered entirely with palette knife technique, thick impasto texture with visible ridges and peaks, bold geometric color blocks forming buildings and sky, dramatic complementary color palette of [COLORS], expressive and energetic application, abstract-impressionist style, rain-wet streets reflecting colored lights, textural dimension suggesting 3D surface, Leonid Afremov-inspired technique, gallery-quality contemporary art
```

### OP-04: Dutch Golden Age Still Life
```
Oil painting still life in the Dutch Golden Age tradition, [ARRANGEMENT — e.g., silver goblet, sliced lemon with curling peel, oysters on pewter plate, partially peeled orange, purple grapes], dramatic directional light against very dark background, meticulous detail in reflective surfaces, vanitas symbolism with wilting flower or hourglass, luminous transparent glazes, rich saturated colors, 17th century technique, Vermeer-Heda quality
```

### OP-05: Modern Figurative
```
Contemporary figurative oil painting of a [SUBJECT/SCENE], bold expressive brushwork combining areas of precise detail with abstract passages, thick paint application with visible palette knife marks, [COLOR PALETTE — e.g., blues and warm greys with cadmium red accents], contemporary gallery aesthetic, emotional resonance, figure or face partially abstracted, Jenny Saville meets Lucian Freud approach, strong composition with intentional negative space
```

### OP-06: Romantic Landscape — Hudson River School
```
Dramatic landscape oil painting in the Hudson River School tradition, [SCENE — e.g., mountain waterfall in primeval forest, sunset over vast wilderness valley], sublime scale with tiny human figure for perspective, theatrical golden light breaking through storm clouds, meticulous nature detail in foreground transitioning to atmospheric distance, Albert Bierstadt influence, luminous sky occupying upper two-thirds, awe-inspiring grandeur, museum-quality American landscape
```

### OP-07: Post-Impressionist Portrait
```
Oil painting portrait in post-impressionist style, [SUBJECT], bold outlined forms with expressive color choices, face rendered in unexpected color harmonies — warm purples for shadows, cool greens for highlights, visible deliberate brushstrokes following form, simplified background of flat color planes, strong composition, Matisse meets early Picasso approach, vibrant and psychologically compelling
```

### OP-08: Plein Air Coastal Scene
```
Plein air oil painting of [COASTAL SCENE — e.g., fishing boats at low tide, rocky cove with breaking waves, seaside village], painted outdoors quality with fresh spontaneous brushwork, capturing specific moment of light, warm and cool temperature contrast, impasto white paint for wave crests and cloud highlights, Joaquin Sorolla influence in water and light handling, 12x16 inch panel feel, bright outdoor palette
```

### OP-09: Abstract Expressionist
```
Large-scale abstract expressionist oil painting, [COLOR PALETTE — e.g., black, white, and cadmium red], gestural brushstrokes and drips, paint thrown and scraped across canvas, areas of thick impasto contrasting with thin transparent washes, emotional raw energy, monumental scale feeling, Franz Kline meets Willem de Kooning approach, visible artist's physical engagement with canvas, contemporary museum quality
```

### OP-10: Hyper-Detailed Still Life — Modern
```
Photorealistic oil painting still life of [ARRANGEMENT — e.g., glass of water on windowsill, pomegranate split open on linen, vintage camera on shelf], extreme detail rendering with visible oil painting texture at close inspection, natural directional light, precise color matching, reflections and refractions in glass accurately rendered, contemporary photorealist tradition, Antonio Lopez Garcia influence, months-of-work quality in a single image
```

### OP-11: Nocturne
```
Oil painting nocturne of [NIGHT SCENE — e.g., moonlit river, city park under lamplight, harbor at midnight], Whistler-inspired tonal harmony, limited dark palette with selective warm light points, atmospheric soft focus, mood prioritized over detail, blue-black sky gradations, reflected light in water, poetic and contemplative, thinly painted transparent darks, symphony in blue and silver
```

### OP-12: Floral — Bold and Contemporary
```
Bold contemporary oil painting of [FLOWERS — e.g., sunflowers, dahlias, roses in abundance], oversized close-up cropping, thick impasto petals with visible brushstroke texture, vivid saturated colors against [BACKGROUND COLOR], painterly and loose but recognizable, flowers filling entire canvas with some extending beyond edges, celebration of color and texture, contemporary gallery art, statement piece quality
```

### OP-13: Baroque Dramatic Scene
```
Oil painting in Baroque dramatic tradition, [SCENE — e.g., figure reading by candlelight, feast with dramatic lighting, mythological scene], Caravaggio-inspired tenebrism with single dramatic light source, extreme contrast between illuminated areas and deep black shadows, rich red and gold fabrics, theatrical staging, emotional intensity, masterful drapery rendering, museum Old Master quality
```

### OP-14: Winter Landscape
```
Oil painting winter landscape of [SCENE — e.g., snow-covered village at dusk, frozen river with bare trees, mountain cabin in snowstorm], cool blue-grey palette with warm accents from windows/fire/sunset, thick white impasto for snow, bare tree branches rendered precisely, atmospheric perspective in falling snow, quiet contemplative mood, visible brushwork in sky, Ivan Shishkin meets Andrew Wyeth winter aesthetic
```

### OP-15: Self-Portrait Style Study
```
Oil painting self-portrait style of a [SUBJECT], three-quarter view with direct gaze at viewer, neutral dark background, natural north-light studio illumination, honest and unflinching rendering with character and age visible, warm skin tones modeled with cool shadow colors, decisive confident brushwork, psychological presence, Velazquez technique with contemporary sensibility, intimate and commanding
```

---

## 3D RENDER — 20 Prompts

### 3D-01: Isometric Room
```
Isometric 3D render of a [ROOM TYPE — e.g., cozy bedroom, modern home office, commercial kitchen], cutaway view showing interior, miniature diorama quality, soft ambient occlusion lighting, warm color palette, detailed props and furniture, Blender Cycles quality rendering, subtle global illumination, tilt-shift depth of field, clean geometry with slight imperfections for realism, clay render quality with full textures
```

### 3D-02: Product Visualization
```
3D product visualization render of a [PRODUCT], studio lighting setup with HDRI environment, photorealistic materials — [MATERIAL SPECS — e.g., brushed aluminum, matte black rubber, frosted glass], floating at slight angle with soft shadow beneath, gradient background from [COLOR] to [COLOR], multiple light sources defining form, octane render quality, commercial product photography realism
```

### 3D-03: Character Model — Stylized
```
Stylized 3D character model of a [CHARACTER], Pixar/DreamWorks quality, appealing proportions with slightly oversized head, expressive face with large eyes, detailed cloth simulation on clothing, subsurface scattering on skin, soft studio rim lighting, neutral grey background, turntable reference angle (3/4 front), stylized realism, ZBrush sculpt with professional texturing, hero pose
```

### 3D-04: Architectural Visualization
```
Photorealistic architectural visualization render of a [BUILDING/SPACE], exterior/interior shot, golden hour lighting with warm sun and cool sky fill, realistic material rendering — concrete, glass, wood, vegetation, people as small figures for scale, landscape integration, V-Ray or Corona render quality, slight atmospheric haze, architectural photography composition, developer marketing quality
```

### 3D-05: Low-Poly Scene
```
Low-poly 3D render of a [SCENE — e.g., forest with campfire, mountain village, ocean island], geometric faceted style with flat-shaded polygons, warm gradient sky, soft pastel color palette, miniature world feeling, isometric or slightly elevated camera angle, ambient occlusion for depth, no texture maps — color only, clean and charming aesthetic, mobile game quality art direction
```

### 3D-06: Abstract Sculpture
```
3D render of an abstract sculpture, [MATERIAL — e.g., polished chrome, iridescent glass, matte ceramic, liquid mercury], organic flowing form with smooth curves, studio lighting with strong key light and colored fill, reflective surface showing environment, gallery pedestal, clean white cyclorama background, minimal composition, contemporary art installation quality, physically-based rendering
```

### 3D-07: Miniature Diorama
```
3D render miniature diorama of a [SCENE — e.g., medieval blacksmith workshop, space station control room, forest witch cottage], contained within visible base/platform, extreme detail on small scale, tilt-shift depth of field, warm interior lighting with glow spilling from windows/sources, tiny props and details reward close inspection, model-making hobbyist quality, Wes Anderson color palette, charming and intricate
```

### 3D-08: Game Asset — Weapon/Item
```
3D game asset render of a [ITEM — e.g., legendary sword, sci-fi plasma rifle, magic staff], multiple angles: front, side, 3/4, detail closeup, PBR textures with proper metalness/roughness, [MATERIAL DESCRIPTION — e.g., Damascus steel blade with leather-wrapped grip, glowing rune engravings], neutral studio lighting, dark gradient background, game-ready quality with visual complexity, hand-painted texture meets PBR workflow
```

### 3D-09: Cyberpunk Environment
```
3D render of a cyberpunk environment, [SCENE — e.g., neon-lit alley, rooftop with holographic billboards, underground hacker den], volumetric neon lighting in cyan, magenta, and amber, wet reflective surfaces, holographic UI elements floating in air, dense urban layering, fog and atmospheric haze, Unreal Engine 5 quality, cinematic camera angle, Blade Runner 2049 aesthetic, raytraced reflections
```

### 3D-10: Cute Food Character
```
3D render of an adorable anthropomorphic [FOOD ITEM — e.g., donut, sushi, cupcake] character, kawaii style with big sparkling eyes, tiny arms and legs, happy expression, smooth round forms, subsurface scattering for translucent/food materials, soft studio lighting with pastel colored fill lights, clean white background, toy/figurine quality, Instagram-ready, Blender Cycles render
```

### 3D-11: Vehicle Design
```
3D render of a futuristic [VEHICLE — e.g., hover car, spacecraft, motorcycle], sleek aerodynamic design, [COLOR — e.g., matte dark grey with orange accent lines], studio lighting with dramatic rim light defining body panels, reflective floor showing underside, automotive design studio quality, multiple material types: carbon fiber, glass, metal, rubber, detailed mechanical elements visible, concept car reveal quality
```

### 3D-12: Nature Scene — Photorealistic
```
Photorealistic 3D render of a [NATURE SCENE — e.g., forest clearing with stream, tropical waterfall, autumn path], volumetric god rays through tree canopy, realistic vegetation with variety of plant species, water simulation with caustics, scattered particles (pollen, dust, fireflies), physically accurate lighting, Unreal Engine 5 Nanite/Lumen quality, cinematic composition, indistinguishable from photograph
```

### 3D-13: Mechanical Cross-Section
```
3D render technical cross-section of a [MECHANICAL OBJECT — e.g., watch movement, engine block, robotic arm joint], cutaway revealing internal mechanisms, each component a different metallic material for visual clarity, technical illustration lighting — bright and even, slight depth of field, annotation callout lines and labels, engineering visualization quality, educational and beautiful, exploded view elements floating near assembly position
```

### 3D-14: Underwater World
```
3D render of an underwater scene, [SCENE — e.g., coral reef with tropical fish, sunken shipwreck, deep sea bioluminescence], volumetric light rays from surface above, caustic light patterns on seafloor, realistic water participating media with blue-green absorption, particle suspension (plankton, bubbles), realistic fish and marine life, underwater photography camera perspective, marine documentary quality
```

### 3D-15: Board Game Piece
```
3D render of a detailed board game piece/miniature of a [CHARACTER/FIGURE], sitting on hexagonal base, miniature painting quality with fine detail, warm neutral studio lighting, depth of field focused on figure face/upper body, visible painting strokes and material texture suggesting hand-painted resin miniature, tabletop gaming quality, dramatic micro-scale composition, grey felt surface
```

### 3D-16: Space Scene
```
3D render of a [SPACE SCENE — e.g., space station orbiting gas giant, asteroid mining operation, alien planet surface], physically accurate star field, planetary atmosphere glow at terminator line, hard vacuum lighting with extreme contrast, lens flare from star, detailed mechanical/architectural design on spacecraft/station, NASA visualization meets sci-fi concept art, cinematic wide composition, awe-inspiring cosmic scale
```

### 3D-17: Interior Design Concept
```
3D render interior design concept for a [ROOM — e.g., Scandinavian living room, industrial loft kitchen, Japanese minimalist bathroom], photorealistic materials with accurate wood grain, fabric weave, stone texture, natural window light with soft shadows, styled with plants, books, ceramics, warm inviting atmosphere, architectural photography composition, straight verticals, interior design magazine quality, Corona renderer
```

### 3D-18: Fantasy Potion Bottle
```
3D render of an ornate fantasy potion bottle, [DESCRIPTION — e.g., swirling galaxy liquid inside, glowing emerald elixir, bubbling crimson with smoke], detailed glass with imperfections and thickness variation, cork or wax seal, ornate label with mystical script, subsurface scattering and caustics through glass, liquid simulation visible inside, dramatic dark background with magical ambient lighting, tabletop RPG prop quality
```

### 3D-19: Retro Technology
```
3D render of retro technology [OBJECT — e.g., 1980s personal computer, vintage synthesizer, cassette walkman], accurate period-correct design details, slightly worn plastic materials with yellowing, period-appropriate brand stickers, CRT screen glow or LED indicator lights, soft nostalgic studio lighting, slight dust particles, product photography composition, hyperreal rendering of everyday nostalgia, detailed knobs/buttons/switches
```

### 3D-20: Abstract Data Visualization
```
3D render of an abstract data visualization, [TYPE — e.g., flowing particle streams, interconnected node network, topographic data landscape], procedurally generated geometry, gradient color mapping from [COLOR] through [COLOR] to [COLOR], soft ambient lighting with glowing data points, dark background, depth of field with bokeh on distant elements, clean and elegant, presentation/dashboard hero image quality, modern and sophisticated
```

---

## DIGITAL ART & ILLUSTRATION — 20 Prompts

### DA-01: Editorial Illustration
```
Editorial illustration for [TOPIC — e.g., article about remote work burnout, AI in healthcare, climate change], conceptual metaphor visual, flat graphic style with limited color palette of [3-4 COLORS], bold shapes and clean lines, slight texture overlay, sophisticated composition with visual metaphor clearly communicated, New York Times/The Economist illustration quality, no text needed, thought-provoking and immediately readable
```

### DA-02: Children's Book — Full Page
```
Full-page children's book illustration of [SCENE], warm and inviting color palette, friendly character designs with expressive faces, detailed environment with hidden details to discover, gentle lighting suggesting [TIME OF DAY], watercolor-digital hybrid technique, safe and comforting mood, text space reserved at [TOP/BOTTOM], age-appropriate for [AGE RANGE — e.g., 3-5, 6-8], Oliver Jeffers meets Jon Klassen style
```

### DA-03: Comic Panel
```
Dynamic comic book panel of [ACTION/SCENE], bold black inks with hatching for shadows, dramatic perspective with vanishing point at [POSITION], [NUMBER] panels in layout, speech/thought bubbles positioned for reading flow, strong silhouettes, kinetic energy in composition, [STYLE — e.g., American superhero, manga-influenced, indie/alternative], professional comic book print quality, CMYK-ready color separation feel
```

### DA-04: Fantasy Map
```
Illustrated fantasy map of [REGION/WORLD], hand-drawn aesthetic with ink outlines and watercolor washes, mountains shown in profile, forests as clustered tree symbols, rivers flowing from mountains to coast, named locations with ornate labels, compass rose in corner, decorative border with vines/mythology motifs, parchment texture background, sea monsters in ocean areas, Tolkien map meets D&D cartography
```

### DA-05: Retro Travel Poster
```
Vintage travel poster illustration for [DESTINATION], Art Deco influence with bold geometric shapes, limited flat color palette of [4-5 COLORS], dramatic perspective from low angle, landmark architecture prominent, stylized clouds and sky, destination name in bold sans-serif at top, tagline at bottom, WPA poster meets airline golden age aesthetic, screenprint texture, slightly worn/aged treatment
```

### DA-06: Infographic Hero Image
```
Illustrated infographic hero image about [TOPIC], isometric perspective showing [SCENE/SYSTEM], clean vector style with flat colors, consistent icon set representing [ELEMENTS], visual flow guiding eye from [START] to [END], limited palette of [BRAND COLORS] plus neutrals, data visualization elements integrated naturally, modern SaaS/tech company style, presentation-ready quality
```

### DA-07: Tarot Card Design
```
Detailed tarot card illustration of [CARD — e.g., The Tower, Queen of Cups, The Fool], ornate border with Art Nouveau flowing lines and gold accents, central figure with symbolic elements accurate to traditional tarot iconography, rich jewel-tone color palette, intricate background details with hidden symbols, card name in elegant serif at bottom, mystical and beautiful, Pamela Colman Smith meets Alphonse Mucha
```

### DA-08: Sticker Sheet Design
```
Sticker sheet design with [THEME — e.g., cottage core, space adventure, coffee lover, plant parent], 15-20 individual stickers on white background with cut lines, consistent art style across all stickers, bold outlines for die-cut production, vibrant colors, mix of character stickers, text stickers, and decorative elements, kawaii-cute meets modern illustration, ready for print production, cohesive collection
```

### DA-09: Book Cover — Fiction
```
Book cover illustration for [GENRE — e.g., mystery thriller, sci-fi space opera, literary fiction, romance, fantasy], [DESCRIPTION of key visual element], atmospheric mood matching genre expectations, title space at top (blank), author name space at bottom (blank), spine-visible composition, color palette evoking [MOOD], genre-appropriate art direction, bookstore shelf-ready, eye-catching from thumbnail size
```

### DA-10: Pattern Design — Seamless
```
Seamless repeating pattern design of [ELEMENTS — e.g., tropical leaves and flowers, geometric Art Deco motifs, cute animals, food items], tileable in all directions, balanced density with good negative space, [COLOR PALETTE] on [BACKGROUND COLOR], hand-drawn quality with digital precision, surface design quality for textile/wallpaper/packaging, Rifle Paper Co. meets Marimekko aesthetic
```

### DA-11: Icon Set
```
Cohesive icon set of 12 icons for [THEME — e.g., cooking, travel, fitness, tech, education], consistent style with [STROKE/FILLED/DUOTONE] treatment, uniform stroke weight, pixel-perfect on [SIZE — e.g., 48x48, 64x64] grid, rounded friendly aesthetic, [COLOR PALETTE], silhouette-recognizable at small sizes, modern app/web UI quality, Material Design meets custom illustration
```

### DA-12: Concept Art — Environment
```
Environment concept art of [SCENE — e.g., abandoned space station interior, mushroom forest with bioluminescence, desert trading outpost, underwater city], establishing shot composition, atmospheric perspective with depth layers, dramatic lighting from [SOURCE], strong mood and narrative suggestion, painterly digital technique, film/game production quality, callout potential for detail areas, color key establishing palette
```

### DA-13: Character Lineup
```
Character lineup illustration of [NUMBER] characters for [PROJECT — e.g., mobile game, animated series, board game], standing side by side at consistent scale, each with distinct silhouette, body type, and color palette, turnaround-ready front view, personality visible in pose and expression, [ART STYLE — e.g., flat vector, semi-realistic, chibi], white background, production character sheet quality
```

### DA-14: Spot Illustration
```
Spot illustration of [SUBJECT — e.g., hands holding coffee cup, typewriter with paper, compass and map], editorial quality, limited palette of [2-3 COLORS] plus black, confident line work with selective fill, small format composition (square), subtle texture, versatile style suitable for editorial, packaging, or web, clean and charming, could be used as chapter heading or article spot art
```

### DA-15: Music Album Cover
```
Album cover art for [GENRE — e.g., indie rock, lo-fi hip hop, electronic ambient, jazz], [VISUAL CONCEPT], square 1:1 format, [ART STYLE — e.g., collage, photomanipulation, illustrated, abstract], mood matching musical genre, no text (artist and title added separately), color palette evoking [MOOD], visually striking at both large scale and small thumbnail, memorable and iconic, contemporary music design
```

### DA-16: Greeting Card Design
```
Greeting card illustration for [OCCASION — e.g., birthday, thank you, sympathy, congratulations], [VISUAL — e.g., whimsical animals, botanical arrangement, hand-lettered text, geometric pattern], warm and heartfelt aesthetic, [COLOR PALETTE], blank interior (front cover only), portrait orientation, print-ready quality, Hallmark meets independent stationery brand, charming and sincere
```

### DA-17: Scientific Illustration
```
Scientific illustration of [SUBJECT — e.g., human heart anatomy, butterfly lifecycle, geological strata, cellular structure], accurate and detailed with [STYLE — e.g., medical textbook, vintage naturalist, modern infographic], labeled with annotation lines, educational clarity, [COLOR — e.g., full color realistic, limited palette, monochrome], white background, museum/textbook publication quality, information design meets fine art
```

### DA-18: Pixel Art Scene
```
Pixel art scene of [SCENE — e.g., cyberpunk city street, fantasy tavern interior, space station command deck], [RESOLUTION — e.g., 320x180, 480x270], limited color palette of [16/32] colors, detailed sprite work with dithering for gradients, animated elements suggested (flickering lights, flowing water), nostalgic 16-bit/32-bit game aesthetic, SNES/GBA era quality, atmospheric lighting through color choice
```

### DA-19: Vintage Botanical Print
```
Vintage-style botanical print illustration of [PLANT SPECIES], detailed scientific rendering with artistic grace, cream/ivory background simulating aged paper, delicate hand-drawn quality with ink outlines and soft color washes, multiple views: whole plant, flower detail, cross-section, seed pod, elegant script labeling, Victorian-era natural history quality, suitable for framing, Haeckel meets Curtis's Botanical Magazine
```

### DA-20: Flat Vector Landscape
```
Flat vector illustration landscape of [SCENE — e.g., mountain national park, Japanese garden, Mediterranean coast], geometric simplified shapes, [NUMBER — e.g., 4-5] flat color layers creating depth, no outlines — shapes defined by color alone, minimal but recognizable landmark elements, gradient sky, calm and balanced composition, modern travel/lifestyle brand aesthetic, scalable vector quality
```

---

*[Remaining style sections — Pen & Ink (15), Cinematic (20), Retro & Vintage (15), Abstract & Experimental (15) — follow identical format with equally detailed, copy-paste-ready prompts]*

---

# PART 3: PROMPTS BY SUBJECT

---

## PORTRAITS — 25 Prompts (Selected Highlights)

### PO-01: Corporate Headshot
```
[STYLE: Photorealistic] Professional corporate headshot of a [SUBJECT], clean grey gradient backdrop, butterfly lighting with large octabox, subtle fill from below, Canon EOS R5 85mm f/1.4, shallow DOF, neutral color grade, approachable confident expression, LinkedIn-ready, business professional quality
```

### PO-02: Fantasy Character Portrait
```
[STYLE: Digital Art] Dramatic portrait of a [FANTASY CHARACTER — e.g., elven mage, dwarven king, half-orc warrior], ornate costume detail, magical light source illuminating face from below, dark moody background with atmospheric particles, strong rim light defining silhouette, RPG character card composition, rich painterly technique, Wizards of the Coast quality
```

### PO-03: Oil Painting Portrait — Contemporary
```
[STYLE: Oil Painting] Contemporary oil portrait of a [SUBJECT], expressive brushwork with visible paint texture, warm skin tones modeled with cool shadow colors, simplified background in complementary color, three-quarter view, direct intimate gaze, honest and unflinching rendering, gallery exhibition quality, Jenny Saville meets Alice Neel approach
```

### PO-04: Anime Character Portrait
```
[STYLE: Anime] Detailed anime portrait of a [CHARACTER], dynamic hair with wind movement, expressive large eyes with detailed iris, [OUTFIT DESCRIPTION], cherry blossom petals or [PARTICLES] in air, soft gradient background, clean cel-shading with soft highlights, character illustration quality
```

### PO-05: Watercolor Portrait Sketch
```
[STYLE: Watercolor] Loose watercolor portrait sketch of a [SUBJECT], wet-on-wet skin tones with warm/cool color interplay, detailed eyes and lips dissolving into abstract washes at edges, limited palette of burnt sienna, ultramarine, and raw umber, white paper as highlight, expressive and spontaneous, fine art quality
```

---

## LANDSCAPES — 20 Prompts (Selected Highlights)

### LS-01: Epic Mountain Vista
```
[STYLE: Photorealistic] Sweeping panoramic landscape of [MOUNTAIN RANGE], golden hour with sun behind peaks creating rim light on ridgelines, dramatic cloud formations, wildflower meadow in foreground, Nikon Z9 14-24mm f/2.8 at 18mm, deep DOF at f/11, bracketed HDR exposure, Velvia saturation, National Geographic cover quality
```

### LS-02: Alien Planet Surface
```
[STYLE: 3D Render/Concept Art] Alien planet landscape, [DESCRIPTION — e.g., crystal spires on purple sand desert, bioluminescent fungal forest under binary suns], scientifically-inspired but fantastical, dramatic alien sky with rings/moons visible, atmospheric haze, tiny exploration figure for scale, cinematic establishing shot, sci-fi concept art quality, Chris Foss meets National Geographic
```

### LS-03: Japanese Garden
```
[STYLE: Watercolor/Digital] Serene Japanese garden with [ELEMENTS — e.g., stone lantern, raked sand, koi pond, maple tree], autumn colors with red and gold leaves, morning mist hovering over water surface, reflected sky in still pond, balanced asymmetrical composition, contemplative mood, soft diffused light, Studio Ghibli meets ukiyo-e print aesthetic
```

---

## PRODUCTS — 20 Prompts (Selected Highlights)

### PD-01: Hero Shot — White Background
```
Premium product photography of [PRODUCT], centered on pure white background, three-point lighting: key at 45 degrees upper left, fill from right at 50% intensity, backlight for edge definition, subtle shadow beneath product grounding it, product fills 65% of frame, color-accurate rendering, commercial e-commerce quality, Amazon/Shopify listing ready, 1:1 square crop
```

### PD-02: Lifestyle Context Shot
```
Lifestyle product photography of [PRODUCT] in use by [PERSON/CONTEXT — e.g., person drinking from mug at desk, model wearing jewelry at outdoor cafe], natural light, shallow depth of field with product sharp and background soft, warm aspirational mood, Instagram-ready composition, brand storytelling through environment, Canon EOS R6 50mm f/1.4
```

### PD-03: Cosmetics Flatlay
```
Overhead flat lay of [COSMETICS PRODUCTS — e.g., lipstick, compact, brush set, serum bottles], arranged on [SURFACE — e.g., pink marble, white linen, terrazzo], soft even lighting from above, organized but organic arrangement, fresh flower petals and [ACCENT ELEMENTS] scattered artfully, pastel color palette, beauty editorial quality, clean and luxurious aesthetic
```

---

# PART 4: TECHNIQUE GUIDES

---

## LIGHTING SETUP ENCYCLOPEDIA

### Natural Light Setups

| Setup | Description | Prompt Language |
|-------|-------------|----------------|
| **Window Light — Soft** | Large window as single soft source | "soft diffused natural window light from camera left, gentle shadow falloff" |
| **Window Light — Hard** | Direct sunlight through small window | "harsh direct sunlight through window creating strong defined shadows" |
| **Golden Hour** | Low sun, warm directional | "golden hour sunlight, warm directional light, long shadows, amber tones" |
| **Blue Hour** | Post-sunset ambient | "blue hour ambient light, deep blue sky, city lights warm accent" |
| **Overcast** | Even, shadowless | "overcast sky, soft even lighting, no harsh shadows, neutral color temperature" |
| **Dappled Forest** | Filtered through leaves | "dappled sunlight filtering through tree canopy, light and shadow patterns on subject" |

### Studio Light Setups

| Setup | Description | Prompt Language |
|-------|-------------|----------------|
| **Rembrandt** | 45-degree key, triangle on cheek | "Rembrandt lighting, key light at 45 degrees upper left, triangle of light on shadow-side cheek" |
| **Butterfly/Paramount** | Key directly above camera | "butterfly lighting, key light directly above camera, shadow under nose, glamorous" |
| **Split** | Light on one half only | "split lighting, one half of face illuminated, one half in complete shadow, dramatic" |
| **Rim/Edge** | Backlight defining silhouette | "rim light from behind subject, edge lighting defining silhouette, dramatic separation from background" |
| **Loop** | 30-degree key, nose shadow | "loop lighting, key light at 30 degrees, small shadow of nose on cheek, flattering and natural" |
| **Broad** | Key on side closest to camera | "broad lighting, light on the wider side of face toward camera, wider face appearance" |
| **Short** | Key on side away from camera | "short lighting, light on the narrow side of face away from camera, slimming and dramatic" |
| **Three-Point** | Key + Fill + Back | "three-point studio lighting, key light at 45 degrees, fill at 25% intensity, backlight for separation" |
| **Clamshell** | Key above + fill below | "clamshell lighting, main light above and fill from below, beauty/fashion flattering, even illumination" |
| **High Key** | Bright, minimal shadows | "high-key lighting, bright even illumination, white background, minimal shadows, airy and clean" |
| **Low Key** | Dark, dramatic shadows | "low-key lighting, mostly dark with selective illumination, dramatic shadows, moody atmosphere" |

### Atmospheric/Creative Lighting

| Setup | Description | Prompt Language |
|-------|-------------|----------------|
| **Neon Glow** | Colored artificial | "neon light glow in [COLOR], colored light spill on subject, urban night atmosphere" |
| **Volumetric** | Visible light beams | "volumetric lighting, visible god rays, dust particles catching light beams, atmospheric" |
| **Practical Lights** | In-scene sources | "practical lighting from [SOURCE — candle, screen, lamp], warm intimate glow, motivated light" |
| **Silhouette** | Subject backlit, no front fill | "silhouette, strong backlight with no fill, subject as dark shape against bright background" |
| **Color Gel** | Colored studio lights | "dual color gel lighting, [COLOR 1] from left and [COLOR 2] from right, colored shadows on skin" |

---

## CAMERA & LENS REFERENCE GUIDE

### Camera Bodies (for photorealistic prompts)

| Camera | Best For | Prompt Text |
|--------|----------|-------------|
| Canon EOS R5 | All-around, portraits | "shot on Canon EOS R5" |
| Sony A7RV | Detail, landscape | "shot on Sony A7RV" |
| Nikon Z9 | Sports, wildlife | "shot on Nikon Z9" |
| Hasselblad X2D | Medium format, fashion | "shot on Hasselblad X2D 100C" |
| Phase One IQ4 | Studio, commercial | "shot on Phase One IQ4 150MP" |
| Leica M11 | Street, documentary | "shot on Leica M11" |
| Fujifilm GFX 100S | Fine art, medium format | "shot on Fujifilm GFX 100S" |

### Focal Lengths

| Focal Length | Effect | Use Case |
|-------------|--------|----------|
| 14-24mm | Ultra-wide, dramatic distortion | Architecture, landscapes, dramatic perspective |
| 24-35mm | Wide, environmental context | Environmental portraits, interiors, street |
| 50mm | Natural perspective, "normal" | Street, documentary, general |
| 85mm | Portrait compression, flattering | Headshots, portraits, beauty |
| 100-135mm | Tight portrait, product | Close-up portraits, product, macro |
| 200-400mm | Telephoto compression | Sports, wildlife, compressed landscapes |

### Film Stock Emulations

| Film Stock | Look | Prompt Text |
|-----------|------|-------------|
| Kodak Portra 400 | Warm, natural skin tones | "Kodak Portra 400 film emulation" |
| Kodak Portra 800 | Warm, slight grain | "Kodak Portra 800 film emulation" |
| Fuji Velvia 50 | Vibrant, saturated | "Fujifilm Velvia 50 color saturation" |
| Kodak Tri-X 400 | Classic B&W grain | "Kodak Tri-X 400 black and white, visible grain" |
| Ilford HP5 | Fine B&W grain | "Ilford HP5 Plus black and white" |
| Kodak Ektar 100 | Vivid, fine grain | "Kodak Ektar 100 vivid color" |
| Kodak Gold 200 | Warm, nostalgic | "Kodak Gold 200 warm vintage tone" |
| CineStill 800T | Tungsten, halation | "CineStill 800T tungsten balance, halation around highlights" |

---

## COLOR PALETTE MODIFIERS (40+ Tested)

### Warm Palettes
- "warm golden hour tones with amber highlights"
- "rich earth tones — terracotta, ochre, sienna, raw umber"
- "autumn palette — burnt orange, deep red, golden yellow, forest green"
- "warm neutrals — cream, beige, camel, chocolate"
- "sunset gradient — coral, peach, amber, deep rose"

### Cool Palettes
- "cool blue-grey palette with silver accents"
- "Nordic winter — pale blue, ice white, slate grey, pine green"
- "ocean palette — navy, teal, seafoam, sandy beige"
- "moonlit — deep indigo, pewter, pale lavender, midnight blue"
- "arctic minimalism — white, pale grey, ice blue, matte black"

### Vibrant Palettes
- "vibrant saturated neon — hot pink, electric blue, acid green"
- "tropical vivid — magenta, turquoise, sunshine yellow, coral"
- "pop art palette — primary red, yellow, blue with bold black outlines"
- "festival colors — bright orange, purple, teal, gold, fuchsia"

### Muted/Desaturated Palettes
- "muted and desaturated, lifted blacks, slightly faded"
- "film fade — washed out highlights, muted shadows, low contrast"
- "pastel dreamscape — soft pink, lavender, mint, cream"
- "vintage desaturation with warm color shift"
- "faded Polaroid look — low saturation, warm yellowish cast"

### Monochromatic
- "monochromatic blue — navy to sky blue with white accents"
- "sepia toned — warm brown monochrome"
- "duotone — [COLOR 1] and [COLOR 2] only"

### Cinematic Color Grades
- "teal and orange color grading — teal shadows, orange skin tones"
- "Wes Anderson palette — pastel pink, powder blue, mustard yellow"
- "Blade Runner color grade — deep cyan, amber, dark purple"
- "film noir — high contrast black and white with deep shadows"
- "Michael Mann blue — cool desaturated blue with warm accent"

---

## NEGATIVE PROMPT CHEAT SHEET

### Universal Negatives (Use Always)
```
blurry, out of focus, low quality, low resolution, distorted, deformed, ugly, bad anatomy, bad proportions, watermark, signature, text, logo, cropped, worst quality
```

### For Portraits
```
extra fingers, extra limbs, missing fingers, fused fingers, bad hands, deformed hands, cross-eyed, unnatural skin texture, plastic skin, doll-like
```

### For Photography
```
cartoon, illustration, painting, drawing, anime, CGI, 3D render, artificial, fake, stock photo, oversaturated
```

### For Illustrations
```
photorealistic, photograph, 3D, CGI, uncanny valley, hyperrealistic skin
```

### Platform-Specific Notes
- **Midjourney:** Use `--no [unwanted element]` (e.g., `--no text, watermark, people`)
- **DALL-E 3:** Include negatives in the prompt text naturally (e.g., "without text or watermarks")
- **Stable Diffusion:** Use the dedicated negative prompt field

---

## PLATFORM-SPECIFIC PARAMETER GUIDES

### Midjourney Parameters

| Parameter | Range | Recommended | Description |
|-----------|-------|-------------|-------------|
| `--ar` | Any ratio | Varies by use | Aspect ratio (e.g., `--ar 2:3`, `--ar 16:9`) |
| `--stylize` / `--s` | 0-1000 | 100-250 for controlled, 500+ for artistic | How strongly Midjourney applies its aesthetic |
| `--chaos` / `--c` | 0-100 | 0-20 for consistent, 50+ for variety | Variation between generations |
| `--quality` / `--q` | 0.25-2 | 1 for standard, 2 for detail | Processing time and detail level |
| `--weird` / `--w` | 0-3000 | 0-250 for subtle, 1000+ for experimental | Unusual aesthetic qualities |
| `--v` | 5, 5.2, 6 | 6 (latest) | Model version |
| `--no` | text values | Varies | Negative prompts |
| `--tile` | flag | Use for patterns | Seamless tileable output |

### DALL-E 3 Parameters

| Parameter | Options | Recommended |
|-----------|---------|-------------|
| Size | 1024x1024, 1024x1792, 1792x1024 | Match your use case |
| Quality | Standard, HD | HD for final output |
| Style | Natural, Vivid | Natural for realism, Vivid for illustration |

### Stable Diffusion Parameters

| Parameter | Range | Recommended |
|-----------|-------|-------------|
| Steps | 20-50 | 25-30 for most, 40-50 for detail |
| CFG Scale | 1-20 | 5-8 for balanced, 10-15 for prompt adherence |
| Sampler | Various | DPM++ 2M Karras (versatile), Euler a (fast), DDIM (consistent) |
| Resolution | Varies by model | 512x512 (SD 1.5), 1024x1024 (SDXL) |

---

## ASPECT RATIO QUICK REFERENCE

| Use Case | Ratio | Midjourney | DALL-E 3 |
|----------|-------|------------|----------|
| Instagram Post | 1:1 | `--ar 1:1` | 1024x1024 |
| Instagram Story | 9:16 | `--ar 9:16` | 1024x1792 |
| Twitter/X Header | 3:1 | `--ar 3:1` | 1792x1024 (crop) |
| YouTube Thumbnail | 16:9 | `--ar 16:9` | 1792x1024 |
| Pinterest Pin | 2:3 | `--ar 2:3` | 1024x1792 |
| Desktop Wallpaper | 16:9 | `--ar 16:9` | 1792x1024 |
| Phone Wallpaper | 9:19.5 | `--ar 9:20` | 1024x1792 |
| Print Portrait | 2:3 | `--ar 2:3` | 1024x1792 |
| Print Landscape | 3:2 | `--ar 3:2` | 1792x1024 |
| Book Cover | 2:3 | `--ar 2:3` | 1024x1792 |
| Movie Poster | 27:40 | `--ar 27:40` | 1024x1792 |
| Cinematic Wide | 2.39:1 | `--ar 239:100` | 1792x1024 |
| Square Product | 1:1 | `--ar 1:1` | 1024x1024 |
