import discord
from colorama import Fore, init, Style


def print_add(message):
    print(f'{Fore.GREEN}[TERMINE]{Style.RESET_ALL} {message}')

def print_delete(message):
    print(f'{Fore.RED}[SUPPRESSION]{Style.RESET_ALL} {message}')

def print_warning(message):
    print(f'{Fore.YELLOW}[WARN]{Style.RESET_ALL} {message}')


def print_error(message):
    print(f'{Fore.RED}[ERREUR]{Style.RESET_ALL} {message}')


class Clone:
    @staticmethod
    async def roles_delete(guild_to: discord.Guild):
            for role in guild_to.roles:
                try:
                    if role.name != "@everyone":
                        await role.delete()
                        print_delete(f"Suppression du rôle : {role.name}")
                except discord.Forbidden:
                    print_error(f"Un probleme a été détecté lors de la performance de cette action : {role.name}")
                except discord.HTTPException:
                    print_error(f"Un probleme a été détecté lors de la performance de cette action : {role.name}")

    @staticmethod
    async def roles_create(guild_to: discord.Guild, guild_from: discord.Guild):
        roles = []
        role: discord.Role
        for role in guild_from.roles:
            if role.name != "@everyone":
                roles.append(role)
        roles = roles[::-1]
        for role in roles:
            try:
                await guild_to.create_role(
                    name=role.name,
                    permissions=role.permissions,
                    colour=role.colour,
                    hoist=role.hoist,
                    mentionable=role.mentionable
                )
                print_add(f"Création du rôle : {role.name}")
            except discord.Forbidden:
                print_error(f"Un probleme a été détecté lors de la performance de cette action: {role.name}")
            except discord.HTTPException:
                print_error(f"Un probleme a été détecté lors de la performance de cette action: {role.name}")

    @staticmethod
    async def channels_delete(guild_to: discord.Guild):
        for channel in guild_to.channels:
            try:
                await channel.delete()
                print_delete(f"Suppression du salon : {channel.name}")
            except discord.Forbidden:
                print_error(f"Un probleme a été détecté lors de la performance de cette action: {channel.name}")
            except discord.HTTPException:
                print_error(f"Un probleme a été détecté lors de la performance de cette action: {channel.name}")

    @staticmethod
    async def categories_create(guild_to: discord.Guild, guild_from: discord.Guild):
        channels = guild_from.categories
        channel: discord.CategoryChannel
        new_channel: discord.CategoryChannel
        for channel in channels:
            try:
                overwrites_to = {}
                for key, value in channel.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                new_channel = await guild_to.create_category(
                    name=channel.name,
                    overwrites=overwrites_to)
                await new_channel.edit(position=channel.position)
                print_add(f"Création de la catégorie : {channel.name}")
            except discord.Forbidden:
                print_error(f"Un probleme a été détecté lors de la performance de cette action: {channel.name}")
            except discord.HTTPException:
                print_error(f"Un probleme a été détecté lors de la performance de cette action: {channel.name}")

    @staticmethod
    async def channels_create(guild_to: discord.Guild, guild_from: discord.Guild):
        channel_text: discord.TextChannel
        channel_voice: discord.VoiceChannel
        category = None
        for channel_text in guild_from.text_channels:
            try:
                for category in guild_to.categories:
                    try:
                        if category.name == channel_text.category.name:
                            break
                    except AttributeError:
                        print_warning(f"Le salon {channel_text.name} n'as pas de catégorie!")
                        category = None
                        break

                overwrites_to = {}
                for key, value in channel_text.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                try:
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position,
                        topic=channel_text.topic,
                        slowmode_delay=channel_text.slowmode_delay,
                        nsfw=channel_text.nsfw)
                except:
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position)
                if category is not None:
                    await new_channel.edit(category=category)
                print_add(f"Création du salon textuel : {channel_text.name}")
            except discord.Forbidden:
                print_error(f"Un probleme a été détecté lors de la performance de cette action: {channel_text.name}")
            except discord.HTTPException:
                print_error(f"Un probleme a été détecté lors de la performance de cette action: {channel_text.name}")
            except:
                print_error(f"Un probleme a été détecté lors de la performance de cette action: {channel_text.name}")

        category = None
        for channel_voice in guild_from.voice_channels:
            try:
                for category in guild_to.categories:
                    try:
                        if category.name == channel_voice.category.name:
                            break
                    except AttributeError:
                        print_warning(f"Le salon {channel_voice.name} n'as pas de catégorie.")
                        category = None
                        break

                overwrites_to = {}
                for key, value in channel_voice.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                try:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position,
                        bitrate=channel_voice.bitrate,
                        user_limit=channel_voice.user_limit,
                        )
                except:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position)
                if category is not None:
                    await new_channel.edit(category=category)
                print_add(f"Création du salon vocal : {channel_voice.name}")
            except discord.Forbidden:
                print_error(f"Un probleme a été détecté lors de la performance de cette action: {channel_voice.name}")
            except discord.HTTPException:
                print_error(f"Un probleme a été détecté lors de la performance de cette action: {channel_voice.name}")
            except:
                print_error(f"Un probleme a été détecté lors de la performance de cette action: {channel_voice.name}")


    @staticmethod
    async def emojis_delete(guild_to: discord.Guild):
        for emoji in guild_to.emojis:
            try:
                await emoji.delete()
                print_delete(f"Suppression de l\'Emoji: {emoji.name}")
            except discord.Forbidden:
                print_error(f"Un probleme a été détecté lors de la performance de cette action{emoji.name}")
            except discord.HTTPException:
                print_error(f"Un probleme a été détecté lors de la performance de cette action {emoji.name}")

    @staticmethod
    async def emojis_create(guild_to: discord.Guild, guild_from: discord.Guild):
        emoji: discord.Emoji
        for emoji in guild_from.emojis:
            try:
                emoji_image = await emoji.url.read()
                await guild_to.create_custom_emoji(
                    name=emoji.name,
                    image=emoji_image)
                print_add(f"Création de l'émoji : {emoji.name}")
            except discord.Forbidden:
                print_error(f"Un probleme a été détecté lors de la performance de cette action {emoji.name} ")
            except discord.HTTPException:
                print_error(f"Un probleme a été détecté lors de la performance de cette action {emoji.name}")

    @staticmethod
    async def guild_edit(guild_to: discord.Guild, guild_from: discord.Guild):
        try:
            try:
                icon_image = await guild_from.icon_url.read()
            except discord.errors.DiscordException:
                print_error(f"Un probleme a été détecté lors de la performance de cette action : {guild_from.name}")
                icon_image = None
            await guild_to.edit(name=f'{guild_from.name}')
            if icon_image is not None:
                try:
                    await guild_to.edit(icon=icon_image)
                    print_add(f"Changement de l'icone du serveur: {guild_to.name}")
                except:
                    print_error(f"Un probleme a été détecté lors de la performance de cette action : {guild_to.name}")
        except discord.Forbidden:
            print_error(f"Un probleme a été détecté lors de la performance de cette action : {guild_to.name}")