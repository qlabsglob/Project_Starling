## Database Api 
    --> DatabaseApi is a Flask Blueprint Api Endpoint for accessing Sqlite3 database 
    --> Database Life Cycle
        --> Initalisation 
        --> Validation 
        --> Querry Execution 
        --> Commit and close connection at the End
    --> Databases Required  
        --> PeerNetwork (Stores the List of Peers)
            :: Contains the hashtable with socket 
            :: hashing id is given to the client during creating,
            :: Hashing id is primary id with the socket information 
            :: Boolean Flag will indicate if it contains all the files 
            :: Timestamp column regarding last ping updates 
            :: Json String contining what all files are present
            --> Api Endpoints Required 
                :: Inserting the new Entry 
                :: Updating the entry against Hashing Id
                :: Get the Entery List based on the non unique Feilds
                :: ping receiver ==> If any changes then update the db
                :: Api Endpoint ==> If it requires any file then whom to contact (Peer)
                    ::==> If the peer is not there, then it will return the file itself 
            --> Broadcast Websocket if there is any changes

    
