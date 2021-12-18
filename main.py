import getdata
import sendmessage
import datafilter
import time
#_____________________________________________________
api_key="d4e19d4e-eef3-48da-aea8-6bb8c9826532"
bot_token=''
chat_id= ''
loai_tien_ao=input("Nhap loai tien ao: ")  #Bitcoin: 0
loai_tien_te=input("Nhap loai tien te: ").upper()  #VND or USD
gia_canhbao=float(input("Nhap gia nguy hiem can canh bao ngay: "))
X=int(input("Nhap thoi gian giua hai lan thong bao (phut): "))*60
N=1    #So moc tien trong x phut
#______________________________________________________
end=False
while end==False:
   reponse_json=getdata.GetData(api_key,loai_tien_ao,loai_tien_te)
   gia_thoigian=datafilter.Data_Filter(reponse_json,loai_tien_ao)
   ds.append(gia_thoigian)
   if gia_thoigian[0] <= gia_canhbao:
       sendmessage.SendMessage(ds,bot_token,chat_id)
   if len(ds)>=N:
       sendmessage.SendMessage(ds,bot_token,chat_id)
       ds=[]
   time.sleep(X/N)