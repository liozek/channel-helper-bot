#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Channel Helper Bot """
""" helper_string.py """
""" Copyright 2018, Jogle Lew """

import helper_global

helper_string_zh_cn = {
    "development_text": "该功能正在开发中...",
    "permission_denied_text": "你怕不是假的 jogle",
    "reload_cmd_success": "重启好了，很棒棒哦！",
    "reload_cmd_failed": "嗯，好像出现了一些问题呢…",
    "start_cmd_text": "这是由 JogleLew 开发的频道回复助手 Bot 。你可以使用 /help 命令查看详细使用说明。", 
    "help_cmd_text": "欢迎使用 Channel Helper Bot，本 bot 可以为您的频道提供回复和展示评论信息的入口，从而为频道提供互动的平台。\nGithub链接：https://github.com/JogleLew/channel-helper-bot\n使用此 bot 即为允许本 bot 在您的频道内进行发送、编辑和删除操作，并收集和存储评论信息。\n使用步骤：\n1. 将此 bot 添加为频道管理员。\n2. 使用 /register 命令登记您的频道信息。\n3. 完成。如需更改配置请使用 /option 命令。",
    "add_comment": "添加评论",
    "show_all_comments": "显示所有评论",
    "comment_header": "===== 评论区 =====",
    "comment_empty": "",
    "start_comment_mode": "您已进入评论模式，向我发送消息即可进行评论。使用 /cancel 命令可以中止评论模式。",
    "stop_comment_mode": "您已退出评论模式",
    "comment_success": "评论成功！如需编辑评论，直接编辑已发送的消息即可。",
    "comment_edit_success": "编辑评论成功",
    "prev_page": "上一页",
    "next_page": "下一页",
    "no_prev_page": "没有上一页了",
    "no_next_page": "没有下一页了",
    "register_cmd_text": "请先将本 bot 添加为频道的管理员（注：只需要在频道设置中添加管理员，搜索本 bot 的 username，点击添加即可），并授予 bot 发送、编辑、删除消息的权限。然后从您的频道中转发一条消息（这条消息不能是转发的别处的消息）给我，以便我获取频道的 ID。",
    "register_cmd_invalid": "这条消息中似乎不包含频道信息呢...请从您的频道中转发一条消息给我",
    "register_cmd_not_admin": "您看起来不是频道的管理员呢，本 bot 无法为您进行登记",
    "register_cmd_no_permission": "检测到您没有给本 bot 提供发送、编辑、删除消息的权限。修改完权限后，请重新执行登记操作。",
    "register_cmd_no_info": "本 bot 无法获取您的频道信息，请检查是否已经将本 bot 添加为频道管理员。",
    "register_cmd_failed": "频道信息记录失败，如有问题请联系管理员 @JogleLew",
    "register_cmd_success": "您的频道信息已成功记录，并启用了默认的评论设置。如需修改配置，请使用 /option 命令。",
    "option_no_channel": "您还没有登记过频道信息，请先使用 /register 命令完成登记。",
    "option_delete": "删除频道记录",
    "option_record_deleted": "频道记录已删除，感谢您的使用！",
    "option_finish": "完成配置",
    "option_finished": "配置已完成",
    "option_choose_channel": "请选择一个频道以进行配置",
    "option_choose_item": "请选择一个项目以进行配置\nmode: bot 的工作模式\nrecent: 在频道中显示的评论数量\nnotify: 新评论提醒\nlang: 评论功能使用的语言",
    "option_choose_mode_value": "本 bot 有三种工作模式\n模式 0: 手动模式。当频道中新增消息时，bot 不会自动创建评论消息。当频道管理员使用 /comment 回复需要评论的原始消息时，bot 才会创建评论消息。如果 /comment 命令不起作用，请检查是否授予 bot 删除消息的权限。\n模式 1: 自动模式。当频道中新增消息时，bot 自动创建评论消息。该模式能保持原始频道消息不被修改。\n模式 2: 自动模式(beta)。当频道中新增消息时，bot 会尝试编辑原消息，显示添加评论按钮。如果编辑失败则直接创建评论消息。该模式能尽可能减少频道里的评论区数量。\n请选择您所需要的工作模式：",
    "option_choose_recent_value": "在频道中仅显示最近的若干条消息。请选择频道显示的最近条目数量：",
    "option_choose_notify_value": "您可以选择当频道收到新评论时是否开启提醒功能。0代表关闭，1代表开启。将在从下一条消息开始生效。",
    "option_choose_lang_value": "请选择频道中评论功能采用的语言。",
    "option_update_success": "配置更新成功",
    "option_update_failed": "配置更新失败",
    "clean_cmd_start": "正在进行检查，请稍候...",
    "clean_cmd_deleted": "删除记录成功",
    "clean_cmd_set": "设置成功",
    "fwd_source": "消息来源: ",
    "prev_msg": "上一条消息",
    "next_msg": "下一条消息",
    "no_message_detail": "未找到消息",
    "back_to_msg_list": "返回消息列表",
    "msg_from": "消息来源：",
    "delete_msg": "删除消息",
    "delete_success": "消息删除成功",
    "ban_user": "封禁用户",
    "unban_user": "解封用户",
    "user_banned": "已封禁该用户",
    "user_banned_failed": "封禁失败，该用户可能已被封禁",
    "user_unbanned": "用户已解封",
    "banned_prompt": "频道管理员不允许你进行评论操作",
    "new_comment_message": "您收到了新的评论",
    "target_message": "目标消息："
}

