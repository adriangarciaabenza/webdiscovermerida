---
name: frontend-design
description: Apply accessible, responsive, and intentional frontend design practices when creating or changing HTML, CSS, templates, components, or user interfaces.
---

# Frontend Design Practices

Use this skill for any user-interface work. Make the smallest design system that
fits the product instead of assembling generic components or decorative effects.

## Before coding

- Inspect the existing visual language, content, and technical constraints.
- Define the page's primary action and information hierarchy.
- Choose a deliberate type scale, spacing rhythm, color palette, and visual
  direction that support the product rather than defaulting to framework styles.

## Implementation

- Use semantic HTML and a logical heading hierarchy.
- Declare the document language and provide useful page titles.
- Ensure keyboard access, visible focus states, sufficient color contrast, and
  labels or accessible names for controls.
- Design mobile-first and verify narrow, medium, and wide layouts.
- Prefer fluid sizing, readable line lengths, and spacing that adapts without
  horizontal scrolling.
- Keep content and controls clear; do not use animation, gradients, glassmorphism,
  or decorative elements unless they serve a clear purpose.
- Respect reduced-motion preferences when motion is present.
- Reuse a small set of CSS custom properties for colors, spacing, typography,
  and radii.
- Avoid unnecessary JavaScript, dependencies, and abstractions.

## Verification

- Test the page at mobile and desktop widths.
- Check focus order and the interface using keyboard-only navigation.
- Confirm text remains legible and actions remain obvious without relying on
  color alone.
- Check that the design remains consistent with the project's existing scope
  and README instructions.
