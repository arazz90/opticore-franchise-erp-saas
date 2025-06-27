import frappe

@frappe.whitelist()
def earn_loyalty_points(customer, invoice_amount):
    program = frappe.get_doc("Loyalty Program Setup", {"active": 1})
    earned_points = invoice_amount * (program.earning_percentage / 100)

    wallet = frappe.get_doc("Loyalty Wallet", {"customer": customer})
    wallet.balance_points += earned_points
    wallet.last_earn_date = frappe.utils.nowdate()
    wallet.save()

    return wallet.balance_points

@frappe.whitelist()
def redeem_loyalty_points(customer, redeem_points):
    wallet = frappe.get_doc("Loyalty Wallet", {"customer": customer})
    if redeem_points > wallet.balance_points:
        frappe.throw("Insufficient points")
    wallet.balance_points -= redeem_points
    wallet.save()
    return wallet.balance_points
