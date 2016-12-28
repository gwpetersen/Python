# The client program connects to server and sends data to other connected 
# clients through the server
import socket
import _thread

import sys

def recv_data():
    "Receive data from other clients connected to server"
    while True:
        try:
            recv_data = client_socket.recv(4096)
            message = recv_data.decode("utf8") #bytes are sent so you must decode the message
            
            print(message)
            
            
                    
        except:
            #Handle the case when server process terminates
            print ("Server closed connection, thread exiting.")
            _thread.interrupt_main()
            break
        if not recv_data:
                # Recv with no data, server closed connection
                print ("Server closed connection, thread exiting.")
                _thread.interrupt_main()
                
                break
        else:
                message = recv_data.decode("utf8")
                name = client_socket.getsockname()
               # print ("broadcasted message:  " , message)
                

def send_data():
    "Send data from other clients connected to server"
    while True:
        send_data = str(input("Enter data to send: \n"))
        

        if send_data == "exit" or send_data == "Exit":
            print ("Leaving Chat...")
            _thread.exit()
            _thread.interrupt_main()
            sys.exit()
                        
            break
        else:
            send_data=send_data.encode(encoding='utf_8', errors='strict')
            client_socket.send(send_data) #sends bytes not string
        
if __name__ == "__main__":

    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5000))

    
    name = client_socket.getsockname() # name contains host addr, port
    print ("connected to server at ", name)

    _thread.start_new_thread(recv_data,())
    _thread.start_new_thread(send_data,())

    try:
        while True:
            continue
    except:
        print ("Client program quit....")
        client_socket.close()