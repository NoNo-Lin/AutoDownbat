import os
import getpass
import shutil
from smb.SMBConnection import SMBConnection

#�ˬd�q���ϥΪ�
def username():
    wuser = getpass.getuser()
    return wuser

#�ˬd���|�W����Ƨ��A�S���N�s�W
def judgefile(lpath):
    if not os.path.isdir(lpath):
        os.mkdir(lpath)

#�s�u�ܺ����W����
def linksmb (suser,spass,lcn,rcn,rip):
    conn = SMBConnection(suser,spass,lcn,rcn,use_ntlm_v2 = True,is_direct_tcp = True)
    conn.connect(rip, 445)
    return conn

#�U���ɮ�
def downremotedate(conn,rsl,rfl,lfl):
    lfl = lfl+"\\"
    for f in conn.listPath(rsl,rfl):
        fname = f.filename
        if "." != fname and ".." != fname:
            rrfl = rfl+'\\'+fname
            llfl = lfl+"\\"+fname
            with open(llfl,'wb') as f:
                conn.retrieveFile(rsl,rrfl, f)

#��ؿ������ɮסA���槹���R���C
def usefile(lfl):
    for i in os.listdir(lfl):
        okpaht = '"'+lfl+"\\"+i+'"'
        os.system(okpaht)
    shutil.rmtree(lfl)