devnum = input("How many devices are you configuring?: ")
x = 1
y = 1

for num in range(0,int(devnum)):
	
	a = input("\nAre you configuring a Switch or a Router?: ")

	if a == 's' or  a == 'switch' or a == 'Switch' or a == 'S':
		intnuma = 1
		Sw1 = open("Switch"+str(y)+".txt", "w")
		Sw1.write('enable\nconfigure terminal\n')
		Sw1.write('service password-encryption\n')
		Sw1.write('hostname' + ' ' + input("Enter your desired hostname: "))
		Sw1.write('\nenable secret' + ' ' + input("Enter your desired Privileged EXEC password: "))
		Swint = input("How many Vlan interfaces are you configuring?: ")
		for num in range(0,int(Swint)):
			Sw1.write('\nint' + ' ' + input("Enter the name of your vlan interface" + ' (' + str(intnuma) + "): "))
			Sw1.write('\nip address' + ' ' + input("Enter the IP address for the interface: "))
			Sw1.write(' ' + input("Enter the subnet Mask: "))
			Sw1.write('\nno shut')
			intnuma +=1
		Sw1.close()
		y += 1

	if a == 'r' or a == 'R' or a == 'router' or a == 'Router':
		intnumb = 1
		R1 = open("Router"+str(x)+".txt","w")
		R1.write('enable\nconfigure terminal\n')
		R1.write('service password-encryption\n')
		R1.write('hostname' + ' ' + input("Enter your desired hostname: "))
		R1.write('\nenable secret' + ' ' + input("Enter your desired Privileged EXEC password: "))
		R1.write('\nline vty 0 15\npassword' + ' ' + input("Enter your desired line vty password: "))
		Rint = input("How many interfaces are you configuring?: ")
		for num in range(0,int(Rint)):
			R1.write('\nint' + ' ' + input("Enter the name of your interface" + ' (' + str(intnumb) + "): "))
			R1.write('\nip address' + ' ' + input("Enter the IP address for the interface: "))
			R1.write(' ' + input("Enter the subnet Mask: "))
			R1.write('\nno shut')
			intnumb += 1
		R1.close()
		x += 1
	
