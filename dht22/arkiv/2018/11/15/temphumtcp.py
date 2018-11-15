#!/usr/bin/env python3
# vim:ts=4:sw=4:sts=4:et:ai:fdm=marker

# libs
import asyncio
import datetime
import sqlite3
import time

# vars
dbname = 'temphumtcp.sqlite3'
tablename = "temphum"
sock_port = 4949
sock_addr = '0.0.0.0'

# db setup
conn = sqlite3.connect(dbname)
dbc = conn.cursor()

# Create table in db if it doesn't exist
sql = "create table if not exists " + tablename + "(id integer primary key autoincrement, time float, temperature float, humidity float)"
dbc.execute(sql)

async def handle_munin_node(reader, writer):
    quit = 0
    answer = 'wtf?'
    greeting = b"munin node at ESPxx\r\n"

    writer.write(greeting)
    await writer.drain()

    while quit == 0:
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')
        print("Received %r from %r" % (message, addr))

        print("Send: %r" % message)
        # writer.write(data)
        # await writer.drain()

        message = (message.lower())

        if message == "list\r\n":
            answer = b"dht\r\n"
            writer.write(answer)
            await writer.drain()
        elif message == "config\r\n":
            answer = b"# Unknown service\r\n"
            writer.write(answer)
            await writer.drain()
        elif message == "config dht\r\n":
            answer = b"graph_title Temperature and humidity from DHT sensor\r\ndht_temp.label Temperature (C)\r\ndht_temp.type DERIVE\r\ndht_temp.graph yes\r\ndht_hum.label Temperature (C)\r\ndht_hum.type DERIVE\r\ndht_hum.graph yes\r\ndht_hum.min 0\r\ndht_hum.max 100\r\n"
            writer.write(answer)
            await writer.drain()
        elif message == "fetch\r\n":
            answer = b"# Unknown service\r\n"
            writer.write(answer)
            await writer.drain()
        elif message == "fetch dht\r\n":
            answer = b"dht_temp.value = 23.3\r\ndht_hum.value = 32.5\r\n"
            writer.write(answer)
            await writer.drain()
#       elif message == "fetch dht\r\n":
#           # fetch the data - until that - post som dummies
#           answer = b"graph_title Temperature and humidity from DHT sensor\r\ndht_temp.label Temperature (C)\r\ndht_temp.type DERIVE\r\ndht_temp.graph yes\r\ndht_hum.label Temperature (C)\r\ndht_hum.type DERIVE\r\ndht_hum.graph yes\r\ndht_hum.min 0\r\ndht_hum.max 100\r\n"
#           writer.write(answer)
#           await writer.drain()
        elif message == "quit\r\n":
            quit = 1
        else:
            answer = b"# Unknown command. Try list, config, fetch or quit\r\n"
            writer.write(answer)
            await writer.drain()

        answer = b".\r\n"
        writer.write(answer)
        await writer.drain()

        print("Going on, message is '%r' and quit is %r" % (message, quit))

    print("Close the client socket")
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_munin_node, sock_addr, sock_port, loop=loop)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()

# print("time.time() now is", time.time())

