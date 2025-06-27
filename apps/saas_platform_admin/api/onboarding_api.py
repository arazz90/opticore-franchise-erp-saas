import frappe

@frappe.whitelist(allow_guest=False)
def onboard_new_tenant(company_name, admin_user, admin_email):
    company = frappe.new_doc("Company")
    company.company_name = company_name
    company.insert()

    user = frappe.new_doc("User")
    user.email = admin_email
    user.first_name = admin_user
    user.send_welcome_email = 0
    user.insert()

    return {
        "tenant_company": company.name,
        "tenant_admin_user": user.name
    }
