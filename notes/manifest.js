// Notes manifest: one entry per post, newest first. To publish a new note:
//   1. Add a notes/YYYY-MM-DD-slug.md file (start it with a "# Title" line).
//   2. Add one entry here with the same slug.
//   3. Run `python3 notes/build.py` -- generates notes/<slug>.html with the
//      real title/description baked in statically, so link previews on
//      LinkedIn/Facebook/etc. (which don't run JS) show the actual post
//      instead of a generic placeholder.
//   4. git add (including the generated notes/<slug>.html), commit, push.
window.NOTES = [
  {
    slug: "2026-07-10-hello",
    title: "Why I'm building this",
    date: "2026-07-10",
    summary: "Who this is for, and why a spatial epi tool needed to exist."
  }
];
