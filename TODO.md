# Göle — TODO

## v1 remaining

- [x] Database: SQLAlchemy models + SQLite setup
- [x] Event detail page
- [ ] Event creation form (in progress)
- [ ] Map showing meeting point (Leaflet + OpenStreetMap)
- [ ] RSVP form (name only, no account)
- [ ] RSVP list on event detail page
- [ ] Filter event list by sport and city
- [ ] Set up DB migrations (Alembic) — BLOCKER before deploy: once real
      users exist we can't rebuild the DB to apply schema changes
- [ ] Deploy to Fly.io or Railway

## v1 refinements to consider

- [ ] Pace field: switch from label (relaxed/moderate/fast) to km/h range (e.g. 25–30 km/h)

## v2 and beyond

- [ ] GPX file upload and display (explicitly out of scope for v1)
- [ ] User accounts and authentication
- [ ] Rebuild frontend in Next.js + React + Tailwind + shadcn/ui
