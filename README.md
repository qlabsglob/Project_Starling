# Project_Starling

	Module to be prepared :
		--> Client's Process Server  
			--> Communication Module
				--> Communication Module ( Client - Client
					--> Module for handling Connection with new connection 
						:: Listening and serving connection 
							: Connection handling 
							: Asking the clinet for which all data to need
							: Aggrigating data for the client 
							: Making sure if the data is recived by the user 
						:: 
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
				
			--> Data Handling
				--> Log Mentainance 
				--> Recovery Module (If the system resets then start the server with the last log) 
					--> Broadcast ( Broadcast Messages to the user for there updated ips in case any ) --> Helpful in dhcp env
				
