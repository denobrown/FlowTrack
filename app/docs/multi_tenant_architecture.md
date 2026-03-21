                 ┌─────────────────────────────────┐
                 │         FlowTrack SaaS          │
                 └─────────────────────────────────┘
                               │
                               ▼
                 ┌─────────────────────────────────┐
                 │          Tenant Layer           │
                 │                                 │
                 │ Company A                       │
                 │ Company B                       │
                 │ Company C                       │
                 └─────────────────────────────────┘
                               │
                               ▼
                 ┌─────────────────────────────────┐
                 │        Shared Application       │
                 │                                 │
                 │ Authentication                  │
                 │ Procurement Engine              │
                 │ Shipment Tracking               │
                 │ AI Analytics                    │
                 └─────────────────────────────────┘
                               │
                               ▼
                 ┌─────────────────────────────────┐
                 │         Shared Database         │
                 │                                 │
                 │ company_id column enforces      │
                 │ tenant isolation                │
                 └─────────────────────────────────┘