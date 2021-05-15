import requests
import m3u8

url="https://r1---sn-ja5nnpjuxji-cpge.googlevideo.com/videoplayback?expire=1604248861&ei=vZCeX7KkFsyavwTr4qygDw&ip=2407%3A5200%3A300%3A1291%3A25ff%3Aa4c1%3Ab1d6%3A4f54&id=o-ABcnUH7C5o83mzfG03QGappeiHpctI_jMElDZWpPmlkR&itag=247&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278&source=youtube&requiressl=yes&mh=qG&mm=31%2C29&mn=sn-ja5nnpjuxji-cpge%2Csn-bvvbax-3uhe&ms=au%2Crdu&mv=m&mvi=1&pcm2cms=yes&pl=48&nh=%2CEAI&initcwndbps=577500&vprv=1&mime=video%2Fwebm&gir=yes&clen=59034486&dur=1653.500&lmt=1553254557775655&mt=1604227116&fvip=5&keepalive=yes&c=WEB&txp=5431432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAIgI9fOncXBFeQ-Tyrw6y_6TH61qNudi_MS67xd0Sx2JAiB8zg6bIBVCgcMc1KagHv-N-a67GtJkbExrHFU-a73Vmg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cnh%2Cinitcwndbps&lsig=AG3C_xAwRgIhAKHNGqico25FqKYEnBVZ4acJPgzEnDbpQxRPPIbBP43vAiEAsk9wERXpULq13zjWIVxM4cQC0b2WyRI5vvug-gZMy78%3D&alr=yes&cpn=GT6f0mSWrOEAcrOC&cver=2.20201030.01.00&range=38048386-39684914&rn=20&rbuf=33730"

r=requests.get(url);
print(type(r.content))

with open("tmp.mp4",'wb') as f:
    f.write((r.content))