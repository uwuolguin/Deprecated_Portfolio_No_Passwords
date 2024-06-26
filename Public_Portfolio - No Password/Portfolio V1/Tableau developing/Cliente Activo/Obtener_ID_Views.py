import tableauserverclient as TSC

tableau_auth = TSC.PersonalAccessTokenAuth('', '', '')
server = TSC.Server('https://10ax.online.tableau.com/', use_server_version=True)
server.auth.sign_in(tableau_auth)

workbook = server.workbooks.get_by_id('6993baa9-6eaf-4734-afbf-a6557d9b61d1')
print(workbook.id)

server.workbooks.populate_views(workbook)
print([(view.name, view.id) for view in workbook.views])