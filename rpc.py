#
# A TF2 RPC script by EmeraldSnorlax
# https://github.com/EmeraldSnorlax
# https://steamcommunity.com/id/EmeraldSnorlax/
#



import tkinter
import easygui as gui
import os
import time
import sys
from pypresence import Presence
import tailer

# RPC Client ID. Do not change.
CLIENT_ID = '635786070625091584'
RPC = Presence(client_id=CLIENT_ID)
RPC.connect()

def msg(text):
    gui.msgbox(text, 'TF2 RPC')

# Grab the log file from tf_path.txt. Encoding is utterly scuffed, for some reason. Perhaps it's just my machine...
f = open('tf_path.txt', 'r', encoding="ISO-8859-15")
tf_folder = f.read()
log_file = tf_folder.rstrip('\n') + 'tf/console.log'
f.close()

# Check if the log file actually exists.
if os.path.isfile(log_file):
    print('Log file found')
    msg('Found your TF2 log file. Press OK to start.')
else:
    print('No log file found, exiting...')
    msg('No log file found. Try deleting tf_path.txt \nand running main.py again.')
    sys.exit()

details = 'Waiting for an action...'
state = 'Idle'
image = 'tf2'


def update(details, state, image):
    RPC.update(large_image=image, large_text='A TF2 RPC script made by EmeraldSnorlax.', details=details, state=state)

update(details, state, image)

