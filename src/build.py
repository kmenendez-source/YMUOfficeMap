import base64, json, sys, pathlib

here = pathlib.Path(__file__).parent
out = pathlib.Path(sys.argv[1])

def seat(id, role, dept, x, y, w, h, chair=None, vertical=False, type="desk", area="", room=None):
    return {"id": id, "role": role, "name": "", "dept": dept, "email": "", "phone": "", "notes": "",
            "type": type, "area": area, "room": room, "x": x, "y": y, "w": w, "h": h, "vertical": vertical,
            "chair": {"x": chair[0], "y": chair[1], "r": chair[2]} if chair else None}

EX, WW, EW, HD = "Executive suite", "West wing", "East wing", "Hot desks"
seats = [
    seat(1, "Available office", "Shared", 307, 60, 128, 52, (372, 40, 180), type="vacant", area=EX, room="r1"),
    seat(2, "CEO", "Leadership", 743, 60, 132, 52, (808, 40, 180), area=EX, room="r2"),
    seat(3, "CPO", "Leadership", 1150, 60, 122, 52, (1210, 40, 180), area=EX, room="r3"),
    seat(4, "COO", "Leadership", 52, 487, 64, 106, (34, 543, 90), vertical=True, area="West offices", room="r5"),
    seat(5, "Grant Writer", "Development", 211, 157, 64, 113, vertical=True, area=WW),
    seat(6, "Finance Associate", "Finance", 276, 157, 148, 74, (350, 240, 0), area=WW),
    seat(7, "EA", "Operations", 458, 157, 138, 74, (522, 240, 0), area=WW),
    seat(8, "Development Manager", "Development", 211, 271, 64, 98, vertical=True, area=WW),
    seat(9, "Development Director", "Development", 276, 318, 320, 50, area=WW),
    seat(10, "Operations Associate", "Operations", 211, 380, 64, 110, vertical=True, area=WW),
    seat(11, "Director of Operations", "Operations", 276, 386, 320, 68, (438, 466, 0), area=WW),
    seat(12, "Open desk", "Shared", 211, 492, 64, 113, vertical=True, type="vacant", area=WW),
    seat(13, "Shows Admin", "Shows", 276, 538, 155, 62, (355, 620, 0), area=WW),
    seat(14, "Shows Manager", "Shows", 460, 538, 152, 62, (530, 620, 0), area=WW),
    seat(15, "Programs Ops", "Programs", 1033, 157, 145, 74, (1107, 240, 0), area=EW),
    seat(16, "Afterschool Manager", "Programs", 1236, 157, 167, 74, (1318, 240, 0), area=EW),
    seat(17, "AAM Programs Manager", "Arts Access", 1404, 157, 70, 114, vertical=True, area=EW),
    seat(18, "AAM Director", "Arts Access", 1033, 318, 370, 52, area=EW),
    seat(19, "AAM Ops", "Arts Access", 1404, 272, 70, 98, vertical=True, area=EW),
    seat(20, "AAM Director of Impact", "Arts Access", 1033, 387, 371, 68, (1200, 466, 0), area=EW),
    seat(21, "AAM Marketing Manager", "Arts Access", 1406, 385, 69, 108, vertical=True, area=EW),
    seat(22, "YMU Marketing", "Marketing", 1406, 494, 69, 112, vertical=True, area=EW),
    seat(23, "CMO", "Marketing", 1007, 538, 138, 62, (1077, 620, 0), area=EW),
    seat(24, "Graphic Designer", "Marketing", 1146, 538, 138, 62, (1213, 620, 0), area=EW),
    seat(25, "Marketing Coordinator", "Marketing", 1285, 538, 120, 62, (1345, 620, 0), area=EW),
    seat(26, "Hot Desk A1", "Shared", 202, 748, 76, 82, (238, 852, 0), type="hot", area=HD),
    seat(27, "Hot Desk A2", "Shared", 202, 665, 76, 82, (238, 742, 0), type="hot", area=HD),
    seat(28, "Hot Desk B1", "Shared", 603, 745, 78, 85, (642, 852, 0), type="hot", area=HD),
    seat(29, "Hot Desk B2", "Shared", 603, 665, 78, 80, (642, 742, 0), type="hot", area=HD),
    seat(30, "Hot Desk B3", "Shared", 525, 665, 78, 80, (564, 742, 0), type="hot", area=HD),
    seat(31, "Hot Desk B4", "Shared", 525, 745, 78, 85, (564, 852, 0), type="hot", area=HD),
    seat(32, "Hot Desk C3", "Shared", 949, 665, 76, 82, (987, 742, 0), type="hot", area=HD),
    seat(33, "Hot Desk C4", "Shared", 949, 748, 76, 82, (987, 852, 0), type="hot", area=HD),
]
rooms = [
    {"id": "r1", "name": "Private Office", "kind": "office", "x": 192, "y": 12, "w": 408, "h": 122, "color": "#d6bf5f", "capacity": 1, "notes": "Currently available"},
    {"id": "r2", "name": "CEO Office", "kind": "office", "x": 606, "y": 12, "w": 404, "h": 122, "color": "#7d9cc4", "capacity": 1, "notes": ""},
    {"id": "r3", "name": "CPO Office", "kind": "office", "x": 1015, "y": 12, "w": 410, "h": 122, "color": "#d29e80", "capacity": 1, "notes": ""},
    {"id": "r4", "name": "Conference Room", "kind": "meeting", "x": 14, "y": 120, "w": 136, "h": 268, "color": "#b9a199", "capacity": 6, "notes": "", "table": {"x": 43, "y": 205, "w": 72, "h": 132}},
    {"id": "r5", "name": "COO Office", "kind": "office", "x": 14, "y": 394, "w": 132, "h": 240, "color": "#cf9f6c", "capacity": 1, "notes": ""},
    {"id": "r6", "name": "Lounge", "kind": "lounge", "x": 1068, "y": 668, "w": 432, "h": 238, "color": "#958aa3", "capacity": 8, "notes": ""},
]
edits_path = here / "user_edits.json"
if edits_path.exists() and "--clean" not in sys.argv:
    edits = json.loads(edits_path.read_text())
    for st in seats:
        st.update(edits["seats"].get(str(st["id"]), {}))
        ch = edits["chairs"].get("c%d" % st["id"])
        if ch and st["chair"]:
            st["chair"].update(x=ch[0], y=ch[1], r=ch[2])
    for r in rooms:
        r.update(edits["rooms"].get(r["id"], {}))
