BASE_URL = "https://elcomercio.pe"
NEWS_PAGE = f"{BASE_URL}/ultimas-noticias/"

API_NEWS_URL = "https://elcomercio.pe/pf/api/v3/content/fetch/story-feed-by-section-and-date-v2?query=%7B%22excludedSections%22%3A%22%2Fno-flujo%2C%2Fpublirreportaje%22%2C%22from%22%3A100%2C%22includedFields%22%3A%22%26_sourceInclude%3Dwebsites.elcomercio.website_url%2C_id%2Cheadlines.basic%2Csubheadlines.basic%2Cdisplay_date%2Ccontent_restrictions.content_code%2Ccredits.by._id%2Ccredits.by.name%2Ccredits.by.url%2Ccredits.by.type%2Ccredits.by.image.url%2Cwebsites.elcomercio.website_section.path%2Cwebsites.elcomercio.website_section.name%2Ctaxonomy.sections.path%2Ctaxonomy.sections._id%2Ctaxonomy.sections.name%2Cpromo_items.basic.type%2Cpromo_items.basic.url%2Cpromo_items.basic.width%2Cpromo_items.basic.height%2Cpromo_items.basic.resized_urls%2Cpromo_items.basic_video.promo_items.basic.url%2Cpromo_items.basic_video.promo_items.basic.type%2Cpromo_items.basic_video.promo_items.basic.resized_urls%2Cpromo_items.basic_gallery.promo_items.basic.url%2Cpromo_items.basic_gallery.promo_items.basic.type%2Cpromo_items.basic_gallery.promo_items.basic.resized_urls%2Cpromo_items.youtube_id.content%2Cpromo_items.basic_html%2Cpromo_items.basic_jwplayer.type%2Cpromo_items.basic_jwplayer.subtype%2Cpromo_items.basic_jwplayer.embed%2Cpromo_items.basic_jwplayer.embed.config%2Cpromo_items.basic_jwplayer.embed.config.thumbnail_url%2Cpromo_items.basic_jwplayer.embed.config.resized_urls%2Cpromo_items.basic_jwplayer.embed.config.key%2Cpromo_items.basic_html.content%22%2C%22presets%22%3A%22landscape_s%3A234x161%2Clandscape_xs%3A118x72%22%2C%22size%22%3A%22100%22%7D&filter=%7Bcontent_elements%7B_id%2Ccontent_restrictions%7Bcontent_code%7D%2Ccredits%7Bby%7Bimage%7Burl%7D%2Cname%2Ctype%2Curl%7D%7D%2Cdisplay_date%2Cheadlines%7Bbasic%7D%2Cpromo_items%7Bbasic%7Bresized_urls%7Blandscape_s%2Clandscape_xs%2Clazy_default%7D%2Ctype%2Curl%7D%2Cbasic_gallery%7Bpromo_items%7Bbasic%7Bresized_urls%7Blandscape_s%2Clandscape_xs%2Clazy_default%7D%2Ctype%2Curl%7D%7D%7D%2Cbasic_html%7Bcontent%7D%2Cbasic_jwplayer%7Bembed%7Bconfig%7Bresized_urls%7Blandscape_s%2Clandscape_xs%2Clazy_default%7D%2Cthumbnail_url%7D%7D%2Csubtype%2Ctype%7D%2Cbasic_video%7Bpromo_items%7Bbasic%7Bresized_urls%7Blandscape_s%2Clandscape_xs%2Clazy_default%7D%2Ctype%2Curl%7D%7D%7D%2Cyoutube_id%7Bcontent%7D%7D%2Csubheadlines%7Bbasic%7D%2Ctaxonomy%7Bsections%7Bname%2Cpath%7D%7D%2Cwebsite_url%2Cwebsites%7Belcomercio%7Bwebsite_section%7Bname%2Cpath%7D%2Cwebsite_url%7D%7D%7D%2Cnext%7D&d=2567&_website=elcomercio"
