import discord
import json
from script.clima import pesquisa_clima
from script.bolsa import buscar_acao

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        dados = buscar()
        
        if ("bot" in message.content ):
            if (quebrar_comando(message.content) in dados.keys()):                
                await message.channel.send('{0}'.format(message.author.name + dados.get(quebrar_comando(message.content), " comando não encontrado.")))
            elif (quebrar_comando(message.content) == "clima"):
                await message.channel.send(f"{message.author.name} {pesquisa_clima(message.content)}")
            elif (quebrar_comando(message.content) == "acao"):
                await message.channel.send(f"{message.author.name} {buscar_acao(message.content)}")

def buscar():
    with open("script/commands.json", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados

def quebrar_comando(command):
    cmd = command.split(' ')
    return cmd[1]

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents = intents)
client.run('MTAyNTE0MTA5OTY2NjM1MDE5MQ.GIVr5X.Ei4Cy4BAJBZXm3ffmPbAJz-iSa_F1qLECdh38w')
