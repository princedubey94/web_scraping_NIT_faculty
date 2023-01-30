# NAME:PRINCE KUMAR DUBEY
# ROLL NO. :12112094
# SECTION:CS_B_05
import requests
from bs4 import BeautifulSoup
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
url="https://nitkkr.ac.in/?page_id=791"
r=requests.get(url)
htmlContent= r.content
soup=BeautifulSoup(htmlContent,'html.parser')
name=soup.find_all("div",class_="hd")
for h in name:
    name_list.append(h.h3.text.replace(u'\xa0', u' '))
designation=soup.find_all("i",class_="fa fa-briefcase")
for d in designation:
    designation_list.append(d.next_sibling.replace(u'\xa0', u' '))    
email=soup.find_all("i",class_="fa fa-envelope default-mail")
for d in email:
    email_list.append(d.next_sibling.replace(u'\xa0', u' '))
contact=soup.find_all("i",class_="fa fa-phone default-mail")
for c in contact:
    contact_list.append(c.next_sibling.replace(u'\xa0', u' '))
area_of_interest=soup.find_all("div",class_="left-sec")
for d in area_of_interest:
    aoi_list.append(d.p.text.replace(u'\xa0', u' ')) 
email_list.pop(0)
contact_list.pop(0)
file=open("faculty.txt","w")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  
url="https://nitkkr.ac.in/?page_id=1154"
r=requests.get(url)
htmlContent= r.content
soup=BeautifulSoup(htmlContent,'html.parser')
name=soup.find_all("div",class_="hd")
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
for h in name:
    name_list.append(h.h3.text.replace(u'\xa0', u' '))
designation=soup.find_all("i",class_="fa fa-briefcase")
for d in designation:
    designation_list.append(d.next_sibling.replace(u'\xa0', u' '))    
email=soup.find_all("i",class_="fa fa-envelope default-mail")
for d in email:
    email_list.append(d.next_sibling.replace(u'\xa0', u' '))
contact=soup.find_all("i",class_="fa fa-phone default-mail")
for c in contact:
    contact_list.append(c.next_sibling.replace(u'\xa0', u' '))
area_of_interest=soup.find_all("div",class_="left-sec")
for d in area_of_interest:
    aoi_list.append(d.p.text.replace(u'\xa0', u' ')) 
email_list.pop(0)
contact_list.pop(0)
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]    
url="https://nitkkr.ac.in/?page_id=1953"
r=requests.get(url)
htmlContent= r.content
soup=BeautifulSoup(htmlContent,'html.parser')
name=soup.find_all("div",class_="hd")
for h in name:
    name_list.append(h.h3.text.replace(u'\xa0', u' '))
designation=soup.find_all("i",class_="fa fa-briefcase")
for d in designation:
    designation_list.append(d.next_sibling.replace(u'\xa0', u' '))    
email=soup.find_all("i",class_="fa fa-envelope default-mail")
for d in email:
    email_list.append(d.next_sibling.replace(u'\xa0', u' '))
contact=soup.find_all("i",class_="fa fa-phone default-mail")
for c in contact:
    contact_list.append(c.next_sibling.replace(u'\xa0', u' '))
area_of_interest=soup.find_all("div",class_="left-sec")
for d in area_of_interest:
    aoi_list.append(d.p.text.replace(u'\xa0', u' ')) 
email_list.pop(0)
contact_list.pop(0)
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")
url="https://nitkkr.ac.in/?page_id=1100"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent= r.content
soup=BeautifulSoup(htmlContent,'html.parser')
name=soup.find_all("div",class_="hd")
for h in name:
    name_list.append(h.h3.text.replace(u'\xa0', u' '))
designation=soup.find_all("i",class_="fa fa-briefcase")
for d in designation:
    designation_list.append(d.next_sibling.replace(u'\xa0', u' '))    
email=soup.find_all("i",class_="fa fa-envelope default-mail")
for d in email:
    email_list.append(d.next_sibling.replace(u'\xa0', u' '))
contact=soup.find_all("i",class_="fa fa-phone default-mail")
for c in contact:
    contact_list.append(c.next_sibling.replace(u'\xa0', u' '))
area_of_interest=soup.find_all("div",class_="left-sec")
for d in area_of_interest:
    aoi_list.append(d.p.text.replace(u'\xa0', u' ')) 
email_list.pop(0)
contact_list.pop(0)
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")
url="https://www.nitt.edu/home/academics/departments/faculty/"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent= r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("tr")
for n in data:
    name=n.find_all('td')[2].text
    name_list.append(name)
    contact_list.append("NOT AVAILABLE") 
    aoi_list.append("NOT AVAILABLE")   
for n in data:
    name=n.find_all('td')[4].text
    designation_list.append(name) 
for n in data:
    name=n.find_all('td')[6].text
    email_list.append(name+"@nitt.edu")  
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")             
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]    
url="https://wsdc.nitw.ac.in/facultynew/dept/faculty_profiles/cse"
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="rightm")
for i in data:
    name_list.append(i.find_all("p")[0].text)
    designation_list.append(i.find_all("p")[1].text)
    contact_list.append(i.find_all("p")[2].text)
    email_list.append(i.find_all("p")[3].text) 
    aoi_list.append("NOT AVAILABLE") 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")      
url="https://wsdc.nitw.ac.in/facultynew/dept/faculty_profiles/ece"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="rightm")
for i in data:
    name_list.append(i.find_all("p")[0].text)
    designation_list.append(i.find_all("p")[1].text)
    contact_list.append(i.find_all("p")[2].text)
    email_list.append(i.find_all("p")[3].text) 
    aoi_list.append("NOT AVAILABLE") 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")       
url="https://wsdc.nitw.ac.in/facultynew/dept/faculty_profiles/ee"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="rightm")
for i in data:
    name_list.append(i.find_all("p")[0].text)
    designation_list.append(i.find_all("p")[1].text)
    contact_list.append(i.find_all("p")[2].text)
    email_list.append(i.find_all("p")[3].text) 
    aoi_list.append("NOT AVAILABLE") 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")   
