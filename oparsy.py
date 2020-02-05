import optparse

if __name__ == "__main__":
	parser = optparse.OptionParser("usage : %prog [options] arg1 arg2")
	parser.add_option("-H","--host",dest="hostname",default="127.0.0.1",type="string",help="specify hostname to run on")
	parser.add_option("-p","--port",dest="port",default="8080",type="string",help="enter the port")  
	(option,args) = parser.parse_args() 
	
	#if len(args) != 2:   
	#	parser.error("incorrect number of arguments") 
	hostname = option.hostname  
	port = option.port 
	print("these are the values entered") 
	print("HOSTNAME :: %6s" %(hostname))  
	print("PORT :: %2s" %(port))


