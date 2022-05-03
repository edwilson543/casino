from games.players.player_interactions import PlayerInteractions
from games.player_base_class import Player
from datetime import datetime
import json

loader = PlayerInteractions(player_object=Player)
test_player = Player(name="test", username="test", password="tst123", active_pot=1000, total_active_stake=0,
                     last_top_up_datetime=datetime(2022, 4, 7, 2, 1),
                     active_session_initial_pot=1000, active_session_start_time=datetime(2022, 5, 1, 3, 4),
                     active_session_top_ups=0, last_session_end_time=datetime(2022, 4, 7, 2, 1))

class TestEncodeDecode:
    def test_encoded_then_decoded_player_unchanged(self):
        encoded_player = loader.encode_player(player=test_player)
        decoded_player = loader.decode_player(serialised_attributes_dict=encoded_player)
        assert test_player == decoded_player

    def test_encoded_then_decoded_player_unchanged_with_json(self):
        encoded_player_json = json.dumps(test_player, default=loader.encode_player)
        decoded_player = json.loads(encoded_player_json, object_hook=loader.decode_player)
        assert test_player == decoded_player
