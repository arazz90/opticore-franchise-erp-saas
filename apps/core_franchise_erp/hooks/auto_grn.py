import frappe

@frappe.whitelist()
def create_auto_grn(doc, method):
    """Auto create GRN (Stock Entry - Material Receipt) when Delivery Note is submitted"""
    if doc.destination_warehouse:
        grn = frappe.new_doc("Stock Entry")
        grn.stock_entry_type = "Material Receipt"
        grn.items = []
        for item in doc.items:
            grn.append("items", {
                "item_code": item.item_code,
                "qty": item.qty,
                "uom": item.uom,
                "basic_rate": item.basic_rate,
                "target_warehouse": doc.destination_warehouse
            })
        grn.insert()
        grn.submit()
