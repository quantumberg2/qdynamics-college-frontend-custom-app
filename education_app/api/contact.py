import frappe
import json

@frappe.whitelist(allow_guest=True)
def send_contact_message():
    """Save contact form submission and send email"""
    data = frappe.local.form_dict

    # If frontend sends JSON body, parse it
    if isinstance(data, str):
        data = json.loads(data)

    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email_address = data.get("email_address")
    message = data.get("message")

    # Save into College-Public-Website-Contact Doctype
    doc = frappe.get_doc({
        "doctype": "College-Public-Website-Contact",
        "first_name": first_name,
        "last_name": last_name,
        "email_address": email_address,
        "message": message
    })
    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    # Send email to admin
    frappe.sendmail(
        recipients=["wequantumberg@gmail.com"],   # change to your inbox
        sender="wequantumberg@gmail.com",         # must match configured Email Account
        reply_to=email_address,
        subject=f"New Contact Form Submission from {first_name} {last_name}",
        message=f"""
            <b>First Name:</b> {first_name}<br>
            <b>Last Name:</b> {last_name}<br>
            <b>Email:</b> {email_address}<br>
            <b>Message:</b> {message}
        """,
        delayed=False
    )

    return {"status": "success", "message": "Your message has been submitted successfully!"}
