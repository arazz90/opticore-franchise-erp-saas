import frappe

@frappe.whitelist(allow_guest=False)
def route_order(order_id, delivery_pincode):
    warehouse = frappe.get_all("Warehouse", filters={"pincode": delivery_pincode}, limit=1)
    if not warehouse:
        frappe.throw("No warehouse found for delivery pincode")
    assigned_warehouse = warehouse[0].name
    order = frappe.get_doc("Online Order", order_id)
    order.assigned_warehouse = assigned_warehouse
    order.save()
    return {"assigned_warehouse": assigned_warehouse}
