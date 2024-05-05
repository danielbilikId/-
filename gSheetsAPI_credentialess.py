import pygsheets
def update_google_sheet(people_file):
    gc = pygsheets.authorize(service_file= r"C:\noFile")
    sh = gc.open_by_key('none')
    wks = sh[0]
    wks.set_dataframe(people_file, (1, 1), copy_head=True)
    


