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
