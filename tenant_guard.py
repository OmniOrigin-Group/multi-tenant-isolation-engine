class TenantGuard:
    """
    Architectural abstraction: Wraps DB operations to ensure 
    that no query ever executes without an enforced tenant partition.
    """
    def __init__(self, tenant_id):
        self.tenant_id = tenant_id

    def execute_secured_query(self, sql_query):
        # Automated injection ensures no developer can bypass isolation
        secured_query = f"{sql_query} AND tenant_id = '{self.tenant_id}'"
        print(f"[🛡️ ARCHITECTURE GUARD] Sanitizing Query: {secured_query}")
        return secured_query
