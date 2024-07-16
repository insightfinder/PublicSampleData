#!/usr/bin/python

f1 = open('cass_master.csv', 'r');
f2 = open('cass_slave1.csv', 'r');
f3 = open('cass_slave2.csv', 'r');
f4 = open('cass_slave3.csv', 'r');
f5 = open('cass_slave4.csv', 'r');
output = open('cassandra.csv','w');

newLine = 'timestamp, cpu[node1]:1,memory[node1]:2,disk_read[node1]:3,disk_write[node1]:4,network_receive[node1]:5,network_send[node1]:6'
newLine += ', cpu[node2]:1,memory[node2]:2,disk_read[node2]:3,disk_write[node2]:4,network_receive[node2]:5,network_send[node2]:6';
newLine += ', cpu[node3]:1,memory[node3]:2,disk_read[node3]:3,disk_write[node3]:4,network_receive[node3]:5,network_send[node3]:6';
newLine += ', cpu[node4]:1,memory[node4]:2,disk_read[node4]:3,disk_write[node4]:4,network_receive[node4]:5,network_send[node4]:6';
newLine += ', cpu[node5]:1,memory[node5]:2,disk_read[node5]:3,disk_write[node5]:4,network_receive[node5]:5,network_send[node5]:6\n';
output.write(newLine)
count = 0;
for line1 in f1:
	line1 = line1.strip('\n').split(',');
	line2 = f2.readline().strip('\n').split(',');
	line3 = f3.readline().strip('\n').split(',');
	line4 = f4.readline().strip('\n').split(',');
	line5 = f5.readline().strip('\n').split(',');

	if count > 0:	
		newLine = line1[0] + ',' + line1[1] + ',' + line1[2] + ',' + line1[3] + ',' + line1[4] + ',' + line1[5] + ',' + line1[6];
		newLine += ',' + line2[1] + ',' + line2[2] + ',' + line2[3] + ',' + line2[4] + ',' + line2[5] + ',' + line2[6];
        	newLine += ',' + line3[1] + ',' + line3[2] + ',' + line3[3] + ',' + line3[4] + ',' + line3[5] + ',' + line3[6];
       		newLine += ',' + line4[1] + ',' + line4[2] + ',' + line4[3] + ',' + line4[4] + ',' + line4[5] + ',' + line4[6];
        	newLine += ',' + line5[1] + ',' + line5[2] + ',' + line5[3] + ',' + line5[4] + ',' + line5[5] + ',' + line5[6] + '\n';
		output.write(newLine)
	count += 1
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
output.close()
