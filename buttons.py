import discord
from discord.ext import commands
from discord_buttons_plugin import *
import os

client = commands.Bot(command_prefix=commands.when_mentioned_or("yt!"))
buttons = ButtonsClient(client)

@client.event
async def on_ready():
	print(f"Logged in as {client.user}")

@client.command()
async def invite(ctx):
	embed = discord.Embed(title=f"Invite {client.user.name}", color=0xff0000, description=f"Wanna invite {client.user.name}, then [click here](https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot)")
	await buttons.send(
		content = None,
		embed = embed,
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					style = ButtonType().Link,
					label = "Invite",
					url = f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot"
				)
			])
		]
	)


@buttons.click
async def hibutton(ctx):
	await ctx.reply(f"Hi {ctx.member.name}")

@buttons.click
async def clickbutton(ctx):
	await ctx.reply(f"{ctx.member.name} has clicked the button.")

@buttons.click
async def danger(ctx):
	await ctx.reply(f"{ctx.member}, told'ya not to click!")

@buttons.click
async def lol(ctx):
	await ctx.reply("lol")

@client.command()
async def hi(ctx):
	await buttons.send(
		content="Hey there",
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(

					style = ButtonType().Primary,
					label = "Hi",
					custom_id = "hibutton",

				),

				Button(
					style = ButtonType().Success,
					label = "Click",
					custom_id = "clickbutton"

				),
				Button(
					style = ButtonType().Danger,
					label = "Don't click",
					custom_id = "danger",
				),
				Button(
					style = ButtonType().Secondary,
					label = "Hello",
					custom_id = "lol",
				)
			])
		]
	)

client.run("token")
