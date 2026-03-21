                          ┌───────────────────────────────┐
                          │            Users              │
                          │  Admin | Procurement | Ops    │
                          └───────────────┬───────────────┘
                                          │
                                          │ HTTPS / TLS
                                          ▼
                          ┌───────────────────────────────┐
                          │        Web Interface          │
                          │  Streamlit UI (Frontend)      │
                          └───────────────┬───────────────┘
                                          │
                                          │ Secure API Calls
                                          ▼
                          ┌───────────────────────────────┐
                          │        Application Layer      │
                          │                               │
                          │ Authentication Service        │
                          │ Authorization (RBAC)          │
                          │ AI Analytics Engine           │
                          │ Procurement Engine            │
                          │ Shipment Tracking             │
                          └───────────────┬───────────────┘
                                          │
                                          │ ORM / Queries
                                          ▼
                          ┌───────────────────────────────┐
                          │        Data Access Layer      │
                          │        SQLAlchemy ORM         │
                          └───────────────┬───────────────┘
                                          │
                                          │ Secure Connection
                                          ▼
                          ┌───────────────────────────────┐
                          │           Database            │
                          │          PostgreSQL           │
                          │                               │
                          │ Users                         │
                          │ Companies                     │
                          │ Suppliers                     │
                          │ Purchase Orders               │
                          │ Inventory                     │
                          │ Shipments                     │
                          │ Audit Logs                    │
                          └───────────────┬───────────────┘
                                          │
                                          │ Data Backup
                                          ▼
                          ┌───────────────────────────────┐
                          │     Backup & Recovery Layer   │
                          │     Encrypted Cloud Storage   │
                          └───────────────────────────────┘