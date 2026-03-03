# Perú news

Noticias del Perú recolectadas de páginas web:

| Nombre      | Link                           | RSS                         |
| ----------- | ------------------------------ | --------------------------- |
| RPP         | [🔗](https://rpp.pe)           | ✔️                          |
| El Comercio | [🔗](https://elcomercio.pe)    | ✔️                          |
| Canal N     | [🔗](https://canaln.pe)        | ✔️ No tiene `media:content` |
| Peru 21     | [🔗](https://peru21.pe)        | ✔️ ❌No está actualizado    |
| El Peruano  | [🔗](https://www.elperuano.pe) | ❌                          |
| Latina      | [🔗](https://www.latina.pe)    | ✔️ No tiene `media:content` |

> [!NOTE]
> Los datasets actualizan se cada día

## Estructura del proyecto

```bash
peru-news
  datasets/ # Contains the scrapped data
  models/   # Has each dataclass model
  sites/    # Has each scrapper file named <site>.py
  tests/    # Has a test for each scrapper file
  utils/    # Has general utils

```

## Estructura del `<site>.py`

```python
# constants
SITENAME=""
BASE_URL=""
ROBOTS_URL=""
TO_SCRAP_URL="" # Needed to check if the scrap has permission in 'robots.txt' from ROBOTS_URL

# main functions
async def scrap() -> List[New]:
  """ Scrap site and returns a list of News """
  pass
```
