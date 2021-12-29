from bson import ObjectId
import datetime

f2 = str([{'seller': {'_id': ObjectId('61c8845b6e36bb027a3640f7'), 'f_l_name': 'Clim Sacha', 'start_date': datetime.datetime(2012, 9, 1, 8, 0), 'salary': [{'price': 3000}, {'price': 600}, {'price': 10000}, {'price': 8000}, {'price': 4000}], 'delivery_time': 20, 'category': 'distributor'}}, {'seller': {'_id': ObjectId('61c8845b6e36bb027a3640f8'), 'f_l_name': 'Kucherin Petr', 'start_date': datetime.datetime(2012, 9, 12, 8, 0), 'salary': [{'price': 8000}, {'price': 3000}, {'price': 7500}, {'price': 4000}], 'delivery_time': 24, 'category': 'supplier'}}])
f = str({'_id': ObjectId('61c8101b9a757a85b6b8c757'), 'seller_name': 'Clim Sacha', 'date_in': datetime.datetime(2012, 9, 12, 8, 0), 'defect_number': 100})
f1 = str({'_id': ObjectId('61666c061328210d8eb97bb7'), 'name': 'Sportique', 'phone': '33-2257201', 'address': '172 Rue de Rivoli', 'city': 'Cannes', 'state': None, 'country': 'France', 'zip_code': '', 'creditRating': 'EXCELLENT', 'comments': 'Customer specializes in Soccer. Likes to order accessories in bright colors.'})
print(type(eval(f2)))
print(type(eval(f)))