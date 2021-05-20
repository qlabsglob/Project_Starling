# Project_Starling

	Module to be prepared :
		--> Client's Process Server  
			--> Communication Module
				--> Communication Module ( Client - Client )
					--> Module for handling Connection with new connection 
						:: Listening and serving connection 
							: Connection handling 
							: Asking the clinet for which all data to need
							: Aggrigating data for the client 
							: Making sure if the data is recived by the user 
						:: Pinging to all the clients if there is any changes into the file 
					--> Thread Two for 
				--> Communication Module ( Client - Tracker)
					--> Module for asking active client from the server ( address and other info)
						:Handling first time communication with the Tracker server 
						:This includes getting List of Possible Active Clients and address 
						:Sending ur current address to the tracker server for keeping the list
					--> Module for asking for the client address for files in case of failiure 
			
			--> Data Handling Module
				--> Module for handling database migration (sending and reciving data ) 
					:: Model is also responsible for doing data validation 
					:: The enpoint will also reply with the respose. The response indicate success or failure 
					:: For now make the architecture accept support of sqlite for now 
				--> Return the asked sql table using one endpoint 
				--> Return the querry response from response
				:: Data handling module is responsible for 
				
		--> Tracker Server 
			--> Communication Module
				--> Communication Module (Client - Server)
					--> New Connection 
						--> First Node 
							:: For the first connection it should only returns that its the first connection. 
							   All the connection will recive a sequence code.
						--> Successive Connection 
							:: For the first client node, the endpoint should return the socket which is already connected / Have all the files 
							/ Set of all the server that upon combinining all the files.

					--> Old Connection 
					--> Client Status Updates 
						--> Seeder and Leachers Status 
						--> Taking the Updated Socket Id for preexisting connections 
						--> 
				
			--> Data Handling
				--> Log Mentainance 
				--> Recovery Module (If the system resets then start the server with the last log) 
					--> Broadcast ( Broadcast Messages to the user for there updated ips in case any ) --> Helpful in dhcp env
					
				
