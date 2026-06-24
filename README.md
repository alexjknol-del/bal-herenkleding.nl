# bal-herenkleding.nl

Statische site, deploybaar via GitHub + Cloudflare Pages.

## Structuur
- `site/` bevat de volledige, deploybare website
- `build.py` genereert de site opnieuw vanuit content in het script

## Opnieuw bouwen
    python3 build.py

## Deploy via Cloudflare Pages
1. Push de repository naar GitHub.
2. Maak in Cloudflare een nieuw Pages-project en koppel de repo.
3. Build command: leeg laten (of `python3 build.py`).
4. Build output directory: `site`
5. Koppel het domein bal-herenkleding.nl aan het project.

Een nieuw artikel toevoegen: voeg een blok toe aan de lijst ARTICLES in build.py en draai het script opnieuw.
