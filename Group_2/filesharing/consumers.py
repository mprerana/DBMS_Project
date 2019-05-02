#from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import fileorfolder, peer, chunkshashdb
import json

class Tracker(AsyncConsumer):
	"""
    This consumer handles websocket connections for clients.

    It uses AsyncJsonWebsocketConsumer, which means all the handling functions
    must be async functions, and any sync work (like ORM access) has to be
    behind database_sync_to_async or sync_to_async. For more, read
    http://channels.readthedocs.io/en/latest/topics/consumers.html
    """


	@database_sync_to_async
	def Search(self,FILENAME):
		try:
			# .values() creates an instance of a list i.e
			#[{'filename':val1, 'filehash': val2}{'filename':val3, 'filehash': val4}]
			return fileorfolder.objects.filter(file_name__contains=FILENAME).values()
		except Exception as e:
			raise e

	@database_sync_to_async
	def peerChunksInfo(filehash):
		peerlist = peer.objects.filter(file_hash=filehash).values()
		chunksinfo = chunkshashdb.objects.filter(file_hash=filehash).values()
		return (peerlist,chunksinfo)


	@database_sync_to_async
	def Share(self,content,peerid):
		'''
		When a new file is being shared, We ask peer to send the hashes of chunks too
		'''
		try:
			
			fileorfolder_obj,fileorfolder_created  = fileorfolder.objects.get_or_create(file_hash=content['FILEHASH'],
													defaults={'file_name':content['FILENAME'],
													'file_size':content['SIZE'], 'number_peers':0})
			print(fileorfolder_obj)							
			fileorfolder_obj.save()
			peer_obj, peer_created = peer.objects.get_or_create(file_hash=content['FILEHASH'],peer=peerid)
			peer_obj.save()

			if fileorfolder_created:
				return 'Send Chunks Tracker'
			else:
				return 'not first'

			'''
			If file hash already exists
			-> Check if peer already exists -> yes: Do Nothing
											-> no: Append Peer
			If File hash doesn't exist add file
			create a queing mechanism for chunking and hashes of chunks
			Downloading
			'''
		except Exception as e:
			raise e

	@database_sync_to_async
	def StoreChunks(content):
		#ChunkDict is list of dicts
		for chunk in content['chunkDict']:
			chunkshashdb_obj, chunkshashdb_created = chunkshashdb.objects.get_or_create(file_hash=content['FILEHASH'],
																						chunks=chunk['CHUNKHASH'], offset=chunk['OFFSET'])
			chunkshashdb_obj.save()
		'''
		#Stay less with no. of chunks
		'''










	##### WebSocket event handlers
	async def websocket_connect(self,message):
		"""
		Called when the websocket iwasda	s handshaking as part of initial connection.
		"""
		await self.send({
		'type':'websocket.accept',
				})

	async def websocket_disconnect(self):
		# await self.close()
		pass

	async def websocket_receive(self, text_data):
		print('$$$$', text_data)
		await self.send({
		'type' :'websocket.send',
		'text':text_data['text']				
				})
		content = json.loads(text_data['text'])
		command = content['COMMAND']
		try:
			if command == 'SEARCH':
				fileInfo = await self.Search(content['FILENAME'])
				if fileInfo:
					await self.send({'message':"Following files found",'list':fileInfo
				})
					#await self.send_json({'message':"Following files found",'list':fileInfo})
				else:
					await self.send({'message':"Following files found",'list':fileInfo
				})

			elif command == 'DOWNLOAD':
				peer_chunks_info = await peerChunksInfo(content['FILEHASH'])
				await self.send_json({'Peers':peer_chunks_info[0], 'Chunks':peer_chunks_info[1]})

			elif command == 'SHARE':
				peerid = self.scope['client'][0]
				print(peerid)
				resp = await self.Share(content, peerid)
				#if resp == 'Send Chunks Tracker':
				#	await self.send_json({'message':resp, 'filehash': content['FILEHASH']})
					# Client will recieve this message and create chunks
					# If network error, We'll delete this later
				#elif resp == 'not first':
				#	await self.send_json({{'message':resp}})

			elif command == 'CHUNKSHARE':
				# cONTENT = filehash, dict{'hash',offst}
				await StoreChunks(content)

			elif command == 'UnShare':
				pass

		except Exception as e:
			raise e

		'''
		This function recieves query_type variable and does corresponding tasks.
		query_type = [Share, Search, Unshare]
		Write Exceptions
		Cli Client to be made
		'''




























# # chat/consumers.py
# from asgiref.sync import async_to_sync
# from channels.generic.websocket import JsonWebsocketConsumer
# import json
# from .models import peer, hashTable, refTable
# import datetime
#
# class showDatabaseConsumer(JsonWebsocketConsumer):
#
#     def connect(self):
#         async_to_sync(self.channel_layer.group_add)('active',self.channel_name)
#         self.accept()
#
#
#     def disconnect(self, close_code):
#         async_to_sync(self.channel_layer.group_discard)(
#             'active',
#             self.channel_name
#         )
#
#     # Receive message from WebSocket
#     def receive_json(self, content):
#
#         '''
#             Message= {
#             'command': Share/Unshare/Search
#             'hash' : filehash -Share/unshare
#             'size' : filesize  -share
#             'Filename':filename -search/share/unshare
#             }
#             -->>Share
#             self.client = self.scope['client'] --> store in database
#             Shareddate - scope
#             lastuseddate - same
#         '''
#         command = content.get("command", None)
#         if command =='Share':
#             print(content)
#             print("debug111")
#             peerid = self.scope['client'][0]
#             shareddate = datetime.date.today
#             lastuseddate = datetime.date.today
#             file_obj, file_obj_created  =  hashTable.objects.get_or_create(filename=content['filename'],
#                                                                             filehash=content['hash'],
#                                                                              size=content['size'],
#                                                                              defaults={'shareddate': shareddate,
#                                                                                         'lastuseddate':lastuseddate})
#             print("debug")
#             file_obj.save()
#
#             peer_obj, peer_obj_created = peer.objects.get_or_create(peer_ip=peerid)
#             peer_obj.save()
#
#             refTableobj, refTableobj_created = refTable.objects.get_or_create(peer=peer_obj, filehash=file_obj)
#             refTableobj.save()
#
#             self.send_json({
#                 "message" : "Stored in database"
#                 })
#
#         elif command == 'Unshare':
#             pass
#
#         elif command == 'Search':
#             filename = content['filename']
#             get_fileinfo =  hashTable.objects.filter(filename__contains=filename).values('filename','filehash','size')
#             print(get_fileinfo.query)
#             get_peerinfo = refTable.objects.filter(filehash__filehash__in=[file['filehash'] for file in get_fileinfo]).values('filehash__filehash','filehash__size','peer__peer_ip')
#             print(list(get_peerinfo))
#             self.send_json({
#                 "Peer_List" : list(get_peerinfo),
#                 })
#
#
