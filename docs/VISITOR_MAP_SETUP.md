# Setting Up the Visitor Map

The website footer shows a visitor map powered by **MapMyVisitors**
(formerly ClustrMaps — they rebranded, which retired the old
`clustrmaps.com/map_v2.js` endpoint).

## Current Setup

- The map is embedded in the footer of every page via
  [`_layouts/default.html`](_layouts/default.html) (look for the
  `id="mapmyvisitors"` script tag).
- It is registered to the live domain **`hanchendavidwang.com`**.
- It renders a world map with dots showing where visitors are from.

## Updating or Replacing the Map

If the map ever stops rendering (e.g. another rebrand, an expired/reset
free map, or a domain change):

1. Visit [MapMyVisitors.com](https://mapmyvisitors.com/) and sign in.
2. Confirm the map is registered for `https://hanchendavidwang.com`.
3. Copy the new embed snippet (the `<script id="mapmyvisitors" ...>` tag).
4. Open [`_layouts/default.html`](_layouts/default.html) and replace the
   existing `mapmyvisitors` script tag inside the `.visitor-map` block.

> Tip: to check whether a map ID is still valid, request its `map.js` and
> confirm it returns real content (not 0 bytes):
>
> ```bash
> curl -s -o /dev/null -w "bytes: %{size_download}\n" \
>   "https://mapmyvisitors.com/map.js?d=YOUR_MAP_ID&cl=ffffff&w=a"
> ```

## Alternatives

- **Flag Counter** — [flagcounter.com](https://flagcounter.com/): a simple
  per-country visitor counter badge.
- Any privacy-friendly analytics widget that provides an HTML embed can be
  dropped into the same `.visitor-map` block.
