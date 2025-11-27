import frappe

@frappe.whitelist(allow_guest=True)  # make it public
def get_announcements():
    docs = frappe.get_all(
        "Education Announcement",
        fields=["announcement_created_date", "announcement_title", "announcement_contant"],
        order_by="announcement_created_date desc"  # latest first
    )
    return docs