url="https://wsdc.nitw.ac.in/facultynew/dept/faculty_profiles/che"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="rightm")
for i in data:
    name_list.append(i.find_all("p")[0].text)
    designation_list.append(i.find_all("p")[1].text)
    contact_list.append(i.find_all("p")[2].text)
    email_list.append(i.find_all("p")[3].text) 
    aoi_list.append("NOT AVAILABLE") 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n") 
url="https://wsdc.nitw.ac.in/facultynew/dept/faculty_profiles/ce"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="rightm")
for i in data:
    name_list.append(i.find_all("p")[0].text)
    designation_list.append(i.find_all("p")[1].text)
    contact_list.append(i.find_all("p")[2].text)
    email_list.append(i.find_all("p")[3].text) 
    aoi_list.append("NOT AVAILABLE") 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n") 
url="https://wsdc.nitw.ac.in/facultynew/dept/faculty_profiles/mme"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="rightm")
for i in data:
    name_list.append(i.find_all("p")[0].text)
    designation_list.append(i.find_all("p")[1].text)
    contact_list.append(i.find_all("p")[2].text)
    email_list.append(i.find_all("p")[3].text) 
    aoi_list.append("NOT AVAILABLE") 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n") 
url="https://wsdc.nitw.ac.in/facultynew/dept/faculty_profiles/me"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="rightm")
for i in data:
    name_list.append(i.find_all("p")[0].text)
    designation_list.append(i.find_all("p")[1].text)
    contact_list.append(i.find_all("p")[2].text)
    email_list.append(i.find_all("p")[3].text) 
    aoi_list.append("NOT AVAILABLE") 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n") 
url="https://wsdc.nitw.ac.in/facultynew/dept/faculty_profiles/mat"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="rightm")
for i in data:
    name_list.append(i.find_all("p")[0].text)
    designation_list.append(i.find_all("p")[1].text)
    contact_list.append(i.find_all("p")[2].text)
    email_list.append(i.find_all("p")[3].text) 
    aoi_list.append("NOT AVAILABLE") 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n") 
url="https://wsdc.nitw.ac.in/facultynew/dept/faculty_profiles/cy"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="rightm")
for i in data:
    name_list.append(i.find_all("p")[0].text)
    designation_list.append(i.find_all("p")[1].text)
    contact_list.append(i.find_all("p")[2].text)
    email_list.append(i.find_all("p")[3].text) 
    aoi_list.append("NOT AVAILABLE") 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n") 
url="https://wsdc.nitw.ac.in/facultynew/dept/faculty_profiles/phy"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="rightm")
for i in data:
    name_list.append(i.find_all("p")[0].text)
    designation_list.append(i.find_all("p")[1].text)
    contact_list.append(i.find_all("p")[2].text)
    email_list.append(i.find_all("p")[3].text) 
    aoi_list.append("NOT AVAILABLE") 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n") 
url="https://mnit.ac.in/dept_cse/people"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="col-md-9 mt-3 profileDetails")
for i in data:
    name_list.append(i.h5.text)
    designation_list.append(i.find_all("span")[0].text)
    aoi_list.append(i.find_all("span")[2].text)
    email_list.append(i.find_all("span")[3].text)
    contact_list.append(i.find_all("span")[4].text) 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n") 
url="https://mnit.ac.in/dept_mech/people"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="col-md-9 mt-3 profileDetails")
for i in data:
    name_list.append(i.h5.text)
    designation_list.append(i.find_all("span")[0].text)
    aoi_list.append(i.find_all("span")[2].text)
    email_list.append(i.find_all("span")[3].text)
    contact_list.append(i.find_all("span")[4].text) 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  
url="https://mnit.ac.in/dept_chemical/people"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="col-md-9 mt-3 profileDetails")
for i in data:
    name_list.append(i.h5.text)
    designation_list.append(i.find_all("span")[0].text)
    aoi_list.append(i.find_all("span")[2].text)
    email_list.append(i.find_all("span")[3].text)
    contact_list.append(i.find_all("span")[4].text) 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n") 
url="https://mnit.ac.in/dept_chemistry/people"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="col-md-9 mt-3 profileDetails")
for i in data:
    name_list.append(i.h5.text)
    designation_list.append(i.find_all("span")[0].text)
    aoi_list.append(i.find_all("span")[2].text)
    email_list.append(i.find_all("span")[3].text)
    contact_list.append(i.find_all("span")[4].text) 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")   
url="https://mnit.ac.in/dept_civil/people"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="col-md-9 mt-3 profileDetails")
for i in data:
    name_list.append(i.h5.text)
    designation_list.append(i.find_all("span")[0].text)
    aoi_list.append(i.find_all("span")[2].text)
    email_list.append(i.find_all("span")[3].text)
    contact_list.append(i.find_all("span")[4].text) 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")   
url="https://mnit.ac.in/dept_ee/people"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="col-md-9 mt-3 profileDetails")
for i in data:
    name_list.append(i.h5.text)
    designation_list.append(i.find_all("span")[0].text)
    aoi_list.append(i.find_all("span")[2].text)
    email_list.append(i.find_all("span")[3].text)
    contact_list.append(i.find_all("span")[4].text) 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")         
url="https://mnit.ac.in/dept_ece/people"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="col-md-9 mt-3 profileDetails")
for i in data:
    name_list.append(i.h5.text)
    designation_list.append(i.find_all("span")[0].text)
    aoi_list.append(i.find_all("span")[2].text)
    email_list.append(i.find_all("span")[3].text)
    contact_list.append(i.find_all("span")[4].text) 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  
url="https://mnit.ac.in/dept_math/people"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="col-md-9 mt-3 profileDetails")
for i in data:
    name_list.append(i.h5.text)
    designation_list.append(i.find_all("span")[0].text)
    aoi_list.append(i.find_all("span")[2].text)
    email_list.append(i.find_all("span")[3].text)
    contact_list.append(i.find_all("span")[4].text) 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")      
