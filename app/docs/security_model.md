                    ┌───────────────────────────┐
                    │         Internet          │
                    └─────────────┬─────────────┘
                                  │
                                  │ TLS / HTTPS
                                  ▼
                    ┌───────────────────────────┐
                    │     Reverse Proxy Layer   │
                    │       Nginx Firewall      │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                    ┌───────────────────────────┐
                    │  Authentication Service   │
                    │                           │
                    │ Password Hashing (bcrypt) │
                    │ MFA Authentication        │
                    │ JWT Token Issuance        │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                    ┌───────────────────────────┐
                    │  Authorization Layer      │
                    │  Role Based Access (RBAC) │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                    ┌───────────────────────────┐
                    │   Application Services    │
                    │                           │
                    │ Procurement Engine        │
                    │ Inventory Management      │
                    │ Shipment Tracking         │
                    │ AI Analytics              │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                    ┌───────────────────────────┐
                    │     Database Security     │
                    │                           │
                    │ Encrypted connections     │
                    │ Parameterized queries     │
                    │ Access control policies   │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                    ┌───────────────────────────┐
                    │ Monitoring & Audit Logs   │
                    │                           │
                    │ Login tracking            │
                    │ Data modification logs    │
                    │ Security alerts           │
                    └───────────────────────────┘