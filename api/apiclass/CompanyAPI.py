from api.DB.db import DB


class CompanyAPI(DB):
    def set_companyes(self, result):
        if not result:
            return 'no company'
        if result[0][0] == 'error':
            return 'error'
        else:
            results = []
            for res in result:
                results.append({'company_id': res[0], 'company_name': res[1], 'phone_number': res[2]})
            return results

    def get_companyes(self, table):
        procedure = f'exec get_companyes {table}'
        result = self.execute_procedure(procedure)
        return self.set_companyes(result)

    def post_companyes(self, table, name, phone):
        procedure = f'exec post_companyes {table}, {name}, {phone}'
        result = self.execute_procedure(procedure)
        return self.set_companyes(result)
