#!/usr/bin/python

f1 = open('cass_master.csv', 'r');
f2 = open('cass_slave1.csv', 'r');
f3 = open('cass_slave2.csv', 'r');
f4 = open('cass_slave3.csv', 'r');
f5 = open('cass_slave4.csv', 'r');
output = open('cassandra-memory.csv','w');

newLine = 'timestamp, memory[node1]:1'
newLine += ', memory[node2]:1';
newLine += ', memory[node3]:1';
newLine += ', memory[node4]:1';
newLine += ', memory[node5]:1\n';
output.write(newLine)
count = 0;
for line1 in f1:
	line1 = line1.strip('\n').split(',');
	line2 = f2.readline().strip('\n').split(',');
	line3 = f3.readline().strip('\n').split(',');
	line4 = f4.readline().strip('\n').split(',');
	line5 = f5.readline().strip('\n').split(',');

	if count > 0:	
		newLine = line1[0] + ',' + line1[2];
		newLine += ',' + line2[2];
        	newLine += ',' + line3[2];
       		newLine += ',' + line4[2];
        	newLine += ',' + line5[2] + '\n';
		output.write(newLine)
	count += 1
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
output.close()