helper_string_en_us = {
    "development_text": "This feature is under development...",
    "permission_denied_text": "No Permission",
    "reload_cmd_success": "Reloaded. Good luck.",
    "reload_cmd_failed": "Problem occurred when reloading.",
    "start_cmd_text": "This is Jogle Lew's Channel Helper Bot. Use /help command for more information.", 
    "help_cmd_text": "Thanks for choosing Channel Helper Bot. This bot can manage and display comments in your channel, providing a new way of communication between channel owner and subscribers. The code of Channel Helper Bot is available on Github: https://github.com/JogleLew/channel-helper-bot\nBy using this bot, you allow the bot send, edit and delete messages in your channel, as well as collect and store users' comments. \nHow to use:\n1. Add this bot to your channel as an admin. \n2. Send /register command to enable the comment feature in your channel\n3. Done. Use /option command to config",
    "add_comment": "Add Comment",
    "show_all_comments": "Show All Comments",
    "comment_header": "===== Comments =====",
    "comment_empty": "",
    "start_comment_mode": "[Enter Comment Mode] leave a comment by sending me a message. Use /cancel to quit comment mode",
    "stop_comment_mode": "[Quit Comment Mode]",
    "comment_success": "[Comment Successfully] If you want to edit your comment, just modify the message you sent.",
    "comment_edit_success": "[Edit Successfully]",
    "prev_page": "Prev Page",
    "next_page": "Next Page",
    "no_prev_page": "No previous page",
    "no_next_page": "No next page",
    "register_cmd_text": "Please make sure you add this bot to your channel as an admin (Channel Settings -> Add Admin -> Search bot's username -> Click), and grant the permissions of Send, Edit and Delete Messages to the bot. Then forward an original message (the message itself shouldn't be an forwarded message) from your channel to the bot.",
    "register_cmd_invalid": "This message contains no channel info. Please forward me an original message from your channel.",
    "register_cmd_not_admin": "You are not the channel admin, so you're not allowed to register.",
    "register_cmd_no_permission": "Permission check error. Make sure you grant the permissions of Send, Edit and Delete Messages to the bot and register again.",
    "register_cmd_no_info": "This bot cannot access your channel. Please check whether the bot is an admin of your channel.",
    "register_cmd_failed": "Registration Failed. Please contact the developer @JogleLew for further assistance.",
    "register_cmd_success": "Registered Successfully. Default config is applied to your channel. Use /option command to modify your config.",
    "option_no_channel": "No registration info found. Please use /register command first.",
    "option_delete": "Delete registration",
    "option_record_deleted": "Registration record is deleted. Thanks for your using!",
    "option_finish": "Finish",
    "option_finished": "Config updated.",
    "option_choose_channel": "Please choose a channel to config.",
    "option_choose_item": "Now, you can modify these items\nmode: working mode of the bot\nrecent: the maximum number of comments shown in channel\nnotify: receive notifications when new comments occur\nlang: language of comment buttons and text in your channel",
    "option_choose_mode_value": "There are 3 modes.\nMode 0: Manual Mode. No commment message will appear automatically, unless the channel admin reply the channel post with /comment .\nMode 1: Auto Mode. The bot adds comment message automatically, without modifying original post. \nMode 2: Auto Mode (beta). The bot modifies the channel post to add comment buttons, or add comment message if failed. Using this mode can reduce the number of blank comment message.\nPlease choose the working mode: ",
    "option_choose_recent_value": "In a comment message, only the most recent comments appear. Please choose the number of shown comments:",
    "option_choose_notify_value": "You can choose whether you will receive a notification if new comment comes. 0 stands for no, 1 stands for yes.",
    "option_choose_lang_value": "Choose the language of comment buttons and text in your channel. Take effect when the next message is coming",
    "option_update_success": "Config updated",
    "option_update_failed": "Failed to update config",
    "clean_cmd_start": "Now checking, Please wait...",
    "clean_cmd_deleted": "Registration record deleted",
    "clean_cmd_set": "Auto schedule set",
    "fwd_source": "From: ",
    "prev_msg": "Prev Comment",
    "next_msg": "Next Comment",
    "no_message_detail": "No comment detail found",
    "back_to_msg_list": "Back to comment list",
    "msg_from": "From: ",
    "delete_msg": "Delete Comment",
    "delete_success": "Comment deleted.",
    "ban_user": "Ban User",
    "unban_user": "Unban User",
    "user_banned": "User banned.",
    "user_banned_failed": "Failed to ban this user. This user might have been banned.",
    "user_unbanned": "User unbanned.",
    "banned_prompt": "You are not allowed to leave comments in this channel.",
    "new_comment_message": "New comment received.",
    "target_message": "Target message: "
}

lang_config = {
    "zh-CN": helper_string_zh_cn,
    "en-US": helper_string_en_us
}

for lang_code, lang_dict in lang_config.items():
    for item, value in lang_dict.items():
        helper_global.assign(item, value, lang=lang_code)
