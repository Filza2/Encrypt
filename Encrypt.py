from hashlib import *
import py_compile
gr="\033[1;32m";po='\033[1;38m'
print(f"""
███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   
            
{po}               By @TweakPY - @vv1ck

{gr}- {po}1*[Encrypt md5]
{gr}- {po}2*[Encrypt sha3_512]
{gr}- {po}3*[Encrypt sha256]
{gr}- {po}4*[Encrypt sha384]
{gr}- {po}5*[Encrypt sha1]
{gr}- {po}6*[Encrypt sha512]
{gr}- {po}7*[Encrypt sha224]
{gr}- {po}8*[Encrypt sha3_384]
{gr}- {po}9*[Encrypt sha1]
{gr}- {po}10*[Encrypt Files]\n""")
mod=int(input("[?] Enter The Number : "))
if mod==1:encrypted_text=md5(input("[?] Enter Text : ").encode()).hexdigest();print("[+] The Encrypted Text is : ",encrypted_text)
elif mod==2:encrypted_text=sha3_512(input("[?] Enter Text : ").encode()).hexdigest();print("[+] The Encrypted Text is : ",encrypted_text)
elif mod==3:encrypted_text=sha256(input("[?] Enter Text : ").encode()).hexdigest();print("[+] The Encrypted Text is : ",encrypted_text)
elif mod==4:encrypted_text=sha384(input("[?] Enter Text : ").encode()).hexdigest();print("[+] The Encrypted Text is : ",encrypted_text)
elif mod==5:encrypted_text=sha1(input("[?] Enter Text : ").encode()).hexdigest();print("[+] The Encrypted Text is : ",encrypted_text)
elif mod==6:encrypted_text=sha512(input("[?] Enter Text : ").encode()).hexdigest();print("[+] The Encrypted Text is : ",encrypted_text)
elif mod==7:encrypted_text=sha224(input("[?] Enter Text : ").encode()).hexdigest();print("[+] The Encrypted Text is : ",encrypted_text)
elif mod==8:encrypted_text=sha3_384(input("[?] Enter Text : ").encode()).hexdigest();print("[+] The Encrypted Text is : ",encrypted_text)
elif mod==9:encrypted_text=sha1(input("[?] Enter Text : ").encode()).hexdigest();print("[+] The Encrypted Text is : ",encrypted_text)
elif mod==10:py_compile.compile(input('[?] Enter File Name : '));print('[+] Encryption successful ..')


