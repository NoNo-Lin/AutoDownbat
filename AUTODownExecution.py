import os
import getpass
import shutil
from smb.SMBConnection import SMBConnection

#檢查電腦使用者
def username():
    wuser = getpass.getuser()
    return wuser

#檢查路徑上的資料夾，沒有就新增
def judgefile(lpath):
    if not os.path.isdir(lpath):
        os.mkdir(lpath)

#連線至網路上芳齡
def linksmb (suser,spass,lcn,rcn,rip):
    conn = SMBConnection(suser,spass,lcn,rcn,use_ntlm_v2 = True,is_direct_tcp = True)
    conn.connect(rip, 445)
    return conn

#下載檔案
def downremotedate(conn,rsl,rfl,lfl):
    lfl = lfl+"\\"
    for f in conn.listPath(rsl,rfl):
        fname = f.filename
        if "." != fname and ".." != fname:
            rrfl = rfl+'\\'+fname
            llfl = lfl+"\\"+fname
            with open(llfl,'wb') as f:
                conn.retrieveFile(rsl,rrfl, f)

#到目錄執行檔案，執行完畢刪除。
def usefile(lfl):
    for i in os.listdir(lfl):
        okpaht = '"'+lfl+"\\"+i+'"'
        os.system(okpaht)
    shutil.rmtree(lfl)