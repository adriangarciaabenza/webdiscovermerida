---
name: web-research-images
description: Buscar información actual y localizar imágenes en internet usando fuentes verificables. Usar cuando el usuario pida investigar un tema, consultar datos recientes, encontrar referencias web o buscar imágenes para una página o contenido.
---

# Web Research And Images

Use this skill when the task requires current information or visual assets from
the internet. Prefer primary and authoritative sources, and distinguish facts
verified online from interpretation or inference.

## Research workflow

1. Convert the request into focused search queries. Include the language,
   location, date range, and content type when those details matter.
2. Use `websearch` to discover relevant pages. Use `webfetch` to inspect the
   pages that support the answer rather than relying only on search snippets.
3. Prefer official institutions, original publications, documentation,
   reputable news organizations, and direct creator or organization pages.
4. Cross-check important or surprising claims with at least two independent
   sources. Check the publication date and whether a page is describing a
   current or historical fact.
5. Report the source title and URL next to material claims. Mention the date of
   consultation when the information can change over time.
6. If sources disagree, present the disagreement and explain which source is
   more authoritative or recent. Never invent missing facts.

## Image workflow

1. Search for images using precise subject, location, orientation, dimensions,
   and style terms. Search the subject in its local name as well as in English
   when that can improve results.
2. Prefer images from the rights holder, government or cultural institution,
   Wikimedia Commons, or a clearly identified stock/open-license provider.
3. Inspect the original image or asset page with `webfetch` when possible. Do
   not treat an image-search thumbnail, repost, or hotlinked preview as the
   source.
4. For every recommended image, provide the direct asset URL, the source page,
   creator, license or usage terms, and attribution text when available.
5. Do not claim that an image is free to use without confirming its license.
   If licensing cannot be verified, label the image as reference-only and do
   not add it to the project.
6. For project assets, prefer downloading only when the user has requested it
   and the license permits it. Preserve attribution and license details in the
   project documentation when required.

## Output requirements

- Separate factual findings, recommendations, and unresolved uncertainty.
- Use absolute URLs and avoid URL shorteners.
- Keep the search scope proportional to the request; do not collect unrelated
  links or images.
- Ask for clarification when the intended audience, geography, date range, or
  image usage rights materially changes the result.
- Do not expose private tokens, personal data, or search credentials.
