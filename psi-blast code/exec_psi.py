

from Bio import SeqIO
import os
from optparse import OptionParser

#Options
shellparser = OptionParser()
shellparser.add_option("-i", "--input", action="store", dest="seqfile", help="input a fasta file")
shellparser.add_option("-s", "--start", action="store", type="int", dest="start", default=1, help="input a start position")
shellparser.add_option("-e", "--end", action="store", type="int", dest="end", default=100, help="input a end position")

(options, args) = shellparser.parse_args()
filename = options.seqfile
start = int(options.start)
end = int(options.end)
'''
Example: In Linux
>>python3 exec_psi.py -i input.fasta -s 1 -e 100

It will generate a temporary fasta input file which will change every time when read
and a executable shell file which will run in the psi-blast docker container contain commands of psi-blast.

psi-blast commands:
	"psiblast -num_iterations 3 -db /db/swissprot\
	-query fasta.fasta -evalue 0.001 -num_threads\
	1 -out_ascii_pssm {}.pssm".format
	
'''
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
		
		inscr = "psiblast -num_iterations 3 -db /db/swissprot -query fasta.fasta -evalue 0.001 -num_threads 1 -out_ascii_pssm {}.pssm".format(name)
		#add /home/pso/blast
		script = open("/home/pso/blast/script.sh","w")
		script.write(inscr)
		script.close()
		
		#replace print to os.system
		os.system("docker run --rm -v /home/pso/blast:/blast -v /home/pso/db:/db -w /blast ncbiblast sh script.sh")

		file_no += 1
	continue





	

