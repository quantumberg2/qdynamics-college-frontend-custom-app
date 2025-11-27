import frappe

@frappe.whitelist(allow_guest=True)
def get_news():
    """
    Fetch all Education-News items
    """
    news_list = frappe.get_all(
        "Education-News",
        fields=[
            "name",
            "header_image",
            "thumbnail_image",
            "description_heading_1",
            "description_1",
            "description_heading_2",
            "description_2",
            "description_heading_3",
            "description_3",
            "description_heading_4",
            "description_4",
            "custom_html"
        ],
        order_by="creation desc"
    )

    # Convert image fields to full URLs
    for news in news_list:
        if news.get("header_image"):
            news["header_image"] = frappe.utils.get_url(news["header_image"])
        if news.get("thumbnail_image"):
            news["thumbnail_image"] = frappe.utils.get_url(news["thumbnail_image"])

    return news_list


@frappe.whitelist(allow_guest=True)
def get_news_item(news_name):
    """
    Fetch a single Education-News item by name
    """
    try:
        news = frappe.get_doc("Education-News", news_name)

        # Convert image fields to full URLs
        if news.header_image:
            news.header_image = frappe.utils.get_url(news.header_image)
        if news.thumbnail_image:
            news.thumbnail_image = frappe.utils.get_url(news.thumbnail_image)

        return {
            "name": news.name,
            "header_image": news.header_image,
            "thumbnail_image": news.thumbnail_image,
            "description_heading_1": news.description_heading_1,
            "description_1": news.description_1,
            "description_heading_2": news.description_heading_2,
            "description_2": news.description_2,
            "description_heading_3": news.description_heading_3,
            "description_3": news.description_3,
            "description_heading_4": news.description_heading_4,
            "description_4": news.description_4,
            "custom_html": news.custom_html
        }
    except frappe.DoesNotExistError:
        return {}