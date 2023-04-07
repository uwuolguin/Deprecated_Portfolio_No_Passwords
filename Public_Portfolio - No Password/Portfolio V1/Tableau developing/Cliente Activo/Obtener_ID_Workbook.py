import tableauserverclient as TSC

tableau_auth = TSC.PersonalAccessTokenAuth('', '', '')
server = TSC.Server('https://10ax.online.tableau.com/', use_server_version=True)
server.auth.sign_in(tableau_auth)

with server.auth.sign_in(tableau_auth):
    all_workbooks_items, pagination_item = server.workbooks.get()
    print([(workbook.name,workbook.id) for workbook in all_workbooks_items])
    