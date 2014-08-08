from PIL import Image

def loadImage(imgUrl):
	'''
		Load Image url
	'''
	return Image.open(imgUrl)

def getPixels(imgResources):
	return imgResources.load()


img = loadImage('python.png')
pixels = getPixels(img)

strHtml = ''
rgbaHtml = 'rgba({},{},{},{})'
innerObj = '<span style="color: {}; font-size: 8px;">()</span>'.format(rgbaHtml)

f = open('index.html','w')

for i in range(img.size[0]):
	strHtml = strHtml + '<br>'
	for j in range(img.size[1]):
		px = pixels[i,j]
		if px[3] == 0:
			strHtml += "&nbsp;"
		else:
			strHtml += innerObj.format(px[0],px[1],px[2],px[3])
			
f.write(strHtml)
