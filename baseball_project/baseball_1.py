#coding:UTF-8
import urllib2
from bs4 import BeautifulSoup
import re
import gc
import urllib
import os
import shutil
import MySQLdb as mdb
from readability.readability import Document

const =2


'''
take name from gangraph(beta version)
'''
def get_name_fangraph(position):
	htmlfile = urllib2.urlopen("http://www.fangraphs.com/leaders.aspx?pos=cf&stats=bat&lg=all&qual=y&type=1&season=2015&month=0&season1=2015&ind=0&team=0&rost=0&age=0&filter=&players=0")

	htmlfile = urllib2.urlopen( "http://www.fangraphs.com/leaders.aspx?pos="+position+"&stats=bat&lg=all&qual=y&type=1&season=2015&month=0&season1=2015&ind=0&team=0&rost=0&age=0&filter=&players=0")
	htmltext = htmlfile.read()
	soup = BeautifulSoup(htmltext)
	a =soup.findAll('tr',attrs={"class":"rgRow"})
	b= soup.findAll('tr',attrs={"id":"LeaderBoard1_dg1_ctl00__"+str(const)})
	c= b[0].findAll('td',attrs={"class":"grid_line_regular"})
	d = c[1].text
	return d

'''
get dabase 
'''
def get_database():
	htmlfile=urllib2.urlopen("http://www.baseball-reference.com/leagues/MLB/2015-standard-batting.shtml#players_standard_batting::none")

	htmltext = htmlfile.read()

	soup = BeautifulSoup(htmltext)
	con = mdb.connect('localhost', 'root', '940729mumu', 'testdb')
	with con:
		cur=con.cursor()
		cur.execute("DROP TABLE IF EXISTS Major")
		cur.execute("CREATE TABLE Major(Id INT PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(40),1B INT,2B INT,3B INT,HR INT)")
	a =soup.findAll('tbody')
	playerlist = a[1].findAll('tr')
	for i in range(100):
		dic = playerlist[i].attrs
		print dic["class"]
		if len(dic["class"])==1 or dic["class"][1]!="thead":
			player = playerlist[i].findAll('td',attrs={"align":"right"})
			player2 = playerlist[i].findAll('td',attrs={"align":"left"})
			name_player = player2[0].text
			name_player = name_player.replace("#","")
			name_player = name_player.replace("*","")
			name_player = name_player.encode("utf8")
			name_player = name_player.replace('\xc2\xa0',' ')
			print name_player
			c = name_player.split()
			print c
			hit_1 = player[5].text
			hit_2 = player[6].text
			hit_3 = player[7].text
			hit_4 = player[8].text
			qq = 4
			name ="aa"
			with con:
				cur.execute("INSERT INTO Major(Name,1B,2B,3B,HR) VALUES(%s,%s,%s,%s,%s)",(name_player,hit_1,hit_2,hit_3,hit_4))

'''
get databse 
'''
def get_database2(position):
	url="http://www.fangraphs.com/leaders.aspx?pos="+position+"&stats=bat&lg=all&qual=y&type=8&season=2015&month=0&season1=2015&ind=0&team=0&rost=0&age=0&filter=&players=0"
	htmlfile=urllib2.urlopen(url)

	htmltext = htmlfile.read()

	soup = BeautifulSoup(htmltext)
	con = mdb.connect('localhost', 'root', '940729mumu', 'testdb')
	with con:
		cur=con.cursor()
		cur.execute("DROP TABLE IF EXISTS Major2"+position)
		cur.execute("CREATE TABLE Major2"+position+"(Id INT PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(40),AVERAGE FLOAT,WRC FLOAT,OFF FLOAT,DEF FLOAT,WAR FLOAT)")
	a =soup.findAll('tr',attrs={"class":"rgRow"})
	for j in range(100):
		b= soup.findAll('tr',attrs={"id":"LeaderBoard1_dg1_ctl00__"+str(j)})
		#print b
		#print j
		if(len(b))==0:
			gc.collect()
			return 0
		c= b[0].findAll('td')
		name = c[1].text
		average =float(c[13].text) ##average
		wrc = float(c[17].text) ##wRC+
		off_war = float(c[19].text) ##OFF
		def_war = float(c[20].text) ##DEF
		war = float(c [21].text) ##WAR
		#print name,average,wrc
		with con:
				cur.execute("INSERT INTO Major2"+position+"(Name,AVERAGE,WRC,OFF,DEF,WAR) VALUES(%s,%s,%s,%s,%s,%s)",(name,average,wrc,off_war,def_war,war))

