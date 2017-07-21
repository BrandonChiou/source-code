from Bio import SeqIO
import os
from optparse import OptionParser
import sys
#Options
shellparser = OptionParser()
shellparser.add_option("-i", "--input", action="store", dest="seqfile", default=0, help="input a fasta file. A example in the file.")
shellparser.add_option("-d", "--database", action="store", dest="database", default=0, help="select a database swissprot, uni90, uni50, pfam")
shellparser.add_option("-n", "--num_threads", action="store", type="int", dest="thread", default=1, help="set threads(cpu) number")
shellparser.add_option("-e", "--evalue", action="store", type="float", dest="evalue", default="0.001", help="set an evalue number")
shellparser.add_option("-s", "--start", action="store", type="int", dest="start", default=1, help="input a start position")
shellparser.add_option("-b", "--bottom", action="store", type="int", dest="end", default=100, help="input a end position")




(options, args) = shellparser.parse_args()
filename = options.seqfile
start = int(options.start)
end = int(options.end)
database = options.database
thread = int(options.thread)
evalue = float(options.evalue)
'''
Example: In Linux
>>python3 exec_psi.py -i 3files_test -d swissprot -n 10 -e 0.001 -s 0 -b 10

It will generate a temporary fasta input file which will change every time when read
and a executable shell file which will run in the psi-blast docker container contain commands of psi-blast.

psi-blast commands:
	"psiblast -num_iterations 3 -db /db/{} -query fasta.fasta -evalue 0.001 -num_threads {} -out_ascii_pssm {}.pssm"
                                        ^	                                             ^                  ^
	                                    changeable                                       changeable        change every read
'''
if (options.seqfile == 0 or options.database == 0):
	print ("  The input file or database is not selected!! Please use -i or -d option")
	sys.exit(" For more information, use -h or --help ")
elif (options.seqfile == 0 and options.database == 0):
	print (" The input file and database are not selected!! Please use -i and -d option")
	sys.exit(" For more information, use -h or --help ")
else:
	file_no = 1
	for line in SeqIO.parse(filename,"fasta"):
		split_id = line.id.split("|")
		name = str(file_no)+'_'+str(split_id[1])
		if file_no < start:
			file_no += 1
			continue
		elif file_no > end:
		
			break
		else:
			#add /home/pso/blast
			out = open("/home/pso/blast/fasta.fasta","w")
			out.write(">"+line.id+"\n"+str(line.seq)+"\n")
			out.close()
			
			inscr = "psiblast -num_iterations 3 -db /db/{database} -query fasta.fasta -evalue {ev} \
-num_threads {thread} -out_ascii_pssm {num}.pssm".format(database = "database", ev = evalue, thread = thread, num = "name")
		
			#add /home/pso/blast
			script = open("/home/pso/blast/script.sh","w")
			script.write(inscr)
			script.close()
		
			#replace print to os.system
			os.system("docker run --rm -v /home/pso/blast:/blast -v /home/pso/db:/db -w /blast ncbiblast sh script.sh")

			file_no += 1
		continue





	

