# GroupRide

A web app for organizing group meetups for cyclists, motorcyclists, and runners.
A user posts an event (sport, date/time, meeting point, route, pace), others
RSVP. That's the whole product right now.

---

## About me

I'm a Wirtschaftsinformatik (Information Systems) graduate based in Munich.
This is my first real full-stack project. I'm building it to learn by doing
and to have something concrete to show employers. Treat me as a beginner who
understands concepts but has not built and shipped a real web app before.

I learn best by understanding *why* something is done, not just copying code.

---

## How I want to work with you

**Plan before coding.** When I ask for a feature, your first response should
be a short plan: what files you'll touch, what approach you'll take, and any
decisions I should weigh in on. Wait for me to confirm before writing code.
For tiny changes (one-line fixes, renaming a variable) you can skip the plan.

**Explain the why.** When you write code, add comments on non-obvious lines
explaining the reasoning, not just restating what the code does. After
writing a file, give me a short plain-English summary of what it does and
how it fits into the rest of the app.

**Push back on me.** If I ask for something that's a bad idea, over-engineered,
out of scope for v1, or premature optimization, say so and explain why. Don't
just build whatever I ask. I'd rather have a short argument than a bad feature.

**Pick the simplest thing that works.** No clever abstractions, no design
patterns "for later," no frameworks we don't need yet. If there's a boring
straightforward solution, pick it. We can refactor when there's a real reason.

**Ask when unsure.** If a requirement is ambiguous or you're guessing, stop
and ask. I'd rather answer a clarifying question than debug your guess.

**Help me type some of it myself.** When I say "I'll type this one," walk me
through it line by line instead of dumping the whole file. Some of this I
need to learn with my hands, not my eyes.

**Don't run destructive commands without asking.** No `rm -rf`, no
`git push --force`, no dropping database tables, no deleting files I haven't
explicitly told you to delete. Ask first, every time.

---

## Tech stack (v1)

The stack is deliberately boring. We'll add complexity only when a real need
forces us to.

- **Language:** Python 3.11+
- **Backend framework:** FastAPI
- **Database:** SQLite (single file, zero setup). Migrate to Postgres later.
- **ORM:** SQLAlchemy 2.x with the modern declarative style
- **Frontend:** Server-rendered HTML using Jinja2 templates, with HTMX for
  interactivity. No React, no build step, no JavaScript framework yet.
- **Styling:** Plain CSS to start. Tailwind only if styling becomes painful.
- **Maps:** Leaflet + OpenStreetMap tiles. Never Google Maps (paid, requires key).
- **Auth:** None in v1. Anyone can create or RSVP to events. We'll add a real
  auth provider (Clerk or Supabase Auth) when v1 is otherwise complete.
- **Testing:** pytest, but only for backend logic. UI tested by clicking.
- **Package manager:** uv (or pip + venv if uv isn't installed yet).
- **Hosting (later):** Fly.io or Railway. Not configured yet.

The plan is to rebuild the frontend in Next.js + React + Tailwind + shadcn/ui
in v2, once v1 is shipped and I understand what the frontend actually needs
to do.

---

## Scope for v1

A user can:

1. Create an event with: sport (bike / motorcycle / run), title, date and
   time, meeting point (a place name + map pin), an optional link to a route
   on Komoot or Strava, a description, a pace/difficulty label, and a maximum
   number of participants.
2. Browse a list of upcoming events, filtered by sport and city.
3. View an event's detail page with a map showing the meeting point.
4. RSVP to an event by entering a name (no account needed in v1).
5. See who else has RSVP'd.

That's it. Anything not on this list is **out of scope for v1.**

### Explicitly out of scope (do not build, even if I ask)

- User accounts, login, passwords, OAuth, email verification
- GPX file upload or parsing
- Drawing routes on the map (just show the meeting point pin)
- Chat, comments, or messaging between users
- Email or push notifications
- Photo uploads
- Native mobile apps
- Distance/elevation calculations
- Leaderboards, achievements, stats
- Payment, premium features

If I ask for any of these, remind me they're v2 and ask if I really want to
expand scope or if there's a smaller version that fits v1.

---

## Project structure

We'll evolve this as needed. Starting layout:

```
groupride/
├── CLAUDE.md          # this file
├── README.md          # project overview, how to run
├── pyproject.toml     # dependencies
├── app/
│   ├── main.py        # FastAPI app entry point
│   ├── models.py      # SQLAlchemy models (Event, RSVP)
│   ├── database.py    # DB setup
│   ├── routes/        # one file per resource (events.py, rsvps.py)
│   └── templates/     # Jinja2 HTML templates
├── static/            # CSS, JS, images
└── tests/
```

---

## Coding conventions

- **Type hints everywhere.** Every function gets argument and return type hints.
- **Docstrings on non-trivial functions.** A short sentence is enough.
- **Names over comments.** A well-named function beats a comment explaining a
  badly-named one.
- **Format with `ruff format`.** Lint with `ruff check`.
- **Keep functions short.** If a function doesn't fit on a screen, split it.
- **No premature abstractions.** Don't extract a helper until it's used twice.

---

## Git workflow

- Commit after every meaningful working change. Small commits, often.
- Commit messages: imperative mood, e.g. `add event creation form`, not
  `added event creation form` or `adds`.
- Before suggesting a commit, run the app and confirm it actually works.
- Never `git push --force` without asking me explicitly.

---

## What "done" looks like for v1

I can give a friend a URL. They open it on their phone. They see a list of
upcoming bike rides in Munich. They tap one, see where to meet on a map, type
their name, hit RSVP. The next person who opens the page sees their name in
the list. That's v1. Once that works end-to-end and is deployed, v1 ships and
we plan v2.

---

## Things to remind me of when relevant

- I tend to want to add features before finishing the current one. Push back.
- I haven't deployed a web app before, so when we get to deployment, slow down
  and explain what's happening at each step.
- I'm in Germany, so any user-facing data is subject to GDPR. We're not
  collecting much in v1 (just names and RSVPs), but flag it if we ever start
  collecting more.
