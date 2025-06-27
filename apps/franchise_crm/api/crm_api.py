import frappe

@frappe.whitelist(allow_guest=True)
def create_franchise_lead(lead_name, contact_number, email, preferred_location):
    lead = frappe.new_doc("Franchise Lead")
    lead.lead_name = lead_name
    lead.contact_number = contact_number
    lead.email = email
    lead.preferred_location = preferred_location
    lead.insert()
    return {"status": "success", "lead_id": lead.name}
