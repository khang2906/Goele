# Göle — TODO

## v1 remaining

- [x] Database: SQLAlchemy models + SQLite setup
- [x] Event detail page
- [x] Event creation form
- [ ] Map showing meeting point (Leaflet + OpenStreetMap)
- [x] RSVP form (name only, no account)
- [x] RSVP list on event detail page
- [x] Filter event list by sport (city filter deferred — location will become structured via picker)
- [ ] Set up DB migrations (Alembic) — BLOCKER before deploy: once real
      users exist we can't rebuild the DB to apply schema changes
- [ ] Deploy to Fly.io or Railway

## v1 refinements to consider

- [ ] Pace field: switch from label (relaxed/moderate/fast) to km/h range (e.g. 25–30 km/h)
- [ ] Enforce max_participants on RSVP, plus a waitlist that auto-promotes when someone cancels

## v2 and beyond

- [ ] GPX file upload and display (explicitly out of scope for v1)
- [ ] User accounts and authentication
- [ ] Rebuild frontend in Next.js + React + Tailwind + shadcn/ui
