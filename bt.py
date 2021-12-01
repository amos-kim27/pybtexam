import asyncio # 비동기화 모듈
from bleak import BleakScanner # BLE 검색 모듈

class BT(object):
    
    def __init__(self):
        # 검색 클래스 생성
        self.scanner = BleakScanner()
        # 콜백 함수 등록
        self.scanner.register_detection_callback(detection_callback)
        print("init()")
    async def scan(self, list):
        # 검색 시작
        await self.scanner.start()
        # 5초간 대기 이때 검색된 장치들이 있다면 등록된 콜백함수가 호출된다.
        await asyncio.sleep(5.0)
        # 검색 중지
        await self.scanner.stop()
        devices = await self.scanner.get_discovered_devices()
        list.clear()
        for d in devices:
            if len(d.name) > 1 :
                str1 = d.address, d.name
                list.append(str1) 


def detection_callback(device, advertisement_data):
    tmmp = 0
    # 장치 주소와 신호세기, 그리고 어드버타이징 데이터를 출력한다.
#    if len(device.name) > 1 :
#        print("[",device.name, "]",device.address, "RSSI:", device.rssi, advertisement_data)
        

async def run( ar):
    print("run()")
    # 검색 클래스 생성
    scanner = BleakScanner()
    # 콜백 함수 등록
    scanner.register_detection_callback(detection_callback)
    # 검색 시작
    await scanner.start()
    # 5초간 대기 이때 검색된 장치들이 있다면 등록된 콜백함수가 호출된다.
    await asyncio.sleep(5.0)
    # 검색 중지
    await scanner.stop()
    # 지금까지 찾은 장치들 가져오기
    devices = await scanner.get_discovered_devices()
    # 지금까지 찾은 장치 리스트 출력
  
    for d in devices:
        if len(d.name) > 1 :
            str1 = d.address, d.name
            ar.append(str1) 
        #print(d)       
