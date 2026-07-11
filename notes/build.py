#!/usr/bin/env python3
"""Generate a static, crawler-friendly HTML file per note.

Why this exists: note.html (the interactive template) sets the real
<title>/og:title/og:description via JavaScript after the page loads. That's
fine for a human visitor, but link-preview crawlers (LinkedIn, Facebook,
Twitter/X, Slack, iMessage) do not execute JavaScript -- they only read
whatever is in the raw HTML. Without this, every note shares the same
generic "Notes . MESA" preview card.

This script writes one real, static HTML file per post -- notes/<slug>.html
-- with the correct title/description/og/twitter tags baked in directly, so
link previews show the actual post. The page still renders its body with
the same client-side Markdown + KaTeX pipeline as note.html (nothing about
the reading experience changes); only the <head> is pre-filled and the
JS runtime skips the "find this slug from a query string" indirection
since the slug is now baked into the page itself.

Usage, after writing a new notes/YYYY-MM-DD-slug.md and adding its entry
to notes/manifest.js:

    python3 notes/build.py

No dependencies beyond the standard library. Not a build step in the
"compiles the site" sense -- it only touches files under notes/, and the
rest of the site (index.html, methods pages, etc.) is untouched and still
needs no build step at all.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES_DIR = ROOT / "notes"
MANIFEST = NOTES_DIR / "manifest.js"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>if('scrollRestoration' in history)history.scrollRestoration='manual';</script>
<title>__TITLE__ · MESA notes</title>
<meta name="description" content="__SUMMARY__">
<meta property="og:title" content="__TITLE__ · MESA notes">
<meta property="og:description" content="__SUMMARY__">
<meta property="og:type" content="article">
<meta property="og:url" content="https://www.spatialepi.org/notes/__SLUG__.html">
<meta property="og:image" content="https://www.spatialepi.org/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="__TITLE__ · MESA notes">
<meta name="twitter:description" content="__SUMMARY__">
<meta name="twitter:image" content="https://www.spatialepi.org/og-image.png">
<meta name="theme-color" content="#0e141a">
<link rel="icon" href="/favicon-32.png" type="image/png" sizes="32x32">
<link rel="icon" href="/favicon-16.png" type="image/png" sizes="16x16">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/mesa.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/marked@12/marked.min.js"></script>
</head>
<body>

<header class="top">
  <div class="wrap">
    <a class="mark" href="/" aria-label="MESA home">
      <img src="/mesa-icon.png" width="24" height="24" alt="" aria-hidden="true" style="image-rendering:pixelated">
      <b>MESA</b>
    </a>
    <nav class="nav">
      <a class="hideable" href="/#capabilities">capabilities</a>
      <a class="hideable" href="/#workflow">workflow</a>
      <a class="hideable" href="/#offline">offline</a>
      <a class="hideable" href="/#validation">validation</a>
      <a class="hideable" href="/#download">download</a>
      <a href="/methods.html">methods</a>
      <a class="on" href="/notes.html">notes</a>
      <a href="/about.html">about</a>
    </nav>
  </div>
</header>

<main class="wrap doc">
  <div class="crumb"><a href="/">home</a> <span>/</span> <a href="/notes.html">notes</a> <span>/ __TITLE__</span></div>
  <h1>__TITLE__</h1>
  <p class="meta">__DATE__</p>
  <article id="content">
    <p class="sub">Loading…</p>
  </article>
</main>

<footer>
  <div class="wrap">
    <span class="fmark">
      <img src="/mesa-icon.png" width="20" height="20" alt="" aria-hidden="true" style="image-rendering:pixelated">
      <span class="t"><b>MESA</b><em>mapping epidemiology for sparse areas</em></span>
    </span>
    <span><a href="https://rwardrup.com">Ross Wardrup</a>, MPH candidate · Spatial Epi LLC</span>
    <span><a href="/methods.html">methods</a> &nbsp; <a href="mailto:ross@spatialepi.org">contact</a> &nbsp; spatialepi.org</span>
  </div>
</footer>

<script>
  document.addEventListener('DOMContentLoaded', function(){
    var content = document.getElementById('content');

    fetch('__SLUG__.md', {cache:'no-store'})
      .then(function(r){ if(!r.ok) throw new Error('not found'); return r.text(); })
      .then(function(md){
        md = md.replace(/^#\\s+.*\\n+/, '');

        var mathStash = [];
        function stash(match){
          mathStash.push(match);
          return ' MATH' + (mathStash.length - 1) + ' ';
        }
        md = md.replace(/\\$\\$[\\s\\S]+?\\$\\$/g, stash);
        md = md.replace(/\\\\\\[[\\s\\S]+?\\\\\\]/g, stash);
        md = md.replace(/\\$[^\\n$]+?\\$/g, stash);
        md = md.replace(/\\\\\\([\\s\\S]+?\\\\\\)/g, stash);

        var html = marked.parse(md);
        html = html.replace(/ MATH(\\d+) /g, function(_, i){ return mathStash[+i]; });
        content.innerHTML = html;

        if(window.renderMathInElement){
          renderMathInElement(content, {
            delimiters: [
              {left:'$$', right:'$$', display:true},
              {left:'\\\\[', right:'\\\\]', display:true},
              {left:'$', right:'$', display:false},
              {left:'\\\\(', right:'\\\\)', display:false}
            ],
            throwOnError:false
          });
        }
      })
      .catch(function(){
        content.innerHTML = '<p class="sub">Could not load this note.</p>' +
          '<p><a class="x" href="/notes.html">&larr; back to notes</a></p>';
      });
  });
</script>

<script>
  // Tab-away favicon: swap to the sad mesa while you're not looking.
  (function(){
    var icons = document.querySelectorAll('link[rel="icon"]');
    if(!icons.length) return;
    var originals = Array.prototype.map.call(icons, function(l){ return l.getAttribute('href'); });
    document.addEventListener('visibilitychange', function(){
      icons.forEach(function(link, i){
        var sad = link.getAttribute('sizes') === '16x16' ? '/favicon-16-sad.png' : '/favicon-32-sad.png';
        link.setAttribute('href', document.hidden ? sad : originals[i]);
      });
    });
  })();

  console.log('%c\\u25b2 MESA', 'color:#C8402F;font-weight:bold;font-family:monospace;font-size:14px');
  console.log('%cz = \\u221e \\u00b7 p < 2.2e-16 (very significant find)', 'color:#9BA7AD;font-family:monospace');
</script>
</body>
</html>
"""