url="https://mnit.ac.in/dept_mme/people"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="col-md-9 mt-3 profileDetails")
for i in data:
    name_list.append(i.h5.text)
    designation_list.append(i.find_all("span")[0].text)
    aoi_list.append(i.find_all("span")[2].text)
    email_list.append(i.find_all("span")[3].text)
    contact_list.append(i.find_all("span")[4].text) 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n") 
url="https://mnit.ac.in/dept_physics/people"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="col-md-9 mt-3 profileDetails")
for i in data:
    name_list.append(i.h5.text)
    designation_list.append(i.find_all("span")[0].text)
    aoi_list.append(i.find_all("span")[2].text)
    email_list.append(i.find_all("span")[3].text)
    contact_list.append(i.find_all("span")[4].text) 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")                 
url="https://nitdgp.ac.in/department/computer-science-engineering/faculty-1"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("h4",class_="card-title")
for i in data:
    name_list.append(i.text)
    designation_list.append(i.next_sibling.text)
data=soup.find_all("div",class_="card-body")
for i in data:
    aoi_list.append(i.p.text)    
data=soup.find_all("i",class_="fa fa-envelope")
for i in data:
    email_list.append(i.next_sibling.text)
email_list.pop(0)        
data=soup.find_all("i",class_="fa fa-phone")
for i in data:
    contact_list.append(i.next_sibling.text)  
contact_list.pop(0)    
name_list.pop(len(name_list)-1)
name_list.pop(len(name_list)-1)
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")     
url="https://nitdgp.ac.in/department/biotechnology/faculty-2"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("h4",class_="card-title")
for i in data:
    name_list.append(i.text)
    designation_list.append(i.next_sibling.text)
data=soup.find_all("div",class_="card-body")
for i in data:
    aoi_list.append(i.p.text)    
data=soup.find_all("i",class_="fa fa-envelope")
for i in data:
    email_list.append(i.next_sibling.text)
email_list.pop(0)        
data=soup.find_all("i",class_="fa fa-phone")
for i in data:
    contact_list.append(i.next_sibling.text)  
contact_list.pop(0)    
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")     
url="https://nitdgp.ac.in/department/civil-engineering/faculty-3"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("h4",class_="card-title")
for i in data:
    name_list.append(i.text)
    designation_list.append(i.next_sibling.text)
data=soup.find_all("div",class_="card-body")
for i in data:
    aoi_list.append(i.p.text)    
data=soup.find_all("i",class_="fa fa-envelope")
for i in data:
    email_list.append(i.next_sibling.text)
email_list.pop(0)        
data=soup.find_all("i",class_="fa fa-phone")
for i in data:
    contact_list.append(i.next_sibling.text)  
contact_list.pop(0)    
name_list.pop(len(name_list)-1)
name_list.pop(len(name_list)-1)
name_list.pop(len(name_list)-1)
name_list.pop(len(name_list)-1)
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")    
url="https://nitdgp.ac.in/department/chemical-engineering/faculty-4"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("h4",class_="card-title")
for i in data:
    name_list.append(i.text)
    designation_list.append(i.next_sibling.text)
data=soup.find_all("div",class_="card-body")
for i in data:
    aoi_list.append(i.p.text)    
data=soup.find_all("i",class_="fa fa-envelope")
for i in data:
    email_list.append(i.next_sibling.text)
email_list.pop(0)        
data=soup.find_all("i",class_="fa fa-phone")
for i in data:
    contact_list.append(i.next_sibling.text)  
contact_list.pop(0)    
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")    
url="https://nitdgp.ac.in/department/chemistry/faculty-5"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("h4",class_="card-title")
for i in data:
    name_list.append(i.text)
    designation_list.append(i.next_sibling.text)
data=soup.find_all("div",class_="card-body")
for i in data:
    aoi_list.append(i.p.text)    
data=soup.find_all("i",class_="fa fa-envelope")
for i in data:
    email_list.append(i.next_sibling.text)
email_list.pop(0)        
data=soup.find_all("i",class_="fa fa-phone")
for i in data:
    contact_list.append(i.next_sibling.text)  
contact_list.pop(0)  
name_list.pop(len(name_list)-1)
name_list.pop(len(name_list)-1)  
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")     
url="https://nitdgp.ac.in/department/electronics-and-communication-engineering/faculty-6"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("h4",class_="card-title")
for i in data:
    name_list.append(i.text)
    designation_list.append(i.next_sibling.text)
data=soup.find_all("div",class_="card-body")
for i in data:
    aoi_list.append(i.p.text)    
data=soup.find_all("i",class_="fa fa-envelope")
for i in data:
    email_list.append(i.next_sibling.text)
email_list.pop(0)        
data=soup.find_all("i",class_="fa fa-phone")
for i in data:
    contact_list.append(i.next_sibling.text)  
contact_list.pop(0)   
name_list.pop(len(name_list)-1)
name_list.pop(len(name_list)-1) 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")     
url="https://nitdgp.ac.in/department/electrical-engineering/faculty-7"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("h4",class_="card-title")
for i in data:
    name_list.append(i.text)
    designation_list.append(i.next_sibling.text)
data=soup.find_all("div",class_="card-body")
for i in data:
    aoi_list.append(i.p.text)    
data=soup.find_all("i",class_="fa fa-envelope")
for i in data:
    email_list.append(i.next_sibling.text)
email_list.pop(0)        
data=soup.find_all("i",class_="fa fa-phone")
for i in data:
    contact_list.append(i.next_sibling.text)  
contact_list.pop(0)  
name_list.pop(len(name_list)-1)
name_list.pop(len(name_list)-1)  
name_list.pop(len(name_list)-1)  
name_list.pop(len(name_list)-1)  
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")         
url="https://nitdgp.ac.in/department/mathematics/faculty-10"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("h4",class_="card-title")
for i in data:
    name_list.append(i.text)
    designation_list.append(i.next_sibling.text)
data=soup.find_all("div",class_="card-body")
for i in data:
    aoi_list.append(i.p.text)    
data=soup.find_all("i",class_="fa fa-envelope")
for i in data:
    email_list.append(i.next_sibling.text)
