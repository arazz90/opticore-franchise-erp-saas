import frappe
import argparse
import sys

"""
CLI script to automate SaaS tenant onboarding
"""

def onboard_tenant(company_name, admin_user, admin_email):
    try:
        # Create Company
        company = frappe.new_doc("Company")
        company.company_name = company_name
        company.insert()

        # Create Admin User
        user = frappe.new_doc("User")
        user.email = admin_email
        user.first_name = admin_user
        user.send_welcome_email = 0
        user.insert()

        # Assign Roles
        user.add_roles("System Manager")
        frappe.db.commit()

        print(f"✅ Tenant created: {company_name} with admin {admin_email}")
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SaaS Tenant Onboarding Tool")
    parser.add_argument("company_name", help="Name of the tenant company")
    parser.add_argument("admin_user", help="Name of the admin user")
    parser.add_argument("admin_email", help="Email of the admin user")
    args = parser.parse_args()

    frappe.init(site="opticore.local")
    frappe.connect()
    onboard_tenant(args.company_name, args.admin_user, args.admin_email)
    frappe.destroy()
