import frappe

@frappe.whitelist()
def calculate_royalty(franchise, period, royalty_percent):
    """Calculate Royalty based on sales invoices"""
    total_sales = frappe.db.sql("""
        SELECT SUM(grand_total)
        FROM `tabSales Invoice`
        WHERE franchise = %s AND posting_date LIKE %s AND docstatus = 1
    """, (franchise, f"{period}%"))[0][0] or 0

    royalty_amount = total_sales * (royalty_percent / 100)

    royalty_invoice = frappe.new_doc("Franchise Royalty Invoice")
    royalty_invoice.franchise = franchise
    royalty_invoice.period = period
    royalty_invoice.total_sales = total_sales
    royalty_invoice.royalty_amount = royalty_amount
    royalty_invoice.insert()

    return royalty_invoice.name
