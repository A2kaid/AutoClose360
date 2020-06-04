import pyautogui
import os
import psutil

#保护措施，避免失控
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

def exit_15_360():
    #在当前屏幕中查找指定图片(图片需要由系统截图功能截取的图)
    x,y = pyautogui.locateCenterOnScreen('360.png') 
    #右击该坐标点
    pyautogui.rightClick(x,y)   
    x,y = pyautogui.locateCenterOnScreen('exit.png')
    pyautogui.click(x,y)    
    x,y = pyautogui.locateCenterOnScreen('down.png')
    pyautogui.click(x,y)    
    x,y = pyautogui.locateCenterOnScreen('minutes.png')
    pyautogui.click(x,y)    
    x,y = pyautogui.locateCenterOnScreen('click.png')
    pyautogui.click(x,y)

def exit_360():
    try:
        x,y = pyautogui.locateCenterOnScreen('360.png') 
        pyautogui.rightClick(x,y)   
        x,y = pyautogui.locateCenterOnScreen('exit.png')
        pyautogui.click(x,y)
        x,y = pyautogui.locateCenterOnScreen('next.png')
        pyautogui.click(x,y)
    except:
        x,y = pyautogui.locateCenterOnScreen('up.png') 
        pyautogui.click(x,y)  
        x,y = pyautogui.locateCenterOnScreen('360.png') 
        pyautogui.rightClick(x,y)  
        x,y = pyautogui.locateCenterOnScreen('exit.png')
        pyautogui.click(x,y)
        x,y = pyautogui.locateCenterOnScreen('next.png')
        pyautogui.click(x,y)

def uninstall():
    pids = psutil.pids()
    for pid in pids:
        if '360Tray.exe' == psutil.Process(pid).name():
            _path = psutil.Process(pid).exe().replace("safemon\\360Tray.exe",'')

    os.startfile(_path)
    pyautogui.click()
    x,y = pyautogui.locateCenterOnScreen('c.png')
    pyautogui.doubleClick(x,y)
    pyautogui.scroll(-1000)
    pyautogui.scroll(-1000)
    pyautogui.scroll(-1000)
    pyautogui.scroll(-1000)
    x,y = pyautogui.locateCenterOnScreen('uninstall.png')
    pyautogui.doubleClick(x,y)
    x,y = pyautogui.locateCenterOnScreen('yes.png')
    pyautogui.click(x,y)
    x,y = pyautogui.locateCenterOnScreen('yes.png')
    pyautogui.click(x,y)
    x,y = pyautogui.locateCenterOnScreen('ok.png')
    pyautogui.click(x,y)

if __name__ == "__main__":
    exit_360()
    uninstall()

