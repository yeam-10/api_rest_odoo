
import xmlrpc.client


url = ''
db = ''
username = 'admin'
password = ''


common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

 version = common.version()

print("details..",  version)


uid = common.authenticate(db, username, password, {})



models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))


partners_ids = models.execute_kw(db, uid, password,'res.partner', 'search',[[['customer', '=', True]]], {'offset': 10, 'limit': 5})

print("partners...", partners_ids)


 partners_count = models.execute_kw(db, uid, password,'res.partner', 'search_count', [[]])

print (" partners count", partners_count)



partner_reac = models.execute_kw(db, uid, password,'res.partner', 'read', [partners_ids], {'fields': ['id', 'name',]})


print (" partner_rec....")

for partner in partner_reac:
print(partner)


reds = models.execute_kw(db, uid, password,'res.partner', 'search_read',[[]],{'fields': ['id', 'name'], 'limit': 5})

#print("Search Read Result", reds)

for ab in reds:
print(ab)


#Create


new_contac = models.execute_kw(db, uid, password, 'res.partner', 'create', [{ 'name': "Anye", 'mobile':"1234"}])


print("new create", new_contac)































