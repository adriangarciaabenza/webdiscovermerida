---
name: context7
description: Use Context7 to retrieve current, version-specific library documentation before implementing or reviewing code that depends on an external framework, package, API, or tool.
---

# Context7 Documentation

Use this skill when a task depends on external library behavior, configuration,
APIs, or version-specific examples.

## Workflow

1. Identify the library and the version used by the project.
2. Use the Context7 MCP tools to resolve the library identifier.
3. Query only the documentation relevant to the current task.
4. Base implementation decisions on the returned documentation rather than
   memory or generic examples.
5. If Context7 has no matching documentation, state that limitation and use
   the project's pinned dependencies and official documentation as fallback.

## Rules

- Do not invent APIs, options, imports, or commands.
- Prefer the version declared by the project over the latest version.
- Keep documentation lookups focused and avoid querying unrelated libraries.
- Do not put API keys, tokens, or private documentation in source files.
- For this project, respect the documented HTML/CSS-only frontend scope unless
  the user explicitly changes it.
