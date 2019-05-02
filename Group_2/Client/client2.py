import os
import asyncio
import websockets
import json
#import shutil
#from hashchunk import hashIt, chunkIt
import hashingandchunking
#import mysql.connector


async def test():

    async with websockets.connect('ws://127.0.0.1:8000/ws/boxoshare/') as websocket:
        user_input = input('Enter 1 to share, 2 to search')
        content = {'COMMAND':'SHARE',
                   'FILENAME':'got3',
                   'FILEHASH':'QWEQWEQWE123123',
                   'SIZE':123123}


        
        if user_input == '1':
            #shutil.rmtree(os.getcwd()+'/torrent-hub-file/')
            static_dir_path = os.getcwd()+'/torrent-hub-file/'
            
            print(static_dir_path)
            access_rights = 0o777
            os.mkdir(static_dir_path, access_rights)
            file_path = input('Input File Path')
            file_hash_tup = hashingandchunking.hashing(file_path)
            file_chunk_dict = hashingandchunking.split_equal(file_path,static_dir_path)
            file_hash = file_hash_tup[0]
            file_size = file_hash_tup[1]
            file_name = file_path.split('/')
            file_name = file_name[-1]
            content = {
            'COMMAND':'SHARE',
                       'FILENAME':file_name,
                       'FILEHASH':file_hash,
                       'SIZE':file_size
            }
            print(content)
            await websocket.send(json.dumps(content))
           

        elif user_input == '2':
            file_name = input('Input File Name')
            content = {
            'COMMAND':'SEARCH',
                       'FILENAME':file_name,
            }
            await websocket.send(json.dumps(content))
            
        response = await websocket.recv()
        response = json.loads(response)

        #if response['message'] == 'Send Chunks Tracker':
            # table filehash and path
            # retrieve file path
            # chunkDict=chunkIt(filepath)
            #await websocket.send(json.dumps(content))
asyncio.get_event_loop().run_until_complete(test())

'''
Calculate file FILEHASH => SHARE
if mess = 'Send Chumks Tracker'
    cal chunks
    cal hashes
    store in your db
    send hashes
if mess = 'not first'
    cal (random) chunks
    store hashes in your db

When Sharing with peer
    Recieve bit string
    Send Bit string
        peer2 rcv bit string
        Schedule/ sendrequests for chunks
    send chunks
        rcv chunks
    When Done del some chunks
    send the new bit string
        recv bitstr store some chunks
        Combine recieved Chunks

        import hashlib

def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

print('The MD5 checksum of text.txt is', md5Checksum('test.txt'))
'''



