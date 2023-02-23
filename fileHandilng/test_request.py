import requests
 
url = 'https://doc-0g-7s-docs.googleusercontent.com/docs/securesc/gu7fim8g9hc82lbe7jugdq9q8rfet873/417jcvkoh8pc7ibbviv7fh56ikrt6c7k/1563912000000/15659024415184981874/11595594188083368607/1TPrz5QKd8DHHt1k8SRtm6tMiPjz_Qene?e=download&nonce=bsb79qdcnuhl8&user=11595594188083368607&hash=shn0lu5tium0m2ihso4lhluj24m8f5jf'
 
myfile = requests.get(url)
 
open('/content/ESRGAN/models/RRDB_ESRGAN_x4.pth', 'wb').write(myfile.content)