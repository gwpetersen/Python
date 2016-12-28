# The server accepts connection from multiple clients and
# broadcasts data sent by a client to all other clients


import socket
import select
import string

# used to broadcast a message from a client to all other clients

def display(sock, message):
  
    
    for socket in socket_list:
        if socket != server_socket and socket != sock:  
            try :
                socket.send(message)
            except :
                socket.close()
                socket_list.remove(sock)
            
            #result_string = message.decode("utf8") # the return will be in bytes, so decode
           # print (result_string)
    

if __name__ == "__main__":

   
    socket_list=[]

    #  create and then listen on the socket
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is just the addresses my socket can communicate with such as IPv4
    server_socket.bind(("127.0.0.1", 5000)) #host, portnumber
    server_socket.listen(5) # listen tells the socket library that we want it to queue up as many as 5 connect requests (the normal max) before refusing outside connections

    # the socket is added to a list of connections
    socket_list.append(server_socket)

    print ("Chat server has started.")
    print ("waiting on potential clients...")
    # Have a continuous loop ready to accept any client trying to connect to server.
    while True:
        # Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(socket_list,[],[])

        for sock in read_sockets:

            if sock == server_socket:
                # a new connection is established add them to the list and display who connected
             
                sockfd, addr = server_socket.accept()
                socket_list.append(sockfd)
                print ("Client (%s, %s) connected" % addr)

            else:
                # messaged recieved from client
                try:
                    
                    data = sock.recv(4096) # if connection is no longer established data = 0
                except:
                    print ("Client (%s, %s) is offline" % addr)
                    sock.close()
                    socket_list.remove(sock)
                    continue

                if data:
                    
                    if data == "exit" or data == "Exit":
                        print ("Client (%s, %s) quits" % addr)
                        sock.close()
                        socket_list.remove(sock)
                    else:
                        display(sock, data)                       
                
    server_socket.close()