from django.core.management.base import BaseCommand
from django.db import transaction

from aiarena.core.models import Bot, SeasonParticipation, Season
from aiarena.core.stats.stats_generator import StatsGenerator


class Command(BaseCommand):
    help = "Runs the generate stats db routine to generate bot stats."


    def add_arguments(self, parser):
        parser.add_argument('--botid', type=int, help="The bot id to generate the stats for. "
                                                       "If this isn't supplied, all bots will have "
                                                       "their stats generated.")

    def handle(self, *args, **options):
        bot_id = options['botid']
        if bot_id is not None:
            sp = SeasonParticipation.objects.get(season=Season.get_current_season(), bot_id=bot_id)
            with transaction.atomic():
                sp.lock_me()
                self.stdout.write(f'Generating current season stats for bot {bot_id}...')
                StatsGenerator.update_stats(sp)
        else:
            for sp in SeasonParticipation.objects.filter(season=Season.get_current_season()):
                with transaction.atomic():
                    sp.lock_me()
                    self.stdout.write(f'Generating current season stats for bot {sp.bot_id}...')
                    StatsGenerator.update_stats(sp)

        self.stdout.write('Done')
