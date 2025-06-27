import frappe

@frappe.whitelist()
def assign_nearest_outlet(order_id, delivery_pincode):
    # Dummy logic for now: simply assign first available warehouse
    warehouse = frappe.get_all("Warehouse", filters={"pincode": delivery_pincode}, limit=1)

    if not warehouse:
        frappe.throw("No warehouse found for given pincode")

    assigned_warehouse = warehouse[0].name

    order = frappe.get_doc("Online Order", order_id)
    order.assigned_warehouse = assigned_warehouse
    order.save()

    return assigned_warehouse
