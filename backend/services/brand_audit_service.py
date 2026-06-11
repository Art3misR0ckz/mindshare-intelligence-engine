import requests

from bs4 import BeautifulSoup

# ---------------------------------------------------
# BRAND AUDIT SCRAPER
# ---------------------------------------------------

def audit_brand_website(url):

    """
    Scrape website content
    for brand intelligence.
    """

    try:

        # -----------------------------------------
        # REQUEST WEBSITE
        # -----------------------------------------

        response = requests.get(
            url,
            timeout=10
        )

        html = response.text

        # -----------------------------------------
        # PARSE HTML
        # -----------------------------------------

        soup = BeautifulSoup(
            html,
            "lxml"
        )

        # -----------------------------------------
        # TITLE
        # -----------------------------------------

        title = ""

        if soup.title:
            title = soup.title.text.strip()

        # -----------------------------------------
        # META DESCRIPTION
        # -----------------------------------------

        meta_description = ""

        meta = soup.find(
            "meta",
            attrs={"name": "description"}
        )

        if meta:
            meta_description = meta.get(
                "content",
                ""
            )

        # -----------------------------------------
        # HEADINGS
        # -----------------------------------------

        headings = []

        for tag in soup.find_all(
            ["h1", "h2", "h3"]
        ):

            text = tag.get_text().strip()

            if text:

                headings.append(text)

        # -----------------------------------------
        # PARAGRAPHS
        # -----------------------------------------

        paragraphs = []

        for p in soup.find_all("p"):

            text = p.get_text().strip()

            if len(text) > 40:

                paragraphs.append(text)

        # LIMIT SIZE
        paragraphs = paragraphs[:20]

        # -----------------------------------------
        # FINAL STRUCTURED OUTPUT
        # -----------------------------------------

        return {

            "title": title,

            "meta_description":
            meta_description,

            "headings": headings,

            "paragraphs": paragraphs
        }

    except Exception as e:

        print("Brand Audit Error:")
        print(e)

        return {
            "error": str(e)
        }