# Tools

External sites and tools relevant to working with this project's
subject matter — blueprint sharing/editing, production calculators.
Not game facts, so not held to `mechanics/`/`relations/`'s
per-`Source:`/`Verified:` rule, but still checked rather than
recalled from memory where a concrete claim is made (site
relationships, open-source status).

## Useful links

- **[factorioprints.com](https://factorioprints.com/)** — blueprint
  sharing site, the older/original brand. Same underlying data as
  factorio.school (see below), but per the project owner's own
  practical use: older-feeling, with expired/broken thumbnail images
  on many posts.
- **[factorio.school](https://www.factorio.school/)** — blueprint
  sharing site; officially the same project as factorioprints.com
  under a new name (see below), not an independent competitor. Per the
  project owner's own practical use: preferred day-to-day over the
  factorioprints.com domain — newer-feeling, including 2.0-era
  content, working thumbnail images, and FBE integration (see
  fbe.teoxoy.com below).
- **[factorioblueprints.tech](https://factorioblueprints.tech/)** —
  blueprint sharing site, open source
  (`github.com/barthuijgen/factorio-sites`), built independently of
  the factorioprints/factorio.school lineage. In-page blueprint
  rendering (view a design without decoding the string yourself),
  advanced search, actively being updated for 2.0/Space Age as of this
  writing.
- **[factoriobin.com](https://factoriobin.com/)** — blueprint sharing
  site oriented around fast link generation rather than browsing/
  discovery — per its own About page, built specifically to sidestep
  pasting 200k+-character blueprint strings around by hand. Unofficial
  fan project, not affiliated with Wube. Source not (yet) public per
  its own About page, unlike the other three sites here.
- **[fbe.teoxoy.com](https://fbe.teoxoy.com/)** — Factorio Blueprint
  Editor by teoxoy, open source
  (`github.com/teoxoy/factorio-blueprint-editor`). In-browser
  rendering/editing of blueprints and books, undo/redo, an oil-outpost
  generator, and direct import from blueprint strings, pastebin/
  hastebin/gist/gitlab, factorioprints, factorio.school, and Google
  Docs.
- **[kirkmcdonald.github.io](https://kirkmcdonald.github.io/)** —
  production-ratio/resource calculator by Kirk McDonald, open source
  (`github.com/KirkMcDonald/kirkmcdonald.github.io`), static
  HTML/JS/CSS (no backend). Supports modules and beacons. Uses bigint
  rational arithmetic rather than floats — the same reason this
  project uses Python's `fractions.Fraction` when verifying derived
  ratios (see `relations/oil_cracking_ratio.md`'s discrepancy-closing
  work) rather than decimals.

## factorioprints.com vs. factorio.school: same project, official rename

**Confirmed by an explicit primary source**, not inference: r/factorio
thread *"PSA: Factorio Prints is now Factorio School"*
(reddit.com/r/factorio/comments/oae7pa/) — a direct community
announcement of the rename, not a guess. (A fan-maintained comparison
site, checked first, only hedges this same question with "no official
statement from the operators confirms it clearly" — that page was not
used as the basis for this entry once the PSA thread surfaced.)

**Corroborated technically, same conclusion from an independent
angle**: `factorio.school`'s own page `<title>` is still literally
*"Factorio Prints"*, and its compiled JS bundle
(`static/js/main.4b96850f.js`) contains the literal string
`facorio-blueprints` — the exact Firebase project ID
`factorioprints.com` uses (`factorioprints.com/__/firebase/init.json`,
Firebase Hosting's standard auto-config endpoint, returns
`"projectId": "facorio-blueprints"`). Same project ID means both
domains read and write the same live database — a blueprint posted on
one appears on the other; they aren't independently-curated mirrors.

**One genuine tension, left unresolved rather than papered over**: the
two domains currently serve *different compiled frontends* —
`factorio.school` ships an older Create-React-App-style build
(`static/js/main.[hash].js`, non-module `<script defer>`), while
`factorioprints.com` currently ships a newer Vite-style build
(`assets/index-[hash].js`, `<script type="module">`). Bundler choice
alone would suggest factorioprints.com's *frontend* is the more
recently rebuilt one — which cuts against the project owner's
practical observation above (factorio.school feeling newer/better
maintained day-to-day: working images, FBE integration, 2.0 content).
Both things can be true at once (e.g. a frontend redesign happening
under one domain without yet fixing content/image issues, or the
domains' relative roles having shifted since the 2021 PSA), but this
project doesn't have a source pinning down *why* — recorded as an open
tension, not resolved by guessing.

- `factorioblueprints.tech`, by contrast, is a genuinely separate
  project — its own GitHub repo
  (`github.com/barthuijgen/factorio-sites`), no shared backend
  reference found. Matches its framing as a newer, independent
  competitor rather than a rebrand.
- `factoriobin.com` is a third, unrelated fan project (per its own
  About page) — narrower in scope (link-generation, not
  browsing/search) rather than a competitor aiming at the same
  discovery use case as the other three.

**Old `/view/<id>` links don't cross-open between the two domains** —
project owner's own tested experience: a blueprint ID that resolves on
factorioprints.com fails to open the same way on factorio.school, even
though both domains query the same underlying `facorio-blueprints`
Firebase database. Attempted to verify this project-side and hit a
real limit: both domains serve a byte-identical generic app shell over
plain HTTP regardless of whether the ID in the URL is valid or garbage
(checked directly — `curl`ing a known-good ID and a made-up one against
each domain returns identical HTML both times, on both domains) — pure
client-side single-page apps, so the actual "does this ID resolve"
question only gets answered after the page's own JS runs and queries
Firebase, which isn't something this project's tooling can execute in
this environment. So: recorded as the project owner's own observed
fact, not independently confirmed or contradicted by this project's
own checks — those checks only prove *why* a simple HTTP request can't
settle the question either way, not what the actual answer is.

**Practical implications**:
- For cross-checking a design against multiple independent sources
  (e.g. the way `layouts/city_block_grid.md`'s rail-spacing research
  cross-checked three published blueprints), treating factorio.school
  and factorioprints.com as two separate sources would already be
  misleading on data-sharing grounds alone (ties back to the same
  underlying post) — and per the ID cross-support issue above, may not
  even be reachable as "the same post, different URL" in practice if
  the specific ID was only ever shared as a factorioprints.com link.
- For day-to-day browsing, the project owner's own tested preference
  is factorio.school over the factorioprints.com domain specifically,
  despite the shared backend — the frontend/image-serving difference
  above is real even though the data isn't. Don't assume an old
  factorioprints.com link handed to you will work if pasted into
  factorio.school's address bar instead — re-search there directly.

Source: https://www.reddit.com/r/factorio/comments/oae7pa/psa_factorio_prints_is_now_factorio_school/
(primary, community PSA); technical checks against both domains' live
responses (this project's own verification, 2026-08-09); project
owner's own practical usage account (2026-08-09).
Verified: 2026-08-09
