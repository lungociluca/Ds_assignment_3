import chat_pb2_grpc, chat_pb2
import grpc

def run():
    case = input("Case: ")
    print(case)
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = chat_pb2_grpc.ChatServiceStub(channel)

        if case == '1':
            request = chat_pb2.Message(sender="Not used", receiver="John", message="Null")
            reply = stub.GetMessages(request)

            for elem in reply:
                print("Received: ", str(elem))
        elif case == '2':
            request = chat_pb2.Message(sender="Carl", receiver="John", message="Welcome to San Andreass")
            reply = stub.PostMessage(request)
            print(reply)
        elif case == '3':
            request = chat_pb2.User(name="John")
            reply = stub.GetMessagedUsers(request)
            for elem in reply:
                print(elem)
        elif case == '4':
            
            users = ["Luca", "Lungoci", "Carl", "Claude", "Tommy", "Michael", "Trevor", "Franklin"]

            for i in range(0, len(users), 2):
                request = chat_pb2.Message(sender=users[i], receiver=users[i+1], message=f"Hello {i}")
                stub.PostMessage(request)

            for i in range(len(users)):
                request = chat_pb2.User(name=users[i])
                print(f'{users[i]} has messages from: ',)
                reply = stub.GetMessagedUsers(request)
                for elem in reply:
                    print(elem,)
                print()

            request = chat_pb2.Message(sender="Rus Iulia", receiver="Lungoci Luca", message=f"Mesaj nou")
            stub.PostMessage(request)
            request = chat_pb2.Message(sender="Rus Iulia", receiver="Lungoci Luca", message=f"Sevus, ce faci?")
            stub.PostMessage(request)
            request = chat_pb2.Message(sender="Rus Iulia", receiver="Lungoci Luca", message=f"Ultim mesaj")
            stub.PostMessage(request)
            request = chat_pb2.Message(sender="Lungoci Luca", receiver="Rus Iulia", message=f"Multumesc")
            stub.PostMessage(request)
            request = chat_pb2.Message(sender="CJ", receiver="Lungoci Luca", message=f"Ultim mesaj")
            stub.PostMessage(request)

            request = chat_pb2.Message(sender="Rus Iulia", receiver="Lungoci Luca", message="Null")
            reply = stub.GetMessages(request)
            for elem in reply:
                print(f"{elem.sender} -> {elem.receiver}: {elem.message} ")

if __name__ == "__main__":
    run()