from whoop import WhoopClient
from dataclasses import dataclass

SPORT_DCT = {-1: 'Activity',
    0: 'Running',
    1: 'Cycling',
    16: 'Baseball',
    17: 'Basketball',
    18: 'Rowing',
    19: 'Fencing',
    20: 'Field Hockey',
    21: 'Football',
    22: 'Golf',
    24: 'Ice Hockey',
    25: 'Lacrosse',
    27: 'Rugby',
    28: 'Sailing',
    29: 'Skiing',
    30: 'Soccer',
    31: 'Softball',
    32: 'Squash',
    33: 'Swimming',
    34: 'Tennis',
    35: 'Track & Field',
    36: 'Volleyball',
    37: 'Water Polo',
    38: 'Wrestling',
    39: 'Boxing',
    42: 'Dance',
    43: 'Pilates',
    44: 'Yoga',
    45: 'Weightlifting',
    47: 'Cross Country Skiing',
    48: 'Functional Fitness',
    49: 'Duathlon',
    51: 'Gymnastics',
    52: 'Hiking/Rucking',
    53: 'Horseback Riding',
    55: 'Kayaking',
    56: 'Martial Arts',
    57: 'Mountain Biking',
    59: 'Powerlifting',
    60: 'Rock Climbing',
    61: 'Paddleboarding',
    62: 'Triathlon',
    63: 'Walking',
    64: 'Surfing',
    65: 'Elliptical',
    66: 'Stairmaster',
    70: 'Meditation',
    71: 'Other',
    73: 'Diving',
    74: 'Operations - Tactical',
    75: 'Operations - Medical',
    76: 'Operations - Flying',
    77: 'Operations - Water',
    82: 'Ultimate',
    83: 'Climber',
    84: 'Jumping Rope',
    85: 'Australian Football',
    86: 'Skateboarding',
    87: 'Coaching',
    88: 'Ice Bath',
    89: 'Commuting',
    90: 'Gaming',
    91: 'Snowboarding',
    92: 'Motocross',
    93: 'Caddying',
    94: 'Obstacle Course Racing',
    95: 'Motor Racing',
    96: 'HIIT',
    97: 'Spin',
    98: 'Jiu Jitsu',
    99: 'Manual Labor',
    100: 'Cricket',
    101: 'Pickleball',
    102: 'Inline Skating',
    103: 'Box Fitness',
    104: 'Spikeball',
    105: 'Wheelchair Pushing',
    106: 'Paddle Tennis',
    107: 'Barre',
    108: 'Stage Performance',
    109: 'High Stress Work',
    110: 'Parkour',
    111: 'Gaelic Football',
    112: 'Hurling/Camogie',
    113: 'Circus Arts',
    121: 'Massage Therapy',
    123: 'Strength Trainer',
    125: 'Watching Sports',
    126: 'Assault Bike',
    127: 'Kickboxing',
    128: 'Stretching',
    230: 'Table Tennis',
    231: 'Badminton',
    232: 'Netball',
    233: 'Sauna',
    234: 'Disc Golf',
    235: 'Yard Work',
    236: 'Air Compression',
    237: 'Percussive Massage',
    238: 'Paintball',
    239: 'Ice Skating',
    240: 'Handball'}


def flatten_dict(d: dict, parent_key: str = '', sep: str = '_') -> dict:
    """
    Flatten a nested dictionary.

    Parameters:
    - d: The dictionary to flatten.
    - parent_key: The prefix key.
    - sep: The separator between parent and child keys.

    Returns:
    - A flattened dictionary.
    """
    l = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            l.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            l.append((new_key, v))
    return dict(l)


@dataclass
class Whoop:
    
    def __init__(self, username: str, password: str, start_date: str, end_date: str = None) -> None:
        self.start_date = start_date
        self.end_date = end_date
        self.client = WhoopClient(username=username, password=password)
        self.profile = self.client.get_profile()


    def list_cycles(self, start_dt: str = None, end_dt: str = None, flat: bool = False, clean: bool = True) -> list:
        if not start_dt:
            start_dt = self.start_date
            
        if not end_dt:
            end_dt = self.end_date
        
        lst = self.client.get_cycle_collection(start_date=start_dt, end_date=end_dt)
        
        if flat:
            lst = [flatten_dict(d=i, parent_key='', sep='_') for i in lst]
        
        if clean:
            for i in lst:
                i['whoop_type'] = 'cycle'
                
                for j in ('start', 'end'):
                    if j in i:
                        i[f"{j}_ts"] = i[j]
                        del i[j]
        
        return lst


    def list_recoveries(self, start_dt: str = None, end_dt: str = None, flat: bool = False, clean: bool = True) -> list:
        if not start_dt:
            start_dt = self.start_date
            
        if not end_dt:
            end_dt = self.end_date
        
        lst = self.client.get_recovery_collection(start_date=start_dt, end_date=end_dt)

        if flat:
            lst = [flatten_dict(d=i, parent_key='', sep='_') for i in lst]
        
        if clean:
            for i in lst:
                i['whoop_type'] = 'recovery'
                
                for j in ('start', 'end'):
                    if j in i:
                        i[f"{j}_ts"] = i[j]
                        del i[j]
        
        return lst


    def list_sleeps(self, start_dt: str = None, end_dt: str = None, flat: bool = False, clean: bool = True) -> list:
        if not start_dt:
            start_dt = self.start_date
            
        if not end_dt:
            end_dt = self.end_date
        
        lst = self.client.get_sleep_collection(start_date=start_dt, end_date=end_dt)
        
        if flat:
            lst = [flatten_dict(d=i, parent_key='', sep='_') for i in lst]
        
        if clean:
            for i in lst:
                i['whoop_type'] = 'sleep'
            
                for j in ('start', 'end'):
                    if j in i:
                        i[f"{j}_ts"] = i[j]
                        del i[j]
                
        return lst


    def list_workouts(self, start_dt: str = None, end_dt: str = None, flat: bool = False, clean: bool = True) -> list:
        if not start_dt:
            start_dt = self.start_date
            
        if not end_dt:
            end_dt = self.end_date
        
        lst = self.client.get_workout_collection(start_date=start_dt, end_date=end_dt)
        
        if flat:
            lst = [flatten_dict(d=i, parent_key='', sep='_') for i in lst]
        
        if clean:
            for i in lst:
                i['whoop_type'] = 'workout'
                i['sport_name'] = SPORT_DCT.get(i['sport_id'])
            
                for j in ('start', 'end'):
                    if j in i:
                        i[f"{j}_ts"] = i[j]
                        del i[j]
        
        return lst
