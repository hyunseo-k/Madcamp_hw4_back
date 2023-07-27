import json

from channels.generic.websocket import AsyncWebsocketConsumer


class DrawboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.drawboard_id = self.scope["url_route"]["kwargs"]["drawboard_id"]
        self.drawboard_group_name = f"drawboard_{self.drawboard_id}"

        # Join room group
        await self.channel_layer.group_add(self.drawboard_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.drawboard_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('message', {}).get('action', '')

        if action == 'draw':
            draw_instruction = data.get('message', {}).get('drawInstruction', {})
            # Broadcast the drawing instruction to other connected clients
            await self.channel_layer.group_send(
                self.drawboard_group_name,
                {
                    'type': 'draw_instruction',
                    'draw_instruction': draw_instruction
                }
            )
        elif action == 'clear':
            # Broadcast a clear action to other connected clients
            await self.channel_layer.group_send(
                self.drawboard_group_name,
                {
                    'type': 'clear_canvas'
                }
            )
    async def draw_instruction(self, event):
        draw_instruction = event['draw_instruction']
        # Send the drawing instruction to the client
        await self.send(text_data=json.dumps({
            'message': {
                'drawInstruction': draw_instruction
            }
        }))

    async def clear_canvas(self, event):
        # Send a clear action to the client
        await self.send(text_data=json.dumps({
            'message': {
                'action': 'clear'
            }
        }))