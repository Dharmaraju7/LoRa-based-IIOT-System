import xml.etree.ElementTree as lib


def GenerateXML(fileName) :
	# hello
	root = lib.Element("GPS_DATA")

	m1 = lib.Element("staff")
	root.append (m1)

	b1 = lib.SubElement(m1, "id")
	b1.text = "1"
	b2 = lib.SubElement(m1, "lat")
	b2.text = "17.67173"
	b3 = lib.SubElement(m1, "long")
	b3.text = "83.21803"

	m2 = lib.Element("staff")
	root.append (m2)

	c1 = lib.SubElement(m2, "id")
	c1.text = "2"
	c2 = lib.SubElement(m2, "lat")
	c2.text = "18.67173"
	c3 = lib.SubElement(m2, "long")
	c3.text = "84.21803"

	m3 = lib.Element("staff")
	root.append (m3)

	d1 = lib.SubElement(m3, "id")
	d1.text = "3"
	d2 = lib.SubElement(m3, "lat")
	d2.text = "19.67173"
	d3 = lib.SubElement(m3, "long")
	d3.text = "85.21803"

	tree = lib.ElementTree(root)

	with open (fileName, "wb") as files :
		tree.write(files)

# Driver Code
if __name__ == "__main__":
	GenerateXML("gpsData.xml")
