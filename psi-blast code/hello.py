import sys

def main():
	if len(sys.argv) < 2:
		print "Usage", sys.argv[0], "<WHO>"
		sys.exit(0)
		
	who = sys.argv[1]
	print "Hello, %s" % who
	
if __name__ == "__main__":
	main()