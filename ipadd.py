class ipadd():

      def __init__(self,ip):
          
          self.ip = ip

ip_add = ipadd(ip = [0xc0,0xa8,0x1,0x1])

print(ip_add.ip)          
