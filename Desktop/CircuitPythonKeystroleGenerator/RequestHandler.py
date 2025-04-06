class ServerManager:
    def __init__(self, client):
        self.client = client

    def handle_request(self):
        # Create a buffer to receive initial data
        request = bytearray(1024)
        length = self.client.recv_into(request)

        # Decode the received request data
        request_str = request[:length].decode('utf-8')
        print("Full Request:\n", request_str)

        # Separate headers from body
        headers, _, body = request_str.partition("\r\n\r\n")
        print("Headers:\n", headers)
        print("Body:\n", body)

        # Check for Content-Length
        content_length = 0
        for line in headers.split("\r\n"):
            if line.lower().startswith("content-length:"):
                content_length = int(line.split(":")[1].strip())
                break

        # If the body is incomplete, read the rest
        if content_length > 0 and len(body) < content_length:
            remaining_data = bytearray(content_length - len(body))
            self.client.recv_into(remaining_data)
            body += remaining_data.decode('utf-8')

        return headers, body