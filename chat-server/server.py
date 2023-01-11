from concurrent import futures
import time

import grpc
import chat_pb2
import chat_pb2_grpc

class ChatServicer(chat_pb2_grpc.ChatService):

    def __init__(self) -> None:
        self.messages = []

    def GetMessages(self, request, context):
        print("GetMessages")
        print("Request", request)

        size = len(self.messages)
        for i in range(size - 1, -1, -1):
            if self.messages[i].receiver == request.receiver and self.messages[i].sender == request.sender\
                or self.messages[i].receiver == request.sender and self.messages[i].sender == request.receiver:
                yield self.messages[i]
                #self.messages.pop(i)
    
    def PostMessage(self, request, context):
        print("Request", request)
        self.messages.append(request)
        return request

    def GetMessagedUsers(self, request, context):
        print("Request", request)
        print(request)
        return_set = set()

        size = len(self.messages)
        for i in range(size - 1, -1, -1):
            if self.messages[i].receiver == request.name:
                print(self.messages[i].sender)
                return_set.add(self.messages[i].sender)
        
        for elem in return_set:
            reply = chat_pb2.User(name = elem)
            yield reply

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatServicer(), server)
    server.add_insecure_port("10.5.0.3:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()