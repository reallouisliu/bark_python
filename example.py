import bark_python

SOUND_LIST = []
USER_COFNIG = {
        'templates':{
            "alchemy": {"title":"炼丹炉", "level":"active", "sound":"chime.caf", "icon":"https://bark.1il.ink/icon/alchemy.png", "group":"炼丹系统"},
            "download": {"title":"BT下载", "level":"active", "sound":"horn.caf", "icon":"https://bark.1il.ink/icon/download.png", "group":"BT下载"}
        }
    }
a = bark_python.Bark("diEMAePsGf3SvjhQbGcnC","https://bark.1il.ink")

a.send_message(body = "惊天魔盗团下载完成", user_config=USER_COFNIG['templates']['download'])