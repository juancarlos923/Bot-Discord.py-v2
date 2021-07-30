import discord, datetime
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description="Este É um Bot Faz Tudo")
bot.ticket_configs = {}

@bot.command() #ping
async def ping(ctx):
  embed = discord.Embed(title="Meu Tempo de Resposta!", description=f"{round(bot.latency*1000)} ms", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
  embed.set_footer(text=f'Solicitado Por {ctx.author}')
  embed.set_thumbnail(url="https://media.tenor.com/images/b1c98908e2b1f6b2cdbad3ab98d60248/tenor.gif")
  await ctx.send(embed=embed)

@bot.command() #kick
async def kick(ctx, member : discord.Member=None, *, reason=None):
    if member is None:
        embed1 = discord.Embed(title="Mencione o Usuário Que Tomara Kick!", description="Ex.: !kick @user Motivo", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
        embed1.set_footer(text=f'Solicitado Por {ctx.author}')
        embed1.set_thumbnail(url="https://engenheirodecustos.com.br/wp-content/uploads/2019/02/Erro.jpeg")
        await ctx.send(embed=embed1)
        return
    if reason is None:
        reason = 'Não Informado'
    
    embed3 = discord.Embed(title=f"Você Tomou Kick do Servidor: {ctx.guild.name}", description=f"Motivo: {reason}", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
    embed3.set_footer(text=f'Kikado Por {ctx.author}')
    embed3.set_thumbnail(url="https://cliqueuniao.com.br/wp-content/uploads/2018/11/arbitro-580x335.jpg")
    await member.send(embed=embed3)
    
    await member.kick(reason=reason)#Ação de Kick
    
    embed2 = discord.Embed(title=f"Usuário(a) {member} Tomou Kick", description=f"Motivo: {reason}", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
    embed2.set_footer(text=f'Kikado Por {ctx.author}')
    embed2.set_thumbnail(url="https://cliqueuniao.com.br/wp-content/uploads/2018/11/arbitro-580x335.jpg")
    await ctx.send(embed=embed2)#Ação de Envio de Mensagem
    return

@bot.command() #ban
async def ban(ctx, member : discord.Member=None, *, reason=None):
    if member is None:
        embed1 = discord.Embed(title="Mencione o Usuário Que Tomara Ban!", description="Ex.: !ban @user Motivo", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
        embed1.set_footer(text=f'Solicitado Por {ctx.author}')
        embed1.set_thumbnail(url="https://engenheirodecustos.com.br/wp-content/uploads/2019/02/Erro.jpeg")
        await ctx.send(embed=embed1)
        return
    if reason is None:
        reason = 'Não Informado'
    
    embed3 = discord.Embed(title=f"Você Tomou Ban do Servidor: {ctx.guild.name}", description=f"Motivo: {reason}", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
    embed3.set_footer(text=f'Banido Por {ctx.author}')
    embed3.set_thumbnail(url="https://cliqueuniao.com.br/wp-content/uploads/2018/11/arbitro-580x335.jpg")
    await member.send(embed=embed3)
    
    await member.ban(reason=reason)#Ação de Ban
    
    embed2 = discord.Embed(title=f"Usuário(a) {member} Tomou Ban", description=f"Motivo: {reason}", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
    embed2.set_footer(text=f'Banido Por {ctx.author}')
    embed2.set_thumbnail(url="https://cliqueuniao.com.br/wp-content/uploads/2018/11/arbitro-580x335.jpg")
    await ctx.send(embed=embed2)#Ação de Envio de Mensagem
    return

@bot.command() #unban
async def unban(ctx, *, member=None):
    if member is None:
        embed1 = discord.Embed(title="Mencione o Usuário Que Tomara Unban!", description="Ex.: !unban @user", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
        embed1.set_footer(text=f'Solicitado Por {ctx.author}')
        embed1.set_thumbnail(url="https://engenheirodecustos.com.br/wp-content/uploads/2019/02/Erro.jpeg")
        await ctx.send(embed=embed1)
        return

    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed2 = discord.Embed(title=f"Usuário(a) {member} Tomou Unban", description=f"Desbanido Por {ctx.author}", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
            embed2.set_thumbnail(url="https://media1.giphy.com/media/21Q0iTg8c1tabEcIBe/giphy.gif")
            await ctx.send(embed=embed2)#Ação de Envio de Mensagem
            return

@bot.command()
async def deletar_canal(ctx):
    await ctx.channel.delete()

@bot.command()
async def criar_canal(ctx, canal_name=None):
    await ctx.channel.purge(limit=1)
    if canal_name is None:
        embed1 = discord.Embed(title="Informe o Nome do Canal", description="Ex.: !criar_canal Chat", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
        embed1.set_thumbnail(url="https://image.flaticon.com/icons/png/512/35/35840.png")
        await ctx.send(embed=embed1)#Ação de Envio de Mensagem
        return
    await ctx.guild.create_text_channel(name=canal_name)
    embed2 = discord.Embed(title="Canal Criado!", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
    embed2.set_thumbnail(url="https://cdn.pixabay.com/photo/2015/06/09/16/12/icon-803718_960_720.png")
    await ctx.send(embed=embed2)#Ação de Envio de Mensagem

bot.run("SEU_TOKEN")
