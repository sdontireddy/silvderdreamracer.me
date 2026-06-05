# Repository Instructions for AI Coding Agents

## Theme Safety Rule

- Do not modify, patch, reformat, or overwrite anything under `Flex/`.
- Treat `Flex/` as an external upstream theme dependency.
- Implement site changes through Pelican configuration (`pelicanconf.py`), content files under `content/`, or project-owned files outside `Flex/`.
- If a requested change appears to require editing `Flex/`, stop and propose a config/content-based alternative first.

## Preferred Implementation Paths

- Use `pelicanconf.py` for navigation, metadata, links, feeds, and feature toggles.
- Use `content/` for pages, posts, images, and static assets.
- Keep generated artifacts in `output/` out of source edits unless explicitly requested.
