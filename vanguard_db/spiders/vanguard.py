import scrapy
from vanguard_db.items import VanguardCardItem


class VanguardSpider(scrapy.Spider):
    name = "vanguard"
    start_url = "https://en.cf-vanguard.com/cardlist/"
    base_url = "https://en.cf-vanguard.com"

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse)

    def parse(self, response, **kwargs):
        product_item_links = response.css(
            ".product-item > a::attr(href)").extract()

        for product_item_link in product_item_links:
            yield scrapy.Request(url=F"{self.base_url}{product_item_link}", callback=self.parse_boosters)

    def parse_boosters(self, response):
        card_links = response.css(
            "#cardlist-container > ul > li > a::attr(href)").extract()
        for card_link in card_links:
            yield scrapy.Request(url=F"{self.base_url}{card_link}", callback=self.parse_card)

    def parse_card(self, response):
        card_type = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div:nth-child(3) > div.type::text").get()
        name = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div.name > span.face::text").get()
        group = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div:nth-child(3) > div.group::text").get()
        race = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div:nth-child(3) > div.race::text").get()
        nation = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div:nth-child(3) > div.nation::text").get()
        grade = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div:nth-child(3) > div.grade::text").get()
        power = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div:nth-child(3) > div.power::text").get()
        critical = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div:nth-child(3) > div.critical::text").get()
        shield = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div:nth-child(3) > div.shield::text").get()
        skill = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div:nth-child(3) > div.skill::text").get()
        gift = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div:nth-child(3) > div.gift::text").get()
        effect = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div.effect::text").get()
        flavor = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div.flavor::text").get()
        regulation = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div:nth-child(6) > div.regulation::text").get()
        number = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div:nth-child(6) > div.number::text").get()
        rarity = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div:nth-child(6) > div.rarity::text").get()
        illustrator = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.data > div:nth-child(6) > div.illstrator::text").get()
        image = response.css(
            "#site > div.site-main > div > div > div._entry-content > div > div > div.cardlist_detail > div.image > div > img::attr(src)").get()
        yield VanguardCardItem(
            card_type=card_type,
            name=name,
            group=group,
            race=race,
            nation=nation,
            grade=grade,
            power=power,
            critical=critical,
            shield=shield,
            skill=skill,
            gift=gift,
            effect=effect,
            regulation=regulation,
            number=number,
            rarity=rarity,
            illustrator=illustrator,
            image=image,
        )