email_list.pop(0)        
data=soup.find_all("i",class_="fa fa-phone")
for i in data:
    contact_list.append(i.next_sibling.text)  
contact_list.pop(0)    
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")         
url="https://nitdgp.ac.in/department/mechanical-engineering/faculty-11"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("h4",class_="card-title")
for i in data:
    name_list.append(i.text)
    designation_list.append(i.next_sibling.text)
data=soup.find_all("div",class_="card-body")
for i in data:
    aoi_list.append(i.p.text)    
data=soup.find_all("i",class_="fa fa-envelope")
for i in data:
    email_list.append(i.next_sibling.text)
email_list.pop(0)        
data=soup.find_all("i",class_="fa fa-phone")
for i in data:
    contact_list.append(i.next_sibling.text)  
contact_list.pop(0)   
name_list.pop(len(name_list)-1)
name_list.pop(len(name_list)-1) 
name_list.pop(len(name_list)-1) 
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")      
url="https://nitdgp.ac.in/department/metallurgical-materials-engineering/faculty-12"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("h4",class_="card-title")
for i in data:
    name_list.append(i.text)
    designation_list.append(i.next_sibling.text)
data=soup.find_all("div",class_="card-body")
for i in data:
    aoi_list.append(i.p.text)    
data=soup.find_all("i",class_="fa fa-envelope")
for i in data:
    email_list.append(i.next_sibling.text)
email_list.pop(0)        
data=soup.find_all("i",class_="fa fa-phone")
for i in data:
    contact_list.append(i.next_sibling.text)  
contact_list.pop(0)    
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")         
url="https://nitdgp.ac.in/department/physics/faculty-14"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("h4",class_="card-title")
for i in data:
    name_list.append(i.text)
    designation_list.append(i.next_sibling.text)
data=soup.find_all("div",class_="card-body")
for i in data:
    aoi_list.append(i.p.text)    
data=soup.find_all("i",class_="fa fa-envelope")
for i in data:
    email_list.append(i.next_sibling.text)
email_list.pop(0)        
data=soup.find_all("i",class_="fa fa-phone")
for i in data:
    contact_list.append(i.next_sibling.text)  
