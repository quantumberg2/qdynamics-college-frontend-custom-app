import frappe

@frappe.whitelist(allow_guest=True)
def get_academic_types():
    docs = frappe.get_all(
        "Academic Type",
        fields=["thumbnail_image", "title", "content"]
    )
    return docs
