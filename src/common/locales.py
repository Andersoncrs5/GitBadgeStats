"""Translations for the GitHub streak card."""

from typing import TypedDict


class LocaleTranslations(TypedDict):
    """Translation keys required by the streak card."""

    weekdays: list[str]
    status_active: str
    status_pending: str
    status_start: str
    card_title: str
    streak_label: str
    longest_label: str
    commits_label: str
    days_unit: str
    active_pill: str
    inactive_pill: str

TRANSLATIONS: dict[str, LocaleTranslations] = {
    "en": {
        "weekdays": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "status_active": "Streak active! Flame is burning today",
        "status_pending": "Flame unlit • Commit today to keep your streak!",
        "status_start": "Flame unlit • Commit to start your streak!",
        "card_title": "{name}'s GitHub Streak",
        "streak_label": "DAY STREAK",
        "longest_label": "Longest Streak",
        "commits_label": "Total Commits",
        "days_unit": "days",
        "active_pill": "🔥 STREAK ACTIVE",
        "inactive_pill": "❄️ FLAME UNLIT",
    },
    "pt": {
        "weekdays": ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"],
        "status_active": "Ofensiva mantida! Chama acesa hoje",
        "status_pending": "Chama apagada • Faça um commit hoje!",
        "status_start": "Chama apagada • Faça um commit para iniciar!",
        "card_title": "Ofensiva de {name}",
        "streak_label": "DIAS DE OFENSIVA",
        "longest_label": "Maior Ofensiva",
        "commits_label": "Total de commits",
        "days_unit": "dias",
        "active_pill": "🔥 OFENSIVA ATIVA",
        "inactive_pill": "❄️ CHAMA APAGADA",
    },
    "es": {
        "weekdays": ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
        "status_active": "¡Racha activa! La llama sigue encendida hoy",
        "status_pending": "Llama apagada • ¡Haz un commit hoy para mantener tu racha!",
        "status_start": "Llama apagada • ¡Haz un commit para empezar tu racha!",
        "card_title": "Racha de GitHub de {name}",
        "streak_label": "DÍAS DE RACHA",
        "longest_label": "Racha más larga",
        "commits_label": "Commits totales",
        "days_unit": "días",
        "active_pill": "🔥 RACHA ACTIVA",
        "inactive_pill": "❄️ LLAMA APAGADA",
    },
    "fr": {
        "weekdays": ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"],
        "status_active": "Série active ! La flamme brûle aujourd'hui",
        "status_pending": "Flamme éteinte • Faites un commit aujourd'hui pour continuer votre série !",
        "status_start": "Flamme éteinte • Faites un commit pour commencer votre série !",
        "card_title": "Série GitHub de {name}",
        "streak_label": "JOURS DE SÉRIE",
        "longest_label": "Plus longue série",
        "commits_label": "Commits au total",
        "days_unit": "jours",
        "active_pill": "🔥 SÉRIE ACTIVE",
        "inactive_pill": "❄️ FLAMME ÉTEINTE",
    },
    "de": {
        "weekdays": ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"],
        "status_active": "Serie aktiv! Die Flamme brennt heute",
        "status_pending": "Flamme aus • Erstelle heute einen Commit, um deine Serie fortzusetzen!",
        "status_start": "Flamme aus • Erstelle einen Commit, um deine Serie zu starten!",
        "card_title": "GitHub-Serie von {name}",
        "streak_label": "TAGE IN FOLGE",
        "longest_label": "Längste Serie",
        "commits_label": "Commits insgesamt",
        "days_unit": "Tage",
        "active_pill": "🔥 SERIE AKTIV",
        "inactive_pill": "❄️ FLAMME AUS",
    },
}

SUPPORTED_LOCALES = tuple(TRANSLATIONS)


def get_translations(locale: str) -> LocaleTranslations:
    """Return translations for a supported locale."""
    try:
        return TRANSLATIONS[locale]
    except KeyError as exc:
        supported = ", ".join(SUPPORTED_LOCALES)
        raise ValueError(
            f"Unsupported locale '{locale}'. Supported locales: {supported}"
        ) from exc