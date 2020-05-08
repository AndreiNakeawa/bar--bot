import os
import discord
import asyncio
import random
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print("Ricardão está de pica dura")
    print(client.user.name)
    print(client.user.id)
    print("--------")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('b!kinam'):
        kinamsg = ['Pintassilgo', 'Coiso', 'Eis que', 'Marcos', 'Ednaldo Pereira']
        await message.channel.send(random.choice(kinamsg))

    if message.content.startswith('b!leyks'):
        ley = ['ochiai gostos','ochiai pq vc me odeia','ochiai por que','ochinchi' ,'Kureito!!!!', '@KUREITO @KUREITO ME AJUDA', '@kueeito@kureito@kureito askdasdasd kureito msakureitoooooooooo queulreito kureito aasidas kureito oi kureito@kueeito@kureito@kureito askdasdasd kureito msakureitoooooooooo queulreito kureito aasidas kureito oi kureito']
        await message.channel.send(random.choice(ley))

    if message.content.startswith('b!shade'):
        await message.channel.send('Eu, Shade, sou casado com o Leyks, e ninguém, NINGUÉM pode negar meu amor por ele! Se eu tentar esconder isso um dia, saiba que estou apenas de birra, amo o Leyks do fundo do meu coração!')

    if message.content.startswith('b!kureito'):
        kureitomsg = ['CALA A BOCA LEYKS', 'VAI TOMA NO CU LEYKS', 'sai leyks', 'fica quieto leyks', 'entendi leyks, agora fica quieto ai', 'Não leyks']
        await message.channel.send(random.choice(kureitomsg))

    if message.content.startswith('b!ochiai'):
        ochiaimsg = ['I need you senpai <3']
        await message.channel.send('I need you senpai <3')

    if message.content.startswith('b!kamuri'):
        kamurimsg = ['Homework? You still have a long way to go. I am the Great Archdemon Satanichia, Queen of all Hell! Naturally, I dont do homework!', 'negros', 'banido', 'pretos']
        await message.channel.send(random.choice(kamurimsg))

    if message.content.startswith('b!jooj'):
        await message.channel.send('Cú de criança é igual milho, cresceu cabelo já pode comer')

    if message.content.startswith('b!copypasta'):
        copypasta = ['Amigo você nem é um pássaro, você não possui bico nem penas, muito menos asas. Eu duvido que um especialista da área da taxonomia um dia poderia considerar você como um pássaro. Sinto muita pena da sua vida miserável e como tirou a vida de meu amigo a sangue frio, não consigo sentir a mínima empatia por um ser como você. Espero que você repense seus conceitos e tome um bom rumo com a tua vida.', ]
        await message.channel.send(random.choice(copypasta))

    if message.content.startswith('b!cucktales'):
        await message.channel.send('Uh uh! Ricardão está de pica dura!')

    if message.content.startswith('b!procuradoleyks'):
        embleyks = discord.Embed(title='PROCURA-SE FORAGIDO', description='Indivíduo atende pelo nome de **Leyks** e é procurado por **ser macaco**, recompensa de R$500 mil - vivo ou morto ', color=0xe74c3c)
        embleyks.set_image(url='https://cdn.discordapp.com/attachments/474716449961934870/708419995603828816/download.jpg')
        await message.channel.send(content=None,  embed=embleyks)

    if message.content.startswith('b!procuradoochiai'):
        embochiai = discord.Embed(title='PROCURA-SE FORAGIDO',description='Indivíduo atende pelo nome de **Ochiai** e é procurado por **roubar meu coração**, recompensa de R$2.000.000', color=0xe74c3c)
        embochiai.set_image(url='https://imgur.com/rvdvA0k.png')
        await message.channel.send(content=None,  embed=embochiai)

    if message.content.startswith('b!procuradokureito'):
        embkureito = discord.Embed(title='PROCURA-SE FORAGIDO', description='Indivíduo atende pelo nome de **Kureito** e é procurado pelo motivo abaixo, recompensa de R$5.000.000',color=0xe74c3c)
        embkureito.set_image(url='https://cdn.discordapp.com/attachments/474716449961934870/708440172613599382/unknown.png')
        await message.channel.send(content=None, embed=embkureito)

    if message.content.startswith('b!aimeupirunovinhasentadivaganopiruuu'):
        flood = '🤡🤡 VØÇË§ FØŘÅM ÅŤÅČÅĐØ§ PËĽØ§ PÅĽHÅÇØ§ ĽØĶØ§ 🤡🤡'
        contador = 0
        while contador < 1000:
            await message.channel.send(flood)
            contador = contador + 1



client.run("NzA3NzU3OTk0NzE2NDMwMzg2.XrNmig.9Gx-igTWgwbH1Yas5K3XpIAQpPY")