contact_list.pop(0) 
name_list.pop(len(name_list)-1)
name_list.pop(len(name_list)-1)   
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")                         
url="https://www.nitj.ac.in/index.php/nitj_cinfo/FacultyList/5"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("table",class_="faculty-table")
for i in data:
    name_list.append(i.find_all("tr")[0].find_all("p")[0].font.text)
    designation_list.append(i.find_all("tr")[0].find_all("p")[0].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    email_list.append(i.find_all("tr")[0].find_all("td")[1].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    contact_list.append(i.find_all("tr")[0].find_all("td")[2].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    aoi_list.append(i.find_all("tr")[1].text.replace(u'\n',u''))
file=open("faculty.txt","a")
file.write("\n")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  
url="https://www.nitj.ac.in/index.php/nitj_cinfo/FacultyList/7"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("table",class_="faculty-table")
for i in data:
    name_list.append(i.find_all("tr")[0].find_all("p")[0].font.text)
    designation_list.append(i.find_all("tr")[0].find_all("p")[0].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    email_list.append(i.find_all("tr")[0].find_all("td")[1].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    contact_list.append(i.find_all("tr")[0].find_all("td")[2].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    aoi_list.append(i.find_all("tr")[1].text.replace(u'\n',u''))
file=open("faculty.txt","a")
file.write("\n")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  
url="https://www.nitj.ac.in/index.php/nitj_cinfo/FacultyList/6"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("table",class_="faculty-table")
for i in data:
    name_list.append(i.find_all("tr")[0].find_all("p")[0].font.text)
    designation_list.append(i.find_all("tr")[0].find_all("p")[0].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    email_list.append(i.find_all("tr")[0].find_all("td")[1].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    contact_list.append(i.find_all("tr")[0].find_all("td")[2].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    aoi_list.append(i.find_all("tr")[1].text.replace(u'\n',u''))
file=open("faculty.txt","a")
file.write("\n")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n") 
url="https://www.nitj.ac.in/index.php/nitj_cinfo/FacultyList/2"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("table",class_="faculty-table")
for i in data:
    name_list.append(i.find_all("tr")[0].find_all("p")[0].font.text)
    designation_list.append(i.find_all("tr")[0].find_all("p")[0].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    email_list.append(i.find_all("tr")[0].find_all("td")[1].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    contact_list.append(i.find_all("tr")[0].find_all("td")[2].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    aoi_list.append(i.find_all("tr")[1].text.replace(u'\n',u''))
name_list.pop(len(name_list)-1)
designation_list.pop(len(name_list)-1)
email_list.pop(len(name_list)-1)
contact_list.pop(len(name_list)-1)
# aoi_list.pop(len(name_list)-1)   
file=open("faculty.txt","a")
file.write("\n")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")            
url="https://www.nitj.ac.in/index.php/nitj_cinfo/FacultyList/13"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("table",class_="faculty-table")
for i in data:
    name_list.append(i.find_all("tr")[0].find_all("p")[0].font.text)
    designation_list.append(i.find_all("tr")[0].find_all("p")[0].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    email_list.append(i.find_all("tr")[0].find_all("td")[1].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    contact_list.append(i.find_all("tr")[0].find_all("td")[2].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    aoi_list.append(i.find_all("tr")[1].text.replace(u'\n',u''))
file=open("faculty.txt","a")
file.write("\n")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  
url="https://www.nitj.ac.in/index.php/nitj_cinfo/FacultyList/4"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("table",class_="faculty-table")
for i in data:
    name_list.append(i.find_all("tr")[0].find_all("p")[0].font.text)
    designation_list.append(i.find_all("tr")[0].find_all("p")[0].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    email_list.append(i.find_all("tr")[0].find_all("td")[1].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    contact_list.append(i.find_all("tr")[0].find_all("td")[2].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    aoi_list.append(i.find_all("tr")[1].text.replace(u'\n',u''))
file=open("faculty.txt","a")
file.write("\n")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  
url="https://www.nitj.ac.in/index.php/nitj_cinfo/FacultyList/10"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("table",class_="faculty-table")
for i in data:
    name_list.append(i.find_all("tr")[0].find_all("p")[0].font.text)
    designation_list.append(i.find_all("tr")[0].find_all("p")[0].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    email_list.append(i.find_all("tr")[0].find_all("td")[1].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    contact_list.append(i.find_all("tr")[0].find_all("td")[2].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    aoi_list.append(i.find_all("tr")[1].text.replace(u'\n',u''))
file=open("faculty.txt","a")
file.write("\n")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  
url="https://www.nitj.ac.in/index.php/nitj_cinfo/FacultyList/9"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("table",class_="faculty-table")
for i in data:
    name_list.append(i.find_all("tr")[0].find_all("p")[0].font.text)
    designation_list.append(i.find_all("tr")[0].find_all("p")[0].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    email_list.append(i.find_all("tr")[0].find_all("td")[1].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    contact_list.append(i.find_all("tr")[0].find_all("td")[2].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    aoi_list.append(i.find_all("tr")[1].text.replace(u'\n',u''))
file=open("faculty.txt","a")
file.write("\n")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n") 
url="https://www.nitj.ac.in/index.php/nitj_cinfo/FacultyList/1"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("table",class_="faculty-table")
for i in data:
    name_list.append(i.find_all("tr")[0].find_all("p")[0].font.text)
    designation_list.append(i.find_all("tr")[0].find_all("p")[0].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    email_list.append(i.find_all("tr")[0].find_all("td")[1].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    contact_list.append(i.find_all("tr")[0].find_all("td")[2].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    aoi_list.append(i.find_all("tr")[1].text.replace(u'\n',u''))
file=open("faculty.txt","a")
file.write("\n")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")   
url="https://www.nitj.ac.in/index.php/nitj_cinfo/FacultyList/3"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("table",class_="faculty-table")
for i in data:
    name_list.append(i.find_all("tr")[0].find_all("p")[0].font.text)
    designation_list.append(i.find_all("tr")[0].find_all("p")[0].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    email_list.append(i.find_all("tr")[0].find_all("td")[1].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    contact_list.append(i.find_all("tr")[0].find_all("td")[2].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    aoi_list.append(i.find_all("tr")[1].text.replace(u'\n',u''))
file=open("faculty.txt","a")
file.write("\n")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")   
url="https://www.nitj.ac.in/index.php/nitj_cinfo/FacultyList/8"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("table",class_="faculty-table")
for i in data:
    name_list.append(i.find_all("tr")[0].find_all("p")[0].font.text)
    designation_list.append(i.find_all("tr")[0].find_all("p")[0].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    email_list.append(i.find_all("tr")[0].find_all("td")[1].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    contact_list.append(i.find_all("tr")[0].find_all("td")[2].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    aoi_list.append(i.find_all("tr")[1].text.replace(u'\n',u''))
file=open("faculty.txt","a")
file.write("\n")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")   
url="https://www.nitj.ac.in/index.php/nitj_cinfo/FacultyList/12"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("table",class_="faculty-table")
for i in data:
    name_list.append(i.find_all("tr")[0].find_all("p")[0].font.text)
    designation_list.append(i.find_all("tr")[0].find_all("p")[0].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    email_list.append(i.find_all("tr")[0].find_all("td")[1].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    contact_list.append(i.find_all("tr")[0].find_all("td")[2].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    aoi_list.append(i.find_all("tr")[1].text.replace(u'\n',u''))
file=open("faculty.txt","a")
file.write("\n")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")   
url="https://www.nitj.ac.in/index.php/nitj_cinfo/FacultyList/15"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("table",class_="faculty-table")
for i in data:
    name_list.append(i.find_all("tr")[0].find_all("p")[0].font.text)
    designation_list.append(i.find_all("tr")[0].find_all("p")[0].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    email_list.append(i.find_all("tr")[0].find_all("td")[1].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    contact_list.append(i.find_all("tr")[0].find_all("td")[2].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    aoi_list.append(i.find_all("tr")[1].text.replace(u'\n',u''))
file=open("faculty.txt","a")
file.write("\n")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")   
url="https://www.nitj.ac.in/index.php/nitj_cinfo/FacultyList/16"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("table",class_="faculty-table")
for i in data:
    name_list.append(i.find_all("tr")[0].find_all("p")[0].font.text)
    designation_list.append(i.find_all("tr")[0].find_all("p")[0].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    email_list.append(i.find_all("tr")[0].find_all("td")[1].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    contact_list.append(i.find_all("tr")[0].find_all("td")[2].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    aoi_list.append(i.find_all("tr")[1].text.replace(u'\n',u''))
file=open("faculty.txt","a")
file.write("\n")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  
url="https://www.nitj.ac.in/index.php/nitj_cinfo/FacultyList/17"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("table",class_="faculty-table")
for i in data:
    name_list.append(i.find_all("tr")[0].find_all("p")[0].font.text)
    designation_list.append(i.find_all("tr")[0].find_all("p")[0].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    email_list.append(i.find_all("tr")[0].find_all("td")[1].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    contact_list.append(i.find_all("tr")[0].find_all("td")[2].font.next_sibling.next_sibling.text.replace(u'\n',u''))
    aoi_list.append(i.find_all("tr")[1].text.replace(u'\n',u''))
file=open("faculty.txt","a")
file.write("\n")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  

url="http://www.mnnit.ac.in/index.php/department/engineering/cm/cmfp"
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find("table",id="table46").text
file=open("faculty.txt","a")
file.write(data)
url="http://www.mnnit.ac.in/index.php/department/engineering/csed/csedfp"
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find("table").text
file=open("faculty.txt","a")
file.write(data)
url="http://www.mnnit.ac.in/index.php/department/engineering/am/appmecfp"
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find("table").text
file=open("faculty.txt","a")
file.write(data)
url="http://www.mnnit.ac.in/index.php/department/engineering/biotech/biotechfp"
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find("table").text
file=open("faculty.txt","a")
file.write(data)
url="http://www.mnnit.ac.in/index.php/department/engineering/ce/cefp"
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find("table").text
file=open("faculty.txt","a")
file.write(data)
url="http://www.mnnit.ac.in/index.php/department/engineering/ee/eefp"
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find("table").text
file=open("faculty.txt","a")
file.write(data)
url="http://www.mnnit.ac.in/index.php/department/engineering/ece/ecefp"
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find("table").text
file=open("faculty.txt","a")
file.write(data)
url="http://www.mnnit.ac.in/index.php/department/engineering/me/mefpa"
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find("table").text
file=open("faculty.txt","a")
file.write(data)
url="https://www.nitmz.ac.in/EMPBiodata.aspx"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("a",class_="linktext")
for i in data:
    name_list.append(i.text)
    designation_list.append(i.parent.parent.parent.find_all("tr")[1].text.replace(u'\n\r\n',u'').replace(u'\r\n',u'').replace(u'\n',u''))
    email_list.append(i.parent.parent.parent.find_all("tr")[2].text.replace(u'\n\n\n\n\r\n',u'').replace(u'\n\n\n\n',u'').replace(u'\r\n',u''))
    aoi_list.append(i.parent.parent.parent.find_all("tr")[4].text.replace(u'\n\n\n\n\r\n',u'').replace(u'\n\n\n\n',u'').replace(u'\r\n',u'').replace(u'\n',u''))
    contact_list.append("NOT AVAILABLE")  
file=open("faculty.txt","a")
file.write("\n")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write(email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write(aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  
url="https://nita.ac.in/Department/Department_FacultyList.aspx?nDeptID=caasa"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="fac-content")
for i in data:
    name_list.append(i.h3.text.replace(u'\n',u''))
    designation_list.append(i.find_all("p")[0].text)
    email_list.append(i.find_all("p")[2].text)
    contact_list.append("NOT AVAILABLE")
    aoi_list.append("NOT AVAILABLE")   
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")    
url="https://nita.ac.in/Department/Department_FacultyList.aspx?nDeptID=caaqq"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="fac-content")
for i in data:
    name_list.append(i.h3.text.replace(u'\n',u''))
    designation_list.append(i.find_all("p")[0].text)
    email_list.append(i.find_all("p")[2].text)
    contact_list.append("NOT AVAILABLE")
    aoi_list.append("NOT AVAILABLE")   
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  
url="https://nita.ac.in/Department/Department_FacultyList.aspx?nDeptID=caaqs"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="fac-content")
for i in data:
    name_list.append(i.h3.text.replace(u'\n',u''))
    designation_list.append(i.find_all("p")[0].text)
    email_list.append(i.find_all("p")[2].text)
    contact_list.append("NOT AVAILABLE")
    aoi_list.append("NOT AVAILABLE")   
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")
url="https://nita.ac.in/Department/Department_FacultyList.aspx?nDeptID=caaqm"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="fac-content")
for i in data:
    name_list.append(i.h3.text.replace(u'\n',u''))
    designation_list.append(i.find_all("p")[0].text)
    email_list.append(i.find_all("p")[2].text)
    contact_list.append("NOT AVAILABLE")
    aoi_list.append("NOT AVAILABLE")   
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  
url="https://nita.ac.in/Department/Department_FacultyList.aspx?nDeptID=caasc"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="fac-content")
for i in data:
    name_list.append(i.h3.text.replace(u'\n',u''))
    designation_list.append(i.find_all("p")[0].text)
    email_list.append(i.find_all("p")[2].text)
    contact_list.append("NOT AVAILABLE")
    aoi_list.append("NOT AVAILABLE")   
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  
url="https://nita.ac.in/Department/Department_FacultyList.aspx?nDeptID=caase"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="fac-content")
for i in data:
    name_list.append(i.h3.text.replace(u'\n',u''))
    designation_list.append(i.find_all("p")[0].text)
    email_list.append(i.find_all("p")[2].text)
    contact_list.append("NOT AVAILABLE")
    aoi_list.append("NOT AVAILABLE")   
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  
url="https://nita.ac.in/Department/Department_FacultyList.aspx?nDeptID=caasg"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="fac-content")
for i in data:
    name_list.append(i.h3.text.replace(u'\n',u''))
    designation_list.append(i.find_all("p")[0].text)
    email_list.append(i.find_all("p")[2].text)
    contact_list.append("NOT AVAILABLE")
    aoi_list.append("NOT AVAILABLE")   
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  
url="https://nita.ac.in/Department/Department_FacultyList.aspx?nDeptID=caasi"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="fac-content")
for i in data:
    name_list.append(i.h3.text.replace(u'\n',u''))
    designation_list.append(i.find_all("p")[0].text)
    email_list.append(i.find_all("p")[2].text)
    contact_list.append("NOT AVAILABLE")
    aoi_list.append("NOT AVAILABLE")   
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")
url="https://nita.ac.in/Department/Department_FacultyList.aspx?nDeptID=caaqo"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="fac-content")
for i in data:
    name_list.append(i.h3.text.replace(u'\n',u''))
    designation_list.append(i.find_all("p")[0].text)
    email_list.append(i.find_all("p")[2].text)
    contact_list.append("NOT AVAILABLE")
    aoi_list.append("NOT AVAILABLE")   
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")
url="https://nita.ac.in/Department/Department_FacultyList.aspx?nDeptID=caask"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="fac-content")
for i in data:
    name_list.append(i.h3.text.replace(u'\n',u''))
    designation_list.append(i.find_all("p")[0].text)
    email_list.append(i.find_all("p")[2].text)
    contact_list.append("NOT AVAILABLE")
    aoi_list.append("NOT AVAILABLE")   
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")    
url="https://nita.ac.in/Department/Department_FacultyList.aspx?nDeptID=caasm"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="fac-content")
for i in data:
    name_list.append(i.h3.text.replace(u'\n',u''))
    designation_list.append(i.find_all("p")[0].text)
    email_list.append(i.find_all("p")[2].text)
    contact_list.append("NOT AVAILABLE")
    aoi_list.append("NOT AVAILABLE")   
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")    
url="https://nita.ac.in/Department/Department_FacultyList.aspx?nDeptID=caaso"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="fac-content")
for i in data:
    name_list.append(i.h3.text.replace(u'\n',u''))
    designation_list.append(i.find_all("p")[0].text)
    email_list.append(i.find_all("p")[2].text)
    contact_list.append("NOT AVAILABLE")
    aoi_list.append("NOT AVAILABLE")   
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")    
url="https://nita.ac.in/Department/Department_FacultyList.aspx?nDeptID=caasq"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
data=soup.find_all("div",class_="fac-content")
for i in data:
    name_list.append(i.h3.text.replace(u'\n',u''))
    designation_list.append(i.find_all("p")[0].text)
    email_list.append(i.find_all("p")[2].text)
    contact_list.append("NOT AVAILABLE")
    aoi_list.append("NOT AVAILABLE")   
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")    
url="https://chemistry.nitsikkim.ac.in/people.php"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup)
fac=soup.find("div",id='faculty')
data =fac.find_all('a',class_='card-link')
card_list=[]
for i in data:
    card_list.append(i.get("href"))
for i in range(len(card_list)):
    url="https://chemistry.nitsikkim.ac.in/"+card_list[i]
    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent,'html.parser')
    name_list.append(soup.find("h1",class_="entry-title title-foc-md").text.replace(u'\n\t\t\t\t\t\t\t\t',u''))
    designation_list.append(soup.find("h5",class_="text-foc-md").text)
    email_list.append(soup.find("p",class_="text-foc-md").a.text.replace(u'\n',u'').replace(u'\t\t\t\t\t\t\t\t',u''))
    contact_list.append(soup.find("p",class_="text-foc-md").find_all("a")[1].text.replace(u'\r\n',u''))
    aoi_list.append(soup.find("article",class_="profile-glimps").find_all("p")[1].text.replace(u'\t\t\t\t\t\t\t',u'').replace(u'\r\n\t\t\t\t\t\t\t',u'').replace(u'\r\n',u'').replace(u'\n',u''))
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")    
url="https://physics.nitsikkim.ac.in/people.php"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup)
fac=soup.find("div",id='faculty')
data =fac.find_all('a',class_='card-link')
card_list=[]
for i in data:
    card_list.append(i.get("href"))
for i in range(len(card_list)):
    url="https://physics.nitsikkim.ac.in/"+card_list[i]
    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent,'html.parser')
    name_list.append(soup.find("h1",class_="entry-title title-foc-md").text.replace(u'\n\t\t\t\t\t\t\t\t',u''))
    designation_list.append(soup.find("h5",class_="text-foc-md").text)
    email_list.append(soup.find("p",class_="text-foc-md").a.text.replace(u'\n',u'').replace(u'\t\t\t\t\t\t\t\t',u''))
    contact_list.append(soup.find("p",class_="text-foc-md").find_all("a")[1].text.replace(u'\r\n',u''))
    aoi_list.append(soup.find("article",class_="profile-glimps").find_all("p")[1].text.replace(u'\t\t\t\t\t\t\t',u'').replace(u'\r\n\t\t\t\t\t\t\t',u'').replace(u'\r\n',u'').replace(u'\n',u''))
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n") 
url="https://cse.nitsikkim.ac.in/people.php"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup)
fac=soup.find("div",id='faculty')
data =fac.find_all('a',class_='card-link')
card_list=[]
for i in data:
    card_list.append(i.get("href"))
for i in range(len(card_list)):
    url="https://cse.nitsikkim.ac.in/"+card_list[i]
    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent,'html.parser')
    name_list.append(soup.find("h1",class_="entry-title title-foc-md").text.replace(u'\n\t\t\t\t\t\t\t\t',u''))
    designation_list.append(soup.find("h5",class_="text-foc-md").text)
    email_list.append(soup.find("p",class_="text-foc-md").a.text.replace(u'\n',u'').replace(u'\t\t\t\t\t\t\t\t',u''))
    contact_list.append(soup.find("p",class_="text-foc-md").find_all("a")[1].text.replace(u'\r\n',u''))
    aoi_list.append(soup.find("article",class_="profile-glimps").find_all("p")[1].text.replace(u'\t\t\t\t\t\t\t',u'').replace(u'\r\n\t\t\t\t\t\t\t',u'').replace(u'\r\n',u'').replace(u'\n',u''))
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")  
url="https://ce.nitsikkim.ac.in/people.php"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup)
fac=soup.find("div",id='faculty')
data =fac.find_all('a',class_='card-link')
card_list=[]
for i in data:
    card_list.append(i.get("href"))
for i in range(len(card_list)):
    url="https://ce.nitsikkim.ac.in/"+card_list[i]
    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent,'html.parser')
    name_list.append(soup.find("h1",class_="entry-title title-foc-md").text.replace(u'\n\t\t\t\t\t\t\t\t',u''))
    designation_list.append(soup.find("h5",class_="text-foc-md").text)
    email_list.append(soup.find("p",class_="text-foc-md").a.text.replace(u'\n',u'').replace(u'\t\t\t\t\t\t\t\t',u''))
    contact_list.append(soup.find("p",class_="text-foc-md").find_all("a")[1].text.replace(u'\r\n',u''))
    aoi_list.append(soup.find("article",class_="profile-glimps").find_all("p")[1].text.replace(u'\t\t\t\t\t\t\t',u'').replace(u'\r\n\t\t\t\t\t\t\t',u'').replace(u'\r\n',u'').replace(u'\n',u''))
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")    
url="https://eee.nitsikkim.ac.in/people.php"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup)
fac=soup.find("div",id='faculty')
data =fac.find_all('a',class_='card-link')
card_list=[]
for i in data:
    card_list.append(i.get("href"))
for i in range(len(card_list)):
    url="https://eee.nitsikkim.ac.in/"+card_list[i]
    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent,'html.parser')
    name_list.append(soup.find("h1",class_="entry-title title-foc-md").text.replace(u'\n\t\t\t\t\t\t\t\t',u''))
    designation_list.append(soup.find("h5",class_="text-foc-md").text)
    email_list.append(soup.find("p",class_="text-foc-md").a.text.replace(u'\n',u'').replace(u'\t\t\t\t\t\t\t\t',u''))
    contact_list.append(soup.find("p",class_="text-foc-md").find_all("a")[1].text.replace(u'\r\n',u''))
    aoi_list.append(soup.find("article",class_="profile-glimps").find_all("p")[1].text.replace(u'\t\t\t\t\t\t\t',u'').replace(u'\r\n\t\t\t\t\t\t\t',u'').replace(u'\r\n',u'').replace(u'\n',u''))
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")    
url="https://ece.nitsikkim.ac.in/people.php"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup)
fac=soup.find("div",id='faculty')
data =fac.find_all('a',class_='card-link')
card_list=[]
for i in data:
    card_list.append(i.get("href"))
for i in range(len(card_list)):
    url="https://ece.nitsikkim.ac.in/"+card_list[i]
    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent,'html.parser')
    name_list.append(soup.find("h1",class_="entry-title title-foc-md").text.replace(u'\n\t\t\t\t\t\t\t\t',u''))
    designation_list.append(soup.find("h5",class_="text-foc-md").text)
    email_list.append(soup.find("p",class_="text-foc-md").a.text.replace(u'\n',u'').replace(u'\t\t\t\t\t\t\t\t',u''))
    contact_list.append(soup.find("p",class_="text-foc-md").find_all("a")[1].text.replace(u'\r\n',u''))
    aoi_list.append(soup.find("article",class_="profile-glimps").find_all("p")[1].text.replace(u'\t\t\t\t\t\t\t',u'').replace(u'\r\n\t\t\t\t\t\t\t',u'').replace(u'\r\n',u'').replace(u'\n',u''))
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")    
url="https://me.nitsikkim.ac.in/people.php"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup)
fac=soup.find("div",id='faculty')
data =fac.find_all('a',class_='card-link')
card_list=[]
for i in data:
    card_list.append(i.get("href"))
for i in range(len(card_list)):
    url="https://me.nitsikkim.ac.in/"+card_list[i]
    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent,'html.parser')
    name_list.append(soup.find("h1",class_="entry-title title-foc-md").text.replace(u'\n\t\t\t\t\t\t\t\t',u''))
    designation_list.append(soup.find("h5",class_="text-foc-md").text)
    email_list.append(soup.find("p",class_="text-foc-md").a.text.replace(u'\n',u'').replace(u'\t\t\t\t\t\t\t\t',u''))
    contact_list.append(soup.find("p",class_="text-foc-md").find_all("a")[1].text.replace(u'\r\n',u''))
    aoi_list.append(soup.find("article",class_="profile-glimps").find_all("p")[1].text.replace(u'\t\t\t\t\t\t\t',u'').replace(u'\r\n\t\t\t\t\t\t\t',u'').replace(u'\r\n',u'').replace(u'\n',u''))
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")    
url="https://math.nitsikkim.ac.in/people.php"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup)
fac=soup.find("div",id='faculty')
data =fac.find_all('a',class_='card-link')
card_list=[]
for i in data:
    card_list.append(i.get("href"))
for i in range(len(card_list)):
    url="https://math.nitsikkim.ac.in/"+card_list[i]
    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent,'html.parser')
    name_list.append(soup.find("h1",class_="entry-title title-foc-md").text.replace(u'\n\t\t\t\t\t\t\t\t',u''))
    designation_list.append(soup.find("h5",class_="text-foc-md").text)
    email_list.append(soup.find("p",class_="text-foc-md").a.text.replace(u'\n',u'').replace(u'\t\t\t\t\t\t\t\t',u''))
    contact_list.append(soup.find("p",class_="text-foc-md").find_all("a")[1].text.replace(u'\r\n',u''))
    aoi_list.append(soup.find("article",class_="profile-glimps").find_all("p")[1].text.replace(u'\t\t\t\t\t\t\t',u'').replace(u'\r\n\t\t\t\t\t\t\t',u'').replace(u'\r\n',u'').replace(u'\n',u''))
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")    
url="https://hss.nitsikkim.ac.in/people.php"
name_list=[]
designation_list=[]
email_list=[]
contact_list=[]
aoi_list=[]
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup)
fac=soup.find("div",id='faculty')
data =fac.find_all('a',class_='card-link')
card_list=[]
for i in data:
    card_list.append(i.get("href"))
for i in range(len(card_list)):
    url="https://hss.nitsikkim.ac.in/"+card_list[i]
    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent,'html.parser')
    name_list.append(soup.find("h1",class_="entry-title title-foc-md").text.replace(u'\n\t\t\t\t\t\t\t\t',u''))
    designation_list.append(soup.find("h5",class_="text-foc-md").text)
    email_list.append(soup.find("p",class_="text-foc-md").a.text.replace(u'\n',u'').replace(u'\t\t\t\t\t\t\t\t',u''))
    contact_list.append(soup.find("p",class_="text-foc-md").find_all("a")[1].text.replace(u'\r\n',u''))
    aoi_list.append(soup.find("article",class_="profile-glimps").find_all("p")[1].text.replace(u'\t\t\t\t\t\t\t',u'').replace(u'\r\n\t\t\t\t\t\t\t',u'').replace(u'\r\n',u'').replace(u'\n',u''))
file=open("faculty.txt","a")
for i in range(len(name_list)):
    file.write("Name:"+name_list[i])
    file.write("\n")
    file.write("Designation:"+designation_list[i])
    file.write("\n")
    file.write("email_list:"+email_list[i])
    file.write("\n")
    file.write("Phone:"+contact_list[i])
    file.write("\n")
    file.write("Area of Interest:"+aoi_list[i])
    file.write("\n")
    file.write("------------------------------------------****------------------------------------------")
    file.write("\n")   






