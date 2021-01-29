from xml.dom import minidom 

doc = minidom.parse("gpsData.xml") 

# doc.getElementsByTagName returns the NodeList 

staffs = doc.getElementsByTagName("staff") 
for staff in staffs: 
		staff_id = staff.getElementsByTagName("id")[0]
		lat = staff.getElementsByTagName("lat")[0] 
		log = staff.getElementsByTagName("long")[0] 
		print("id:% s, lat:% s, long:% s" %
			(staff_id.firstChild.data, lat.firstChild.data, log.firstChild.data)) 