# Tail the log file
for line in tailer.follow(open(log_file)):
    #print(line)
    # Uncomment the line above (ie, remove the '#') to output all information. This may decrease performance,
    # so it is left disabled by default.
    # Only enable if debugging
    
    # Read the latest output and check for each case.

    if '[PartyClient] Requesting queue for 12v12 Casual Match' in line:
        details = 'Casual'
        state = 'In Queue'
        image = 'tf2'
        RPC.update(large_image=image, large_text='A TF2 RPC script made by EmeraldSnorlax.', details=details, state=state, start=time.time())
    elif '[PartyClient] Leaving queue for match group 12v12 Casual Match' in line:
        details = 'Casual'
        state = 'Left the Queue'
        image = 'tf2'
        update(details, state, image)
    elif '[PartyClient] Entering queue for match group 6v6 Ladder Match' in line:
        details = 'Competitive'
        state = 'In Queue'
        image = 'tf2'
        RPC.update(large_image=image, large_text='A TF2 RPC script made by EmeraldSnorlax.', details=details, state=state, start=time.time())
    elif '[PartyClient] Leaving queue for match group 6v6 Ladder Match' in line:
        details = 'Competitive'
        state = 'Left the Queue'
        image = 'tf2'
        update(details, state, image)
    elif '[PartyClient] Entering queue for match group MvM MannUp' in line:
        details = 'MvM Mann Up'
        state = 'In Queue'
        image = 'mann_vs_machine'
        RPC.update(large_image=image, large_text='A TF2 RPC script made by EmeraldSnorlax.', details=details, state=state, start=time.time())
    elif '[PartyClient] Entering queue for match group MvM Practice' in line:
        details = 'MvM Boot Camp'
        state = 'In Queue'
        image = 'mann_vs_machine'
        RPC.update(large_image=image, large_text='A TF2 RPC script made by EmeraldSnorlax.', details=details, state=state, start=time.time())
    elif '[PartyClient] Leaving queue for match group MvM MannUp' in line:
        details = 'MvM Mann Up'
        state = 'Left the Queue'
        image = 'mann_vs_machine'
        update(details, state, image)
    elif '[PartyClient] Leaving queue for match group MvM Practice' in line:
        details = 'MvM Boot Camp'
        state = 'Left the Queue'
        image = 'mann_vs_machine'
        update(details, state, image)
    elif 'Disconnecting' in line or 'Sending request to abandon current match' in line:
        details = 'Main Menu'
        state = 'Idle'
        image = 'tf2'
        update(details, state, image)
    elif 'CTFGCClientSystem::ShutdownGC' in line:
        print('Game Client closed')
        msg('It looks like your TF2 client closed. \n Exiting...')
        sys.exit()


    #
    # Check map name.
    # Bittersweet that TF2 only gets an update once every 4 years. It means I won't need to update this list often.
    #
    # Maps are listed in alphabetical order in terms of their spoken name, not literal map file name.
    # A/D is listed as CP, apparently.
    #
    # Gamemodes are listed in alphabetical order.
    #
    # TL:DR the maps are in the same order as this wiki page: https://wiki.teamfortress.com/wiki/List_of_maps#Maps
    #
    # To clarify variable names:
    # > current_map is the map as reported back from console by TF2.
    # > map is the actual map name as spoken, and what is displayed in the RPC.
    # For example, current_map might be 'pl_badwater' and map would be 'Badwater Basin.'
    #


    if 'Map: ' in line:
        current_map = line[5:]
        # Capture the Flag Maps
        if current_map == 'ctf_2fort':
            map = '2Fort'
            gamemode = 'Capture the Flag'
        elif current_map == 'ctf_2fort_invasion':
            map = '2Fort Invasion'
            gamemode = 'Capture the Flag'
        elif current_map == 'ctf_doublecross':
            map = 'Double Cross'
            gamemode = 'Capture the Flag'
        elif current_map == 'ctf_landfall':
            map = 'Landfall'
            gamemode = 'Capture the Flag'
        elif current_map == 'ctf_sawmill':
            map = 'Sawmill'
            gamemode = 'Capture the Flag'
        elif current_map == 'ctf_turbine':
            map = 'Turbine'
            gamemode = 'Capture the Flag'
        elif current_map == 'ctf_well':
            map = 'Well'
            gamemode = 'Capture the Flag'

        # Control Point Maps
        elif current_map == 'cp_5gorge':
            map = '5Gorge'
            gamemode = '5CP'
        elif current_map == 'cp_badlands':
            map = 'Badlands'
            gamemode = '5CP'
        elif current_map == 'cp_coldfront':
            map = 'Coldfront'
            gamemode = '5CP'
        elif current_map == 'cp_fastlane':
            map = 'Fastlane'
            gamemode = '5CP'
        elif current_map == 'cp_foundry':
            map = 'Foundry'
            gamemode = '5CP'
        elif current_map == 'cp_freight_final1':
            map = 'Freight'
            gamemode = '5CP'
        elif current_map == 'cp_granary':
            map = 'Granary'
            gamemode = '5CP'
        elif current_map == 'cp_gullywash_final1':
            map = 'Gullywash'
            gamemode = '5CP'
        elif current_map == 'cp_metalworks':
            map = 'Metalworks'
            gamemode = '5CP'
        elif current_map == 'cp_powerhouse':
            map = 'Metalworks'
            gamemode = 'Control Points'
        elif current_map == 'cp_process_final':
            map = 'Process'
            gamemode = '5CP'
        elif current_map == 'cp_sunshine_event':
            map = 'Sinshine'
            gamemode == '5CP'
        elif current_map == 'cp_snakewater_final1':
            map = 'Snakewater'
            gamemode = '5CP'
        elif current_map == 'cp_sunshine':
            map = 'Sunshine'
            gamemode = '5CP'
        elif current_map == 'cp_vanguard':
            map = 'Vanguard'
            gamemode = '5CP'
        elif current_map == 'cp_well':
            map = 'Well'
            gamemode = '5CP'
        elif current_map == 'cp_yukon_final':
            map = 'Yukon'
            gamemode = '5CP'

        # Attack / Defend Maps
        elif current_map == 'cp_dustbowl':
            map = 'Dustbowl'
            gamemode = 'Attack / Defend'
        elif current_map == 'cp_egypt_final':
            map = 'Egypt'
            gamemode = 'Attack / Defend'
        elif current_map == 'cp_gorge':
            map = 'Gorge'
            gamemode = 'Attack / Defend'
        elif current_map == 'cp_gorge_event':
            map = 'Gorge Event'
            gamemode = 'Attack / Defend'
        elif current_map == 'cp_gravelpit':
            map = 'Gravel Pit'
            gamemode = 'Attack / Defend'
        elif current_map == 'cp_junction_final':
            map = 'Junction'
            gamemode = 'Attack / Defend'
        elif current_map == 'cp_manor_event':
            map = 'Mann Manor'
            gamemode = 'Attack / Defend'
        elif current_map == 'cp_mercenarypark':
            map = 'Mercenary Park'
            gamemode = 'Attack / Defend'
        elif current_map == 'cp_mossrock':
            map = 'Mossrock'
            gamemode = 'Attack / Defend'
        elif current_map == 'cp_mountainlab':
            map = 'Mountain Lab'
            gamemode = 'Attack / Defend'
        elif current_map == 'cp_snowplow':
            map = 'Snowplow'
            gamemode = 'Attack / Defend'
        elif current_map == 'cp_steel':
            map = 'Steel'
            gamemode = 'Attack / Defend'
        elif current_map == 'cp_degrootkeep':
            map = 'DeGroot Keep'
            gamemode = 'A/D Medieval Mode'
        elif current_map == 'cp_standin_final':
            map = 'Standin'
            gamemode = 'CP Domination'

        # Territorial Control
        elif current_map == 'tc_hydro':
            map = 'Hydro'
            gamemode = 'Territory Control'

        # Payload Maps
        elif current_map == 'pl_badwater':
            map = 'Badwater Basin'
            gamemode = 'Payload'
        elif current_map == 'pl_barnblitz':
            map = 'Barnblitz'
            gamemode = 'Payload'
        elif current_map == 'pl_borneo':
            map = 'Borneo'
            gamemode = 'Payload'
        elif current_map == 'pl_fifthcurve_event':
            map = 'Brimstone'
            gamemode = 'Payload'
        elif current_map == 'pl_enclosure_final': # Yes. I skipped pl_cactuscanyon (Cactus Canyon).
            map = 'Enclosure'
            gamemode = 'Payload'
        elif current_map == 'pl_frontier_final':
            map = 'Frontier'
            gamemode = 'Payload'
        elif current_map == 'pl_goldrush':
            map = 'Gold Rush'
            gamemode = 'Payload'
        elif current_map == 'pl_rumble_event':
            map = 'Gravestone'
            gamemode = 'Payload'
        elif current_map == 'pl_millstone_event':
            map = 'Hellstone'
            gamemode = 'Payload'
        elif current_map == 'pl_hoodoo_final':
            map = 'Hoodoo'
            gamemode = 'Payload'
        elif current_map == 'pl_precipice_event_final':
            map = 'Precipice'
            gamemode = 'Payload'
        elif current_map == 'pl_snowycoast':
            map = 'Snowycoast'
            gamemode = 'Payload'
        elif current_map == 'pl_swiftwater_final1':
            map = 'Swiftwater'
            gamemode = 'Payload'
        elif current_map == 'pl_thundermountain':
            map = 'Thunder Mountain'
            gamemode = 'Payload'
        elif current_map == 'pl_upward':
            map = 'Upward'
            gamemode = 'Final'
        # Payload Race Maps
        elif current_map == 'plr_bananabay':
            map = 'Banana Bay'
            gamemode = 'Payload Race'
        elif current_map == 'plr_hightower_event':
            map = 'Helltower'
            gamemode = 'Payload Race'
        elif current_map == 'plr_hightower':
            map = 'Hightower'
            gamemode = 'Payload Race'
        elif current_map == 'plr_nightfall_final':
            map = 'Nightfall'
            gamemode = 'Payload Race'
        elif current_map == 'plr_pipeline':
            map = 'Pipeline'
            gamemode = 'Payload Race'

        # Arena Maps
        elif current_map == 'arena_badlands':
            map = 'Badlands'
            gamemode = 'Arena'
        elif current_map == 'area_byre':
            map = 'Byre'
            gamemode = 'Arena'
        elif current_map == 'arena_granary':
            map = 'Granary'
            gamemode = 'Arena'
        elif current_map == 'arena_lumberyard':
            map = 'Lumberyard'
            gamemode = 'Arena'
        elif current_map == 'arena_nucleus':
            map = 'Nucleus'
            gamemode = 'Arena'
        elif current_map == 'arena_offblast_final':
            map = 'Offblast'
            gamemode = 'Arena'
        elif current_map == 'arena_ravine':
            map = 'Ravine'
            gamemode = 'Arena'
        elif current_map == 'arena_sawmill':
            map = 'Sawmill'
            gamemode = 'Arena'
        elif current_map == 'arena_watchtower':
            map = 'Watchtower'
            gamemode = 'Arena'
        elif current_map == 'arena_well':
            map = 'Arena'
            gamemode = 'Well'

        # KOTH Maps
        elif current_map == 'koth_brazil':
            map = 'Brazil'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_bagel_event':
            map = 'Cauldron'
            gamemode == 'King of the Hill'
        elif current_map == 'koth_viaduct_event':
            map = 'Eyeaduct'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_lakeside_event':
            map = 'Ghost Fort'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_harvest_final':
            map = 'Harvest'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_harvest_event':
            map = 'Harvest Event'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_highpass':
            map = 'Highpass'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_king':
            map = 'Kong King'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_lakeside_final':
            map = 'Lakeside'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_slaughter_event':
            map = 'Laughter'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_lazarus':
            map = 'Lazarus'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_maple_ridge_event':
            map = 'Maple Ridge Event'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_moonshine_event':
            map = 'Moonshine Event'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_nucleus':
            map = 'Nucleus'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_probed':
            map = 'Probed'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_sawmill':
            map = 'Sawmill'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_slasher':
            map = 'Slasher'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_suijin':
            map = 'Suijin'
            gamemode = 'King of the Hill'
        elif current_map == 'koth_viaduct':
            map = 'Viaduct'
            gamemode = 'King of the Hill'

        # Special Delivery Maps
        elif current_map == 'sd_doomsday_event':
            map = 'Carnival of Carnage'
            gamemode = 'Special Delivery'
        elif current_map == 'sd_doomsday':
            map = 'Doomsday'
            gamemode = 'Special Delivery'

        # Skipping the training and devtest maps and straight to MvM
        elif current_map == 'mvm_bigrock':
            map = 'Bigrock'
            gamemode = 'Mann vs. Machine'
        elif current_map == 'mvm_coaltown':
            map = 'Coal Town'
            gamemode = 'Mann vs. Machine'
        elif current_map == 'mvm_decoy':
            map = 'Decoy'
            gamemode = 'Mann vs. Machine'
        elif current_map == 'mvm_ghost_town': # Yes. I skipped mvm_example (Example)
            map = 'Ghost Town'
            gamemode = 'Mann vs. Machine'
        elif current_map == 'mvm_mannhattan':
            map = 'Mannhattan'
            gamemode = 'Mann vs. Machine'
        elif current_map == 'mvm_mannworks':
            map = 'Mannworks'
            gamemode = 'Mann vs. Machine'
        elif current_map == 'mvm_rottenburg':
            map = 'Rottenburg'
            gamemode = 'Mann vs. Machine'

        # Mannpower Maps. Yes; I skipped rd_asteroid (Asteroid Robot Destruction)
        elif current_map == 'ctf_foundry':
            map = 'Foundry'
            gamemode = 'Mannpower'
        elif current_map == 'ctf_gorge':
            map = 'Gorge'
            gamemode = 'Mannpower'
        elif current_map == 'ctf_hellfire':
            map = 'Hellfire'
            gamemode = 'Mannpower'
        elif current_map == 'ctf_thundermountain':
            map = 'Thunder Mountain'
            gamemode = 'Mannpower'

        # PASS Time Maps.
        # It's a shame no one plays this anymore.
        # It was a really fun gamemode.
        elif current_map == 'pass_brickyard':
            map = 'Brickyard'
            gamemode = 'PASS Time'
        elif current_map == 'pass_district':
            map = 'District'
            gamemode = 'PASS Time'
        elif current_map == 'pass_timbertown':
            map = 'Timbertown'
            gamemode = 'PASS Time'

        # Player Destruction Maps
        elif current_map == 'pd_monsterbash':
            map = 'Monster Bash'
            gamemode = 'Player Destruction'
        elif current_map == 'pd_pit_of_death_event':
            map = 'Pit of Death'
            gamemode = 'Player Destruction'
        elif current_map == 'pd_watergate':
            map = 'Watergate'
            gamemode = 'Player Destruction'
        else:
            map = current_map
            gamemode = 'An unoffical map'

        # Rip my (3) braincells. I never want to have to transcribe this again.

        # Set image
        if gamemode == '5CP' or gamemode == 'Attack / Defend' or gamemode == 'Control Points' or gamemode == 'King of the Hill' or gamemode == 'Territory Control':
            image = 'king_of_the_hill'
        elif gamemode == 'Capture the Flag':
            image = 'capture_the_flag'
        elif gamemode == 'Mannpower':
            image = 'mannpower'
        elif gamemode == 'Mann vs. Machine':
            image = 'mann_vs_machine'
        elif gamemode == 'PASS Time':
            image = 'pass_time'
        elif gamemode == 'Payload':
            image = 'payload'
        elif gamemode == 'Payload Race':
            image = 'payload_race'


        RPC.update(large_image=image, large_text='A TF2 RPC script made by EmeraldSnorlax.', details=map, state=gamemode, start=time.time())