'''
get picture from wiki
'''	
def get_picture(name_player):
	print name_player
	htmlfile2 =urllib2.urlopen("https://en.wikipedia.org/wiki/"+name_player)
	htmltext2 = htmlfile2.read()
	soup = BeautifulSoup(htmltext2)
	img = soup.findAll('img')
	change_name = name_player.split()
	for i in range(3):
		if img[i].attrs["alt"]=="Disambiguation icon":
			htmlfile2 =urllib2.urlopen("https://en.wikipedia.org/wiki/"+change_name[0]+"_"+change_name[1]+"_(baseball)")
			##print "https://en.wikipedia.org/wiki/"+change_name[0]+"_"+change_name[1]+"_(baseball)"
			htmltext2 = htmlfile2.read()
			soup = BeautifulSoup(htmltext2)
			break
	img = soup.findAll('img')
	print "legth",len(img)
	url=""
	for i in range(7):
		print i
		print img[i]
		dic =img[i].attrs
		#print dic["alt"]
		if (change_name[0] in dic["alt"]) or(change_name[1] in dic["alt"]) :
			url = "http:"+dic["src"]
			break
	
	current_adress = os.getcwd()
	os.chdir('images')
	print url
	if "jpg" in url or 'JPG' in url:
		judge_1 = 1
		urllib.urlretrieve(url, name_player+".jpg")
	elif "png" in url or 'PNG' in url:
		judge_1 = 2
		urllib.urlretrieve(url, name_player+".png")
	os.chdir('../')
	return judge_1

def get_picture_2(name_player):
	print name_player
	htmlfile2 =urllib2.urlopen("https://en.wikipedia.org/wiki/"+name_player)
	htmltext2 = htmlfile2.read()
	soup = BeautifulSoup(htmltext2)
	change_name = name_player.split()
	
	for i in range(3):
		if img[i].attrs["alt"]=="Disambiguation icon":
			htmlfile2 =urllib2.urlopen("https://en.wikipedia.org/wiki/"+change_name[0]+"_"+change_name[1]+"_(baseball)")
			##print "https://en.wikipedia.org/wiki/"+change_name[0]+"_"+change_name[1]+"_(baseball)"
			htmltext2 = htmlfile2.read()
			soup = BeautifulSoup(htmltext2)
			break
	img = soup.findAll('img')
	print "legth",len(img)
	url=""
	for i in range(7):
		print i
		print img[i]
		dic =img[i].attrs
		#print dic["alt"]
		if (change_name[0] in dic["alt"]) or(change_name[1] in dic["alt"]) :
			url = "http:"+dic["src"]
			break
	
	current_adress = os.getcwd()
	os.chdir('images')
	print url
	if "jpg" in url or 'JPG' in url:
		judge_1 = 1
		urllib.urlretrieve(url, name_player+".jpg")
	elif "png" in url or 'PNG' in url:
		judge_1 = 2
		urllib.urlretrieve(url, name_player+".png")
	os.chdir('../')
	return judge_1

def get_picture_2(name_player):
	print name_player
	print "https://en.wikipedia.org/wiki/"+name_player
	htmlfile2 =urllib2.urlopen("https://en.wikipedia.org/wiki/"+name_player)
	htmltext2 = htmlfile2.read()
	soup = BeautifulSoup(htmltext2)
	change_name = name_player.split()
	img = soup.findAll('img')
	for i in range(3):
		if img[i].attrs["alt"]=="Disambiguation icon":
			htmlfile2 =urllib2.urlopen("https://en.wikipedia.org/wiki/"+change_name[0]+"_"+change_name[1]+"_(baseball)")
			##print "https://en.wikipedia.org/wiki/"+change_name[0]+"_"+change_name[1]+"_(baseball)"
			htmltext2 = htmlfile2.read()
			soup = BeautifulSoup(htmltext2)
			break
	table = soup.findAll('table',attrs={"class":"infobox bordered vcard"})
	img = table[0].findAll('img')
	dic =img[0].attrs
	url = "http:"+dic["src"]
	current_adress = os.getcwd()
	os.chdir('images')
	print url
	if "jpg" in url or 'JPG' in url:
		judge_1 = 1
		urllib.urlretrieve(url, name_player+".jpg")
	elif "png" in url or 'PNG' in url:
		judge_1 = 2
		urllib.urlretrieve(url, name_player+".png")
	os.chdir('../')
	return judge_1
'''
get bast defensive player with respect to each position
'''
def get_name_fielding(position,number):
	con = mdb.connect('localhost', 'root', '940729mumu', 'testdb')
	with con:
		cur=con.cursor()
		cur.execute("SELECT * from Major2"+position+" ORDER BY DEF DESC LIMIT %s,%s",(number,1))
		data = cur.fetchone()
		name =data[1]
		average = data[2]
		OFF = data[4]
		DEF =data[5]
		WAR = data[6]
		gc.collect()
		return [name,average,OFF,DEF,WAR]
'''
get bast defensive player with respect to each position
'''
def get_name_batting(position,number):
	con = mdb.connect('localhost', 'root', '940729mumu', 'testdb')
	with con:
		cur=con.cursor()
		cur.execute("SELECT * from Major2"+position+" ORDER BY OFF DESC LIMIT %s,%s",(number,1))
		data = cur.fetchone()
		name =data[1]
		average = data[2]
		OFF = data[4]
		DEF =data[5]
		WAR = data[6]
		gc.collect()
		return [name,average,OFF,DEF,WAR]
		
		gc.collect()
		return name

def make_images():
	if os.path.exists(current_adress+"/images"):
		pass
	else:
		os.mkdir("images")
		
###main function
if __name__ == "__main__":
	get_picture_2("Eric_Hosmer")


