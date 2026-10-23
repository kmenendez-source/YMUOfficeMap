# YMU Office Map

An interactive floor plan and seating chart for the YMU office.

**Live site:** https://kmenendez-source.github.io/YMUOfficeMap/

**Open it offline:** download `index.html` and double-click it. It runs in any browser with no install or internet connection needed. (The team version that everyone edits together lives at the shared Claude link.)

## What it does

- Find anyone: search by name, role or team, or press `/`.
- Click a desk to see who sits there, their team, email and phone.
- Filter by team, or show only open seats.
- Colour desks by team, by status (assigned, open, hot desk), or with custom colours.
- **Edit** mode: drag, resize and rotate desks; add chairs, tables and rooms; resize the floor; turn label text.
- **Roster** shows everyone in a table you can type straight into.
- ⋯ menu: import or export the roster as CSV, back up or restore the layout as JSON, print, or download a copy with your changes built in.

Edits made in `index.html` are saved in that browser only.

## Files

| Path | What it is |
| --- | --- |
| `index.html` | The finished map with the current layout built in |
| `data/layout.json` | The current layout: desks, people, rooms, chairs, floor size |
| `src/template.html` | The map's source code |
| `src/build.py` | Builds `index.html` from the template and a layout file |

## Rebuilding after changing the layout data

```bash
cd src
python3 build.py ../index.html --state=../data/layout.json
```

To refresh `data/layout.json` from the map, use **⋯ → Back up layout (JSON)** and replace the file.
