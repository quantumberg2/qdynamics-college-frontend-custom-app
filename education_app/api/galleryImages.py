import frappe

@frappe.whitelist(allow_guest=True)   # 👈 makes it public
def get_gallery_images():
    """
    Public API to fetch gallery images
    """
    gallery = frappe.get_all(
        "Gallery-Image-Education-App",
        fields=[
            "first_image",
            "second_image",
            "third_image",
            "fourth_image",
            "fifth_image",
            "sixth_image"
        ],
        order_by="creation desc",
        limit_page_length=1
    )

    if gallery:
        return gallery[0]   # returns the latest entry
    return {}