def parse_manifest(text):
    """Pull {slug, title, date, summary} objects out of manifest.js.

    Deliberately not a JS parser -- manifest.js entries are a fixed, simple
    shape (four double-quoted string fields, no nested objects, no escaped
    quotes inside values), so a per-field regex is enough and keeps this
    script dependency-free.
    """
    entries = []
    for block in re.findall(r"\{[^{}]*\}", text):
        fields = {}
        for key in ("slug", "title", "date", "summary"):
            m = re.search(rf'{key}\s*:\s*"([^"]*)"', block)
            if not m:
                break
            fields[key] = m.group(1)
        if len(fields) == 4:
            entries.append(fields)
    return entries


def html_escape(s):
    return (s.replace("&", "&amp;")
             .replace('"', "&quot;")
             .replace("<", "&lt;")
             .replace(">", "&gt;"))


def main():
    manifest_text = MANIFEST.read_text(encoding="utf-8")
    entries = parse_manifest(manifest_text)
    if not entries:
        print("No entries found in notes/manifest.js -- nothing to build.")
        return

    for e in entries:
        out = (TEMPLATE
               .replace("__TITLE__", html_escape(e["title"]))
               .replace("__SUMMARY__", html_escape(e["summary"]))
               .replace("__DATE__", html_escape(e["date"]))
               .replace("__SLUG__", e["slug"]))
        out_path = NOTES_DIR / f"{e['slug']}.html"
        out_path.write_text(out, encoding="utf-8")
        print(f"wrote {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
