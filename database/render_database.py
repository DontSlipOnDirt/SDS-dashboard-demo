from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Relational Database Schema')

# Define tables with fields
tables = {
    "Products": ["ProductID (PK)", "ProductName", "CategoryID (FK)", "SupplierID (FK)", "UnitPrice"],
    "Categories": ["CategoryID (PK)", "CategoryName"],
    "Suppliers": ["SupplierID (PK)", "SupplierName"],
    "Customers": ["CustomerID (PK)", "CustomerName"],
    "Orders": ["OrderID (PK)", "CustomerID (FK)", "OrderDate", "Amount"],
    "OrderDetails": ["OrderID (FK)", "ProductID (FK)", "Quantity"]
}

# Add nodes for each table
for table, fields in tables.items():
    label = f"{table}|" + "\\l".join(fields) + "\\l"
    dot.node(table, label=label, shape='record')

# Add relationships (foreign keys)
relationships = [
    ("Products", "Categories"),  # Products.CategoryID -> Categories.CategoryID
    ("Products", "Suppliers"),   # Products.SupplierID -> Suppliers.SupplierID
    ("Orders", "Customers"),     # Orders.CustomerID -> Customers.CustomerID
    ("OrderDetails", "Orders"),  # OrderDetails.OrderID -> Orders.OrderID
    ("OrderDetails", "Products") # OrderDetails.ProductID -> Products.ProductID
]

# Draw edges for relationships
for src, dst in relationships:
    dot.edge(src, dst)

# Render the diagram
dot.render('relational_schema', format='png', cleanup=False)
