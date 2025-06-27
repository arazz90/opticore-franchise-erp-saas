import frappe
import argparse
import sys

def create_franchise_user(email, first_name, franchise):
    try:
        user = frappe.new_doc("User")
        user.email = email
        user.first_name = first_name
        user.send_welcome_email = 0
        user.insert()

        # Assign franchise-specific role
        user.add_roles("Franchise Manager")

        # Assign custom property (franchise linkage)
        user.set("franchise", franchise)
        user.save()

        print(f"✅ Franchise User Created: {email}")
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Franchise User Provisioning Tool")
    parser.add_argument("email", help="User Email")
    parser.add_argument("first_name", help="First Name")
    parser.add_argument("franchise", help="Franchise Company Name")
    args = parser.parse_args()

    frappe.init(site="opticore.local")
    frappe.connect()
    create_franchise_user(args.email, args.first_name, args.franchise)
    frappe.destroy()
