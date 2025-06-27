import frappe

frappe.whitelist(methods=["POST"])
def loyalty_wallet():
    if frappe.request.method == "POST":
        data = frappe.request.get_json()
        customer = data.get("customer")
        from .loyalty_api import get_wallet_balance
        return get_wallet_balance(customer)