seed = json.dumps({"savedAt": 0, "seats": seats, "rooms": rooms}, separators=(",", ":")).replace("<", "\\u003c")
state_arg = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--state=")), None)
if state_arg:
    import time
    st = json.loads(pathlib.Path(state_arg).read_text())
    st["savedAt"] = int(time.time() * 1000)  # newer than any copy a viewer saved before
    seed = json.dumps(st, separators=(",", ":")).replace("<", "\\u003c")
shared = "--shared" in sys.argv
if shared:
    # The published map keeps its records in the shared store, never in the page source.
    seed = json.dumps({"savedAt": 0, "seats": [], "rooms": [], "chairs": [], "teamColors": {}, "floor": {"x": 0, "y": 0, "w": 2100, "h": 1250}})
html = (here / "template.html").read_text().replace("__SEED__", seed).replace("__SHARED__", "true" if shared else "false")
if shared:
    # The artifact viewer supplies its own doctype/html/head/body skeleton.
    import re
    html = re.sub(r"<!doctype html>\s*<html[^>]*>\s*<head>\s*<meta charset=\"utf-8\">\s*<meta name=\"viewport\"[^>]*>\s*", "", html, count=1)
    html = html.replace("</head>\n<body>\n", "", 1)
    html = re.sub(r"</body>\s*</html>\s*$", "", html)
out.write_text(html)
print(out, len(html))
