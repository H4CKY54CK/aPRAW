"""List of Reddit API endpoints known to aPRAW."""
from typing import Dict

BASE_URL = "https://oauth.reddit.com{}?{}"

API_PATH: Dict[str, str] = {
    "comment"                     : "/r/{sub}/comments/{submission}/_/{id}",
    "compose"                     : "/api/compose",
    "sub_friend"                  : "/r/{sub}/api/friend",
    "sub_unfriend"                : "/r/{sub}/api/unfriend",
    "info"                        : "/api/info",
    "me"                          : "/api/v1/me",
    "me_karma"                    : "/api/v1/me/karma",
    "message_inbox"               : "/message/inbox",
    "message_sent"                : "/message/sent",
    "message_unread"              : "/message/unread",
    "mod_approve"                 : "/api/approve",
    "mod_distinguish"             : "/api/distinguish",
    "mod_ignore_reports"          : "/api/ignore_reports",
    "mod_lock"                    : "/api/lock",
    "mod_remove"                  : "/api/remove",
    "mod_show_comment"            : "/api/show_comment",
    "mod_sticky"                  : "/api/set_subreddit_sticky",
    "mod_unignore_reports"        : "/api/unignore_reports",
    "mod_unlock"                  : "/api/unlock",
    "moderated"                   : "/user/{user}/moderated_subreddits",
    "modmail_conversation"        : "/api/mod/conversations/{id}",
    "modmail_conversation_action" : "/api/mod/conversations/{id}/{action}",
    "modmail_conversations"       : "/api/mod/conversations",
    "morechildren"                : "/api/morechildren",
    "post_delete"                 : "/api/del",
    "post_hide"                   : "/api/hide",
    "post_marknsfw"               : "/api/marknsfw",
    "post_save"                   : "/api/save",
    "post_spoiler"                : "/api/spoiler",
    "post_unhide"                 : "/api/unhide",
    "post_unmarknsfw"             : "/api/unmarknsfw",
    "post_unsave"                 : "/api/unsave",
    "post_unspoiler"              : "/api/unspoiler",
    "post_vote"                   : "/api/vote",
    "quarantine_opt_in"           : "/api/quarantine_optin",
    "quarantine_opt_out"          : "/api/quarantine_optout",
    "removal_comment_message"     : "api/v1/modactions/removal_comment_message",
    "removal_link_message"        : "api/v1/modactions/removal_link_message",
    "removal_reasons"             : "api/v1/modactions/removal_reasons",
    "reply"                       : "/api/comment",
    "submission"                  : "/r/{sub}/comments/{id}",
    "subreddit"                   : "/r/{sub}",
    "subreddit_about"             : "/r/{sub}/about",
    "subreddit_banned"            : "/r/{sub}/about/banned",
    "subreddit_comments"          : "/r/{sub}/comments",
    "subreddit_edited"            : "/r/{sub}/about/edited",
    "subreddit_flair"             : "/r/{sub}/api/flair",
    "subreddit_hot"               : "/r/{sub}/hot",
    "subreddit_log"               : "/r/{sub}/about/log",
    "subreddit_moderators"        : "/r/{sub}/about/moderators",
    "subreddit_modqueue"          : "/r/{sub}/about/modqueue",
    "subreddit_new"               : "/r/{sub}/new",
    "subreddit_random"            : "/r/{sub}/random",
    "subreddit_removal_reason"    : "/api/v1/{sub}/removal_reasons/{id}",
    "subreddit_removal_reasons"   : "/api/v1/{sub}/removal_reasons",
    "subreddit_reports"           : "/r/{sub}/about/reports",
    "subreddit_rising"            : "/r/{sub}/rising",
    "subreddit_settings"          : "/r/{sub}/about/edit",
    "subreddit_spam"              : "/r/{sub}/about/spam",
    "subreddit_top"               : "/r/{sub}/top",
    "subreddit_unmoderated"       : "/r/{sub}/about/unmoderated",
    "subreddits_new"              : "/subreddits/new",
    "user_about"                  : "/user/{user}/about",
    "user_comments"               : "/user/{user}/comments",
    "user_submissions"            : "/user/{user}/submitted",
    "wiki"                        : "/r/{sub}/wiki/pages",
    "wiki_alloweditor"            : "/r/{sub}/api/wiki/alloweditor/{act}",
    "wiki_edit"                   : "/r/{sub}/api/wiki/edit",
    "wiki_hide"                   : "/r/{sub}/api/wiki/hide",
    "wiki_page"                   : "/r/{sub}/wiki/{page}",
    "wiki_page_revisions"         : "/r/{sub}/wiki/revisions/{page}",
    "wiki_revert"                 : "/r/{sub}/api/wiki/revert",
    "wiki_revisions"              : "/r/{sub}/wiki/revisions",
    "submit"                      : "/api/submit",
}
