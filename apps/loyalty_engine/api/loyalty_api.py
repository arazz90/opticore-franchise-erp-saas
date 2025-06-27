import frappe
from frappe import _

@frappe.whitelist(allow_guest=False)
def get_wallet_balance(customer):
    wallet = frappe.get_doc("Loyalty Wallet", {"customer": customer})
    return {
        "customer": customer,
        "balance_points": wallet.balance_points
    }

@frappe.whitelist(allow_guest=False)
def redeem_wallet_points(customer, redeem_points):
    wallet = frappe.get_doc("Loyalty Wallet", {"customer": customer})
    if redeem_points > wallet.balance_points:
        frappe.throw(_("Insufficient points."))
    wallet.balance_points -= redeem_points
    wallet.save()
    return {
        "customer": customer,
        "updated_balance": wallet.balance_points
    }
