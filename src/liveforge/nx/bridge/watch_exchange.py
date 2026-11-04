import time
import NXOpen

def main():
    session = NXOpen.Session.GetSession()
    lw = session.ListingWindow
    lw.Open()
    lw.WriteLine("NX12 LiveForge Watcher 启动...")
    # 这里只是骨架，真正跑的时候会去读文件
    
if __name__ == "__main__":
    main()
